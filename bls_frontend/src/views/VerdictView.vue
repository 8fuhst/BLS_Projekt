<template>
  <div>
    <VerdictHero :verdict="verdict" />
    <div class="text-container">
      <VerdictLongtext :tenor="tenor" :offense="offense" :reasonsForDecision="reasonsForDecision" />
      <VerdictReferenceList />
    </div>
  </div>
</template>

<script>
import VerdictHero from "@/components/VerdictViewComponents/VerdictHero";
import VerdictLongtext from "@/components/VerdictViewComponents/VerdictLongtext";
import VerdictReferenceList from "@/components/VerdictViewComponents/VerdictReferenceList";
import {LongtextModel} from "@/models/longtext-model";

export default {
  name: "VerdictView",
  components: {
    VerdictHero,
    VerdictLongtext,
    VerdictReferenceList,
  },
  data() {
    return {
      tenor: '',
      offense: [],
      reasonsForDecision: [],
    }
  },
  computed: {
    verdict() {
      return this.$store.getters.getCurrentVerdict
    }
  },
  methods: {
    isSpaces(string) {
      return !string.replace(/\s/g, '').length
    }
  },
  mounted() {
    this.tenor = this.verdict.tenor.join(', ')

    let i = 0
    for (i = 0; i < this.verdict.reasonsForDecision.length; i++) {
      if (this.isSpaces(this.verdict.reasonsForDecision[i])) {
        continue
      }
      if (isNaN(this.verdict.reasonsForDecision[i])) {
        this.reasonsForDecision.push(new LongtextModel(this.verdict.reasonsForDecision[i]))
      } else {
        this.reasonsForDecision.push(new LongtextModel(this.verdict.reasonsForDecision[i], this.verdict.reasonsForDecision[i + 1]))
        i++
      }
    }

    for (i = 0; i < this.verdict.offense.length; i++) {
      if (this.isSpaces(this.verdict.offense[i])) {
        continue
      }
      if (isNaN(this.verdict.offense[i])) {
        this.offense.push(new LongtextModel(this.verdict.offense[i]))
      } else {
        this.offense.push(new LongtextModel(this.verdict.offense[i], this.verdict.offense[i + 1]))
        i++
      }
    }
  }
}
</script>

<style scoped>
  .text-container {
    display: flex;
    height: auto;
    width: 80%;
    margin: 0 10%;
  }
</style>