<template>
  <div class="references">
    <VerdictReference class="position-absolute" v-for="(refGroup, idx) in tenor" v-bind:key="idx"
                      :section="'bewertung'" :references="refGroup" />
    <VerdictReference class="position-absolute" v-for="(refGroup, idx) in reasons" v-bind:key="idx"
      :section="'bewertung'" :references="refGroup"/>
    <VerdictReference class="position-absolute" v-for="(refGroup, idx) in offense" v-bind:key="idx"
                      :section="'sachverhalt'" :references="refGroup" />
  </div>
</template>

<script>
import VerdictReference from "@/components/VerdictViewComponents/VerdictReference";
export default {
  name: "VerdictReferenceList",
  components: {VerdictReference},
  computed: {
    verdict() {
      return this.$store.getters.getCurrentVerdict
    },
    verdictNode() {
      return this.$store.getters.getVerdictNode
    },
    reasons() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].gruende && this.verdictNode.outgoingReferenceList[0].gruende.length > 0) {
        return this.verdictNode.outgoingReferenceList[0].gruende
      } else if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].entscheidungsgruende && this.verdictNode.outgoingReferenceList[0].entscheidungsgruende.length > 0) {
        return this.matchIndicesReasons(this.verdictNode.outgoingReferenceList[0].entscheidungsgruende)
      } else {
        return []
      }
    },
    offense() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].tatbestand && this.verdictNode.outgoingReferenceList[0].tatbestand.length > 0) {
        return this.matchIndicesOffense(this.verdictNode.outgoingReferenceList[0].tatbestand)
      } else {
        return []
      }
    },
    tenor() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].tenor && this.verdictNode.outgoingReferenceList[0].tenor.length > 0) {
        return [this.verdictNode.outgoingReferenceList[0].tenor]
      } else {
        return []
      }
    }
  },
  methods: {
    matchIndicesOffense(references) {
      const offense = this.verdict.modelledOffense
      const referenceGroupList = []
      let i
      for (i = 0; i < offense.length; i++) {
        const indices = offense[i].indices
        const matchedReferences = references.filter((reference) => {
          return indices.find((possibleIndex) => {
            return possibleIndex + '' === reference.index + '' }) !== undefined
        })

        if (matchedReferences.length > 0) {
          referenceGroupList.push(matchedReferences)
        }
      }
      return referenceGroupList
    },
    matchIndicesReasons(references) {
      const reasons = this.verdict.modelledReasonsForDecision
      const referenceGroupList = []
      let i
      for (i = 0; i < reasons.length; i++) {
        const indices = reasons[i].indices
        const matchedReferences = references.filter((reference) => {
          return indices.find((possibleIndex) => {
            return possibleIndex + '' === reference.index + '' }) !== undefined
        })

        if (matchedReferences.length > 0) {
          referenceGroupList.push(matchedReferences)
        }
      }
      return referenceGroupList
    }
  }
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