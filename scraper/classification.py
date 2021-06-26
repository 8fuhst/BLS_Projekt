import formatter
import numpy as np
import tensorflow.keras as keras
from Transformer.transformer_classification_de import get_encoding

model_path = "../Transformer/classifier-model"

def get_label(index):
    """
    Matches the classify-index to the associated string-label.

    :param index: The classify-index
    :return: The label
    :rtype: str
    """
    if index == 0:
        return "positiv"
    elif index == 2:
        return "negativ"
    elif index == 3:
        return "irrelevant"
    elif index == 1:
        return "neutral"
    else:
        print("unknown labbel ", index)


def classify(tenor_array):
    """
    Classifies the judgment result of a verdict by analysing the tenor with a trained model.

    :param list(str) tenor_array: The tenor-string as an array of sentences
    :return: 0 -> "positiv", 1 -> "neutral", 2 -> "negativ", 3 -> "irrelevant"
    :rtype: str
    """
    token_list = []
    for s in tenor_array:
        token_list.append(get_encoding(formatter.replace_abbreviations(s)))

    tokens_np = np.asarray(token_list).astype('float32')

    # Load model
    model = keras.models.load_model(model_path)

    prediction = model.predict(tokens_np)
    # finds the index of the highest value in the prediction that isn't 3 because those are irrelevent:
    all_time_index = 3
    all_time_value = 0
    for sentence_prediction in prediction:
        max_index = np.argmax(sentence_prediction)
        if max_index != 3 and all_time_value < sentence_prediction[max_index]:
            all_time_value = sentence_prediction[max_index]
            all_time_index = max_index

    return get_label(all_time_index)
