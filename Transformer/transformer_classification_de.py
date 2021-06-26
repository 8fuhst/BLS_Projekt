import os
#os.environ['CUDA_VISIBLE_DEVICES']='1,2,3'
import numpy as np
import pandas as pd
import tensorflow as tf
import torch
import torch.nn as nn
from transformers import ElectraConfig, ElectraForPreTraining, ElectraTokenizer, ElectraModel
from tensorflow.keras import backend as K

electra = 'german-nlp-group/electra-base-german-uncased'

tokenizer = ElectraTokenizer.from_pretrained(electra, do_lower_case=False, strip_accent=False, add_special_tokens=True,
                                             max_length=768, pad_to_max_length=True, padding=True)

#distil_bert = 'distilbert-base-german-cased'

config = ElectraConfig.from_json_file('../Transformer/electra-config.json')#(dropout=0.2, attention_dropout=0.2, vocab_size=32767, embedding_size= 768)
config.output_hidden_states = False
transformer_model = ElectraModel.from_pretrained(electra, config = config)

def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))

def get_encoding(text):
    #inputs = tokenizer.encode_plus(text, add_special_tokens=True, max_length=768, pad_to_max_length=True,
    #                                         return_attention_mask=True, return_token_type_ids=True, return_tensors="pt")
    inputs = tokenizer(text, max_length=512, pad_to_max_length=True, return_tensors="pt")
    #print(inputs.shape)
    outputs = transformer_model(**inputs)
    last_hidden_state = outputs.last_hidden_state[0]
    return last_hidden_state.detach().numpy()#.flatten()

def get_label(label):
    if label == "positiv":
        return [1,0,0,0]
    elif label == "negativ":
        return [0,0,1,0]
    elif label == "neutral":
        return [0,1,0,0]
    elif label == "irrelevant":
        return [0,0,0,1]
    else:
        print("unknown labbel ", label)

