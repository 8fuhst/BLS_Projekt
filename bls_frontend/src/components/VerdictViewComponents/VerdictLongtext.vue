<template>
  <div class="longtext">
    <div v-if="tenor">
      <verdictText id="tenor" :prefix="'Tenor'" :divider="true" />
      <verdictText :prefix="tenor"/>
    </div>
    <div v-if="verdict.modelledOffense.length > 0">
      <verdictText id="sachverhalt" :prefix="'Sachverhaltsdarstellung'" :divider="true" />
      <VerdictText v-for="reason in verdict.modelledOffense" v-bind:key="reason.id" :prefix="reason.prefix" :text="reason.text" />
    </div>
    <div v-if="verdict.modelledReasonsForDecision.length > 0">
      <verdictText id="bewertung" :prefix="'Rechtliche Bewertung'" :divider="true" />
      <VerdictText v-for="reason in verdict.modelledReasonsForDecision" v-bind:key="reason.id" :prefix="reason.prefix" :text="reason.text" />
    </div>
  </div>
</template>

<script>
import VerdictText from "@/components/VerdictViewComponents/VerdictText";
import {mapGetters} from 'vuex'

export default {
  name: "VerdictLongtext",
  components: {VerdictText},
  computed: {
    ...mapGetters(['getCurrentVerdict']),
    verdict() {
      return this.getCurrentVerdict
    },
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