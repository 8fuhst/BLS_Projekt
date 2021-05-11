<template>
  <div class="container">
    <MetaData :meta-data="verdict.metaData" />
    <DocType :doc-type="verdict.docType"/>
    <TeaserText :key-sentence="verdict.keySentence" :tenor="verdict.tenor"/>
  </div>
</template>

<script>
import MetaData from "@/components/VerdictTileSubComponents/MetaData";
import DocType from "@/components/VerdictTileSubComponents/DocType";
import TeaserText from "@/components/VerdictTileSubComponents/TeaserText";

export default {
  name: "VerdictTile",
  props: {
    verdict: Object,
  },
  components: {TeaserText, DocType, MetaData}
}
</script>

<style scoped>
  .container {
    border: #42b983;
  }
</style>