if __name__ == '__main__':
    df = pd.DataFrame(columns = ['text', 'label'])

    ## irrelevant sentences
    path_irr = "data_class/irrelevant_sentences/"
    file_list = list(os.listdir(path_irr))
    for f in file_list:
        if f in ['irrelevant_sentences_webanno_VIII_B_159_08.txt']:
            continue
        #print(f)
        df_irr = pd.read_csv(path_irr+f, sep='\t', header=None, warn_bad_lines=True, error_bad_lines=False)
        df_irr.columns = ['text']
        df_irr = df_irr.sample(frac=0.2,random_state=41)
        df = df.append(df_irr, ignore_index=True)#, columns = ['text', 'encoding', 'label'])

    df['label'] = 'irrelevant'
    #print(df.head)


    ## relevant data
    df_rel = pd.read_csv('data_class/training_sentences_classification.txt', sep='\t', header=None, warn_bad_lines=True, error_bad_lines=False)
    df_rel.columns = ['nr', 'text', 'label']
    df_rel['text'] = df_rel['text'].apply(lambda x: x.replace("#Text=", ""))
    df_rel.drop(['nr'], axis=1, inplace=True)
    #print(df_rel.head)

    df = df.append(df_rel, ignore_index=True)

    '''
    ## old data, train+test
    df_trainold = pd.read_csv('data_class/trainingsData.tsv.txt', sep='\t', header=None, warn_bad_lines=True, error_bad_lines=False)
    df_trainold.columns = ['id', 'text', 'label']
    df_trainold.drop(['id'], axis=1, inplace=True)
    
    df = df.append(df_trainold, ignore_index=True)
    
    df_testold = pd.read_csv('data_class/testData.tsv.txt', sep='\t', header=None, warn_bad_lines=True, error_bad_lines=False)
    df_testold.columns = ['id', 'text', 'label', 'label2', 'label3']
    df_testold.drop(['id'], axis=1, inplace=True)
    df_testold.drop(['label2'], axis=1, inplace=True)
    df_testold.drop(['label3'], axis=1, inplace=True)
    
    df = df.append(df_trainold, ignore_index=True)
    
    df['label'] = df['label'].apply(lambda x: x.replace("revisionsErfolg", "positiv"))
    df['label'] = df['label'].apply(lambda x: x.replace("revisionsMisserfolg", "negativ"))
    '''

    ## shuffle
    train=df.sample(frac=0.75,random_state=41) #random state is a seed value
    test=df.drop(train.index)
    #train=train.sample(frac=0.1,random_state=41) #random state is a seed value
    #test=test.sample(frac=0.1,random_state=41) #random state is a seed value

    print(train.head)

    df.head

    # labels = np.asarray([[0,0,1,0],[0,0,1,0],[0,1,0,0],[1,0,0,0],[0,0,0,1]]).astype('float32')
    train_y_text = train['label'].tolist()
    train_y_l = []
    for l in train_y_text:
        train_y_l.append(get_label(l))

    train_y = np.asarray(train_y_l).astype('float32')
    # print(train_y)

    data_x = []
    #a= tokenize(input_texts, tokenizer)
    #print(a.shape)
    for t in train['text'].tolist():
        sample = get_encoding(t)
        data_x.append(sample)
        #print(sample)

    train_x = np.asarray(data_x).astype('float32')
    #data_np.shape
    #data_np = data_np.transpose()
    train_x.shape

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(100, return_sequences=True, dropout=0.1, recurrent_dropout=0.1)))
    model.add(tf.keras.layers.GlobalMaxPool1D())
    #model.add(tf.keras.layers.Dense(1000, input_dim=393216,activation='relu'))
    model.add(tf.keras.layers.Dense(100,activation='relu'))
    model.add(tf.keras.layers.Dense(50,activation='relu'))
    model.add(tf.keras.layers.Dense(4,activation='softmax'))
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy',f1_m,precision_m, recall_m])
    model.fit(train_x, train_y, epochs=20, batch_size=32)

    model.summary()

    sentences = []
    sentences.append("Die Beschwerde gegen die Nichtzulassung der Revision in dem Urteil des 5. Zivilsenats des Oberlandesgerichts Köln vom 18. April 2007 wird auf Kosten des Klägers zurückgewiesen.")
    sentences.append("II. Die Revision ist begründet")
    sentences.append("II. Die Revision ist unbegründet")
    sentences.append("Apple Inc. introduced a new mobile device today")


    labels_test = np.asarray([[0,0,1,0],[1,0,0,0],[0,0,1,0], [0,0,0,1]]).astype('float32')


    data = []
    #a= tokenize(input_texts, tokenizer)
    #print(a.shape)
    for t in sentences:
        sample = get_encoding(t)
        data.append(sample)
        #print(sample)
    #print(data)

    test_np = np.asarray(data).astype('float32')

    model.predict(test_np)

    test_y_text = test['label'].tolist()
    test_y_l = []
    for l in test_y_text:
        test_y_l.append(get_label(l))

    test_y = np.asarray(test_y_l).astype('float32')

    data_x_t = []
    #a= tokenize(input_texts, tokenizer)
    #print(a.shape)
    for t in test['text'].tolist():
        sample = get_encoding(t)
        data_x_t.append(sample)
    test_x = np.asarray(data_x_t).astype('float32')

    # import pickle

    #
    # Create your model here (same as above)
    #

    model.optimizer = None
    model.compiled_loss = None
    model.compiled_metrics = None

    # Save to file in the current working directory
    pkl_path = "classifier-model"
    model.save(pkl_path)

    # Load from file
    pickle_model = tf.keras.models.load_model(pkl_path, compile=False)

    # evaluate the model

    y_pred = pickle_model.predict(test_x, batch_size=64, verbose=1)
    y_pred_bool = np.argmax(y_pred, axis=1)
    print(y_pred_bool)
    # loss, accuracy, f1_score, precision, recall = model.evaluate(test_x, test_y)

    from sklearn.metrics import classification_report

    y_pred = model.predict(test_x, batch_size=64, verbose=1)
    y_pred_bool = np.argmax(y_pred, axis=1)
    print(y_pred_bool)
    #print(np.argmax(test_y, axis=1))
    print(classification_report(np.argmax(test_y, axis=1), y_pred_bool))