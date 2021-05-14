<template>
  <div>
    <div v-for="verdict in verdicts" :key="verdict.documentnumber">
      <VerdictTile :verdict="verdict" />
    </div>
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