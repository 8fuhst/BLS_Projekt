<template>
  <div>
    <b-row align-v="stretch" class="justify-content-center" v-if="!fetching">
      <b-col class="mb-4" lg="4" md="10" sm="10" v-for="(verdict, index) in verdicts" :key="index">
        <VerdictTile :verdict="verdict" />
      </b-col>
    </b-row>

    <div class="text-center py-3">
      <b-spinner class="spinner"></b-spinner>
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
    },
    fetching() {
      return this.$store.getters.getFetching
    },
  },
  components: {VerdictTile}
}
</script>

<style scoped>
  .spinner {
    color: #A21E29;
    width: 50px;
    height: 50px;
  }
</style>