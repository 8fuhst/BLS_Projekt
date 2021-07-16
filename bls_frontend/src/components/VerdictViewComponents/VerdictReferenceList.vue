<template>
  <div class="references">
    <VerdictReference class="position-absolute" v-for="(reference, idx) in tenor" v-bind:key="idx"
                      :section="'bewertung'" :indexInput="reference.index" :text="reference.referenz"/>
    <VerdictReference class="position-absolute" v-for="(reference, idx) in reasons" v-bind:key="idx"
      :section="'bewertung'" :indexInput="reference.index" :text="reference.referenz"/>
    <VerdictReference class="position-absolute" v-for="(reference, idx) in offense" v-bind:key="idx"
                      :section="'sachverhalt'" :indexInput="reference.index" :text="reference.referenz"/>
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
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].gruende && this.verdictNode.outgoingReferenceList[0].gruende.length > 0) {
        return this.verdictNode.outgoingReferenceList[0].gruende
      } else if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].entscheidungsgruende && this.verdictNode.outgoingReferenceList[0].entscheidungsgruende.length > 0) {
        return this.verdictNode.outgoingReferenceList[0].entscheidungsgruende
      } else {
        return [{index: '30', referenz: 'VI ZR 498/19'}]
      }
    },
    offense() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].tatbestand && this.verdictNode.outgoingReferenceList[0].tatbestand.length > 0) {
        return this.verdictNode.outgoingReferenceList[0].tatbestand
      } else {
        return []
      }
    },
    tenor() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].tenor && this.verdictNode.outgoingReferenceList[0].tenor.length > 0) {
        return this.verdictNode.outgoingReferenceList[0].tenor
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