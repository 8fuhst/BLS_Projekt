<template>
  <div>
    <Searchbar />
    <b-container class="center" v-if="verdicts.length !== 0">
      <h3>Ergebnisse:</h3>
      <b-row>
        <VerdictTileList :verdicts="verdicts" />
      </b-row>
    </b-container>
  </div>
</template>

<script>
import VerdictTileList from "@/components/VerdictTileList";
import Searchbar from "@/components/Searchbar";

export default {
  name: "Search",
  components: {
    Searchbar,
    VerdictTileList
  },
  computed: {
    verdicts() {
      return this.$store.getters.getVerdicts
    }
  },
}
</script>

<style scoped>
  .center {
    max-width: 480px;
  }
</style>