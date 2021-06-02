<template>
  <div>
    <div v-for="(verdict, index) in verdicts" :key="index">
      <VerdictTile :verdict="verdict" />
    </div>
  </div>
</template>

<script>
import VerdictTile from "@/components/VerdictTileComponents/VerdictTile";

export default {
  name: "VerdictTileList",
  computed: {
    verdicts() {
      return this.$store.getters.getVerdicts
    }
  },
  components: {VerdictTile}
}
</script>

<style scoped>

</style>