<template>
  <div class="card-div">
    <b-card>
      <b-container>
        <!-- Gericht/Aktenzeichen row !-->
        <b-row>
          <b-col class="entry">
            <b-card-text>{{ verdict.metaData.gericht }}</b-card-text>
          </b-col>
          <b-col class="al-right entry no-col-padding">
            <DropDownText :items="verdict.metaData.aktenzeichen" :id="verdict.id + 'drop'" />
          </b-col>
        </b-row>

        <!-- Date/Ecli row !-->
        <b-row>
          <b-col class="entry">
            <b-card-text>{{ verdict.metaData.datum }}</b-card-text>
          </b-col>
          <b-col class="al-right entry">
            <b-card-text>
              {{verdict.metaData.ecli}}
            </b-card-text>
          </b-col>
        </b-row>

        <!-- Normen row !--> <!-- TODO: Dafür sorgen, dass die collapsables unabhängig offen bleiben !-->
        <b-row class="bottom-margin">
          <ExpandableText :content="normenStr" :content-brief="normenStrBrief" :id="verdict.id + 'exp'" />
        </b-row>

        <!-- Doctype row !-->
        <b-row class="bottom-margin">
          <b-col class="al-center">
            <div class="doc-type-tag">
              <b-card-text class="doc-type-text">
                {{ verdict.docType }}
              </b-card-text>
            </div>
          </b-col>
        </b-row>
      </b-container>

      <!-- Texte !-->
      <h5>Leitsatz</h5>
      <b-card-text class="text-padding">{{ verdict.keySentence }}</b-card-text>
      <h5>Tenor</h5>
      <b-card-text class="text-padding">{{ verdict.keySentence }}</b-card-text>
    </b-card>
  </div>
</template>


<script>

import DropDownText from "@/components/DropDownText";
import ExpandableText from "@/components/ExpandableText";

export default {
  name: "VerdictTile",
  props: {
    verdict: Object,
  },
  components: {
    ExpandableText,
    DropDownText,
  },
  data() {
    return {
      normenStr: '',
      normenStrBrief: '',
    }
  },
  created() {
    const normen = this.verdict.metaData.normen.slice(0)
    this.normenStr = normen.join(', ');
    if (normen.length > 3) {
      this.normenStrBrief = normen.slice(0, 3).join(', ') + '...'
    } else {
      // TODO: Dann auch dafür sorgen, dass das Ding nicht expandable ist
      this.normenStrBrief = normen.join(', ')
    }
  }
}
</script>

<style scoped>
  .card-div {
    margin-bottom: 20px;
    min-width: 480px;
  }

  .al-right {
    text-align: right;
  }

  .al-center {
    text-align: center;
  }

  .entry {
    padding: 15px 12px;
    height: 54px;
  }

  .text-padding {
    padding: 0px 8px;
  }

  .doc-type-tag {
    display: inline-block;
    height: 54px;
    width: auto;
    cursor: auto !important;
    border-radius: .25rem;
    padding: 14px 12px;

    background-color: rgba(255, 0, 0, 0.59);
  }

  .doc-type-text {
    color: white;
  }

  .bottom-margin {
    margin-bottom: 15px;
  }

  .no-col-padding {
    padding-left: 0px;
    padding-right: 0px;
  }
</style>