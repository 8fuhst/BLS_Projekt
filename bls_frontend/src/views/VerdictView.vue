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

/**
 * VerdictView component for single view of a verdict
 */
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
    /**
     * The verdict is the current active verdict form the store
     */
    verdict() {
      return this.$store.getters.getCurrentVerdict
    }
  },
  created() {
    this.$store.dispatch('setCurrent', this.$route.query.docnr)
    window.document.title = 'BLS Tool - Urteil - ' + this.verdict.filenumber[0]
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
    /**
     * On new verdict also get new verdictnode
     */
    verdict: function () {
      if (this.verdict.filenumber[0] !== undefined) {
        this.$store.dispatch('setVerdictNode', this.verdict.filenumber[0])
      }
    },
    /**
     * On route change dispatch for new verdict
     */
    $route() {
      this.$store.dispatch('setCurrent', this.$route.query.docnr)
    }
  }
}
</script>

<style scoped>
  .text-container {
    display: flex;
    height: auto;
    width: 90%;
    margin: 0 5%;
  }

  .scroll {
    scroll-behavior: smooth;
  }

  .scroll {
    scroll-behavior: smooth;
  }
</style>