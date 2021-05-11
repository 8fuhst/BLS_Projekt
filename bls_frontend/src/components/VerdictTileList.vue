<template>
  <div v-for="verdict in verdicts" :key="verdict.id">
    <VerdictTile :verdict="verdict" />
  </div>
</template>

<script>
import VerdictTile from "@/components/VerdictTile";

export default {
  name: "VerdictTileList",
  props: {
    verdicts: Array,
  },
  components: {VerdictTile}
}
</script>

<style scoped>

</style>