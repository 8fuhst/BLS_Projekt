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

/**
 * Component to build the VerdictReferenceList
 *
 */
export default {
  name: "VerdictReferenceList",
  components: {VerdictReference},
  computed: {
    /**
     * Returns the current verdict
     */
    verdict() {
      return this.$store.getters.getCurrentVerdict
    },
    /**
     * Returns the verdictNode
     */
    verdictNode() {
      return this.$store.getters.getVerdictNode
    },
    /**
     * Returns a list of reasons
     */
    reasons() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].gruende && this.verdictNode.outgoingReferenceList[0].gruende.length > 0) {
        return this.verdictNode.outgoingReferenceList[0].gruende
      } else if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].entscheidungsgruende && this.verdictNode.outgoingReferenceList[0].entscheidungsgruende.length > 0) {
        return this.matchIndicesReasons(this.verdictNode.outgoingReferenceList[0].entscheidungsgruende)
      } else {
        return []
      }
    },
    /**
     * Returns a list of offenses
     */
    offense() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].tatbestand && this.verdictNode.outgoingReferenceList[0].tatbestand.length > 0) {
        return this.matchIndicesOffense(this.verdictNode.outgoingReferenceList[0].tatbestand)
      } else {
        return []
      }
    },
    /**
     * Returns the tenor
     */
    tenor() {
      if (this.verdictNode.outgoingReferenceList[0] && this.verdictNode.outgoingReferenceList[0].tenor && this.verdictNode.outgoingReferenceList[0].tenor.length > 0) {
        return [this.verdictNode.outgoingReferenceList[0].tenor]
      } else {
        return []
      }
    }
  },
  methods: {
    /**
     * Match the references to corresponding offense indices
     *
     * @param references list of references to match
     * @returns {*[]} list of grouped references that match
     */
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
    /**
     * Match the references to corresponding reasons indices
     *
     * @param references list of references to match
     * @returns {*[]} list of grouped references that match
     */
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