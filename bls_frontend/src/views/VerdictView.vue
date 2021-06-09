<template>
  <div :class="colorClass + '-anzeige'" class="scroll">
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
import {ColorService} from "@/services/ColorService";

const colorService = new ColorService()

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
      colorClass: '',
    }
  },
  computed: {
    verdict() {
      return this.$store.getters.getCurrentVerdict
    }
  },
  mounted() {
    this.colorClass = colorService.colorClass(this.verdict.documenttype)
  },
  created() {
    window.scroll({
      top: 0,
      left: 0,
    });
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