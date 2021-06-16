<template>
  <div class="scroll">
    <VerdictHero :verdict="verdict" />
    <div class="text-container">
      <VerdictLongtext />
      <VerdictReferenceList />
    </div>
  </div>
</template>

<script>
import VerdictHero from "@/components/VerdictViewComponents/VerdictHero";
import VerdictLongtext from "@/components/VerdictViewComponents/VerdictLongtext";
import VerdictReferenceList from "@/components/VerdictViewComponents/VerdictReferenceList";

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
  mounted() {
    window.scroll({
      top: 0,
      left: 0,
    });
    if (this.verdict.filenumber[0] !== undefined) {
      this.$store.dispatch('setVerdictNode', this.verdict.filenumber[0])
    }

  },
  watch: {
    verdict: function () {
      if (this.verdict.filenumber[0] !== undefined) {
        this.$store.dispatch('setVerdictNode', this.verdict.filenumber[0])
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

  .scroll {
    scroll-behavior: smooth;
  }
</style>