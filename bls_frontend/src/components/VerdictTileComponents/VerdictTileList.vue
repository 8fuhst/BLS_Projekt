<template>
  <b-row align-v="stretch" class="justify-content-center">
    <b-col class="mb-4" lg="4" md="10" sm="10" v-for="(verdict, index) in verdicts" :key="index">
      <VerdictTile :verdict="verdict" />
    </b-col>
  </b-row>
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