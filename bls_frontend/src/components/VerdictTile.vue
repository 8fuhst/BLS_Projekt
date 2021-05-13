<template>
  <div>
    <b-card>
      <b-container>
        <b-row>
          <b-col>{{ verdict.metaData.gericht }}</b-col>
          <b-col>
            <DropDownText :items="verdict.metaData.aktenzeichen" />
          </b-col>
        </b-row>
        <b-row>
          <b-col>{{ verdict.metaData.datum }}</b-col>
          <b-col>{{verdict.metaData.ecli}}</b-col>
        </b-row>
        <b-row>
          <ExpandableText :content="normenStr" />
        </b-row>
      </b-container>
      <p>{{ verdict.docType }}</p>
    </b-card>
  </div>
</template>


<script>

import DropDownText from "@/components/DropDownText";
import ExpandableText from "@/components/ExpandableText";
/**
 <MetaData :meta-data="verdict.metaData" />
 <DocType :doc-type="verdict.docType"/>
 <TeaserText :key-sentence="verdict.keySentence" :tenor="verdict.tenor"/>
 */

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
.container {
  border: #42b983;
}
</style>