<template>
  <div class="references">
    <VerdictReference v-for="(reference, index) in reasons" v-bind:key="index"
      :section="'bewertung'" :indexInput="reference[0]" :text="reference[1]"/>
    <VerdictReference v-for="(reference, index) in offense" v-bind:key="index"
                      :section="'sachverhalt'" :indexInput="reference[0]" :text="reference[1]"/>
  </div>
</template>

<script>
import VerdictReference from "@/components/VerdictViewComponents/VerdictReference";
export default {
  name: "VerdictReferenceList",
  components: {VerdictReference},
  computed: {
    verdictNode() {
      return this.$store.getters.getVerdictNode
    },
    reasons() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0][1] && this.verdictNode.outgoingReferenceList[0][1].gruende && this.verdictNode.outgoingReferenceList[0][1].gruende.length > 0) {
        return this.verdictNode.outgoingReferenceList[0][1].gruende
      } else if (this.verdictNode.outgoingReferenceList[1] && this.verdictNode.outgoingReferenceList[1].gruende && this.verdictNode.outgoingReferenceList[1].gruende.length > 0) {
        return this.verdictNode.outgoingReferenceList[1].gruende
      } else if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0][2] && this.verdictNode.outgoingReferenceList[0][2].entscheidungsgruende && this.verdictNode.outgoingReferenceList[0][2].entscheidungsgruende.length > 0) {
        return this.verdictNode.outgoingReferenceList[0][2].entscheidungsgruende
      } else if (this.verdictNode.outgoingReferenceList[2] && this.verdictNode.outgoingReferenceList[2].entscheidungsgruende && this.verdictNode.outgoingReferenceList[2].entscheidungsgruende.length > 0) {
        return this.verdictNode.outgoingReferenceList[2].entscheidungsgruende
      } else {
        return []
      }
    },
    offense() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0][3] && this.verdictNode.outgoingReferenceList[0][3].tatbestand && this.verdictNode.outgoingReferenceList[0][3].tatbestand.length > 0) {
        return this.verdictNode.outgoingReferenceList[0][3].tatbestand
      } else if (this.verdictNode.outgoingReferenceList[3] && this.verdictNode.outgoingReferenceList[3].tatbestand && this.verdictNode.outgoingReferenceList[3].tatbestand.length > 0) {
        return this.verdictNode.outgoingReferenceList[3].tatbestand
      } else {
        return []
      }
    }
  },
}
</script>

<style scoped>
  .references {
    padding: 54px 0;
    display: inline-block;
    width: 38%;
    background-color: rgba(206, 206, 206, 0.5);
  }
</style>