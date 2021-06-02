<template>
  <div>
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
  computed: {
    verdict() {
      return this.$store.getters.getCurrentVerdict
    }
  },
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