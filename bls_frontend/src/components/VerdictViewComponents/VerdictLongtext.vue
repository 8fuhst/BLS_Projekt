<template>
  <div class="longtext">
    <div v-if="tenor">
      <verdictText id="tenor" :prefix="'Tenor'" :divider="true" />
      <verdictText :prefix="tenor" :section="'tenor'" :indices="[0]"/>
    </div>
    <div v-if="verdict.modelledOffense.length > 0">
      <verdictText id="sachverhalt" :prefix="'Sachverhaltsdarstellung'" :divider="true" />
      <VerdictText v-for="reason in verdict.modelledOffense" v-bind:key="reason.id" :prefix="reason.prefix" :text="reason.text" :indices="reason.indices" :section="'sachverhalt'" />
    </div>
    <div v-if="verdict.modelledReasonsForDecision.length > 0">
      <verdictText id="bewertung" :prefix="'Rechtliche Bewertung'" :divider="true" />
      <VerdictText v-for="reason in verdict.modelledReasonsForDecision" v-bind:key="reason.id" :prefix="reason.prefix" :text="reason.text" :indices="reason.indices" :section="'bewertung'" />
    </div>
  </div>
</template>

<script>
import VerdictText from "@/components/VerdictViewComponents/VerdictText";
import {mapGetters} from 'vuex'

/**
 * Component to build the detailed information on reasons and offenses of a verdict
 *
 */
export default {
  name: "VerdictLongtext",
  components: {VerdictText},
  computed: {
    ...mapGetters(['getCurrentVerdict']),
    /**
     * Returns the current verdict
     */
    verdict() {
      return this.getCurrentVerdict
    },
    /**
     * Returns the tenor of current verdict
     */
    tenor() {
      return this.verdict.tenor.join(' ')
    }
  },
}
</script>

<style scoped>
  .longtext {
    display: inline-block;
    width: 62%;
    position: relative;
  }
</style>