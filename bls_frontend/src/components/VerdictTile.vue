<template>
  <div class="card-div">
    <b-card>
      <b-container>
        <b-row>
          <b-col class="entry">
            <b-card-text>{{ verdict.metaData.gericht }}</b-card-text>
          </b-col>
          <b-col class="al-right entry">
            <DropDownText :items="verdict.metaData.aktenzeichen" :id="verdict.id" />
          </b-col>
        </b-row>
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
        <b-row class="bottom-margin">
          <ExpandableText :content="normenStr" />
        </b-row>
        <b-row class="bottom-margin">
          <b-col class="al-center">
            <b-button class="doc-type-tag">{{ verdict.docType }}</b-button>
          </b-col>
        </b-row>
      </b-container>
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
    }
  },
  created() {
    this.normenStr = this.verdict.metaData.normen.join(', ');
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
    padding: 15px 8px;
    height: 54px;
  }

  .text-padding {
    padding: 0px 8px;
  }

  .doc-type-tag {
    height: 54px;
    cursor: auto !important;
    background-color: rgba(255, 0, 0, 0.59);
    border-color: white;
  }

  .bottom-margin {
    margin-bottom: 15px;
  }
</style>