<template>
  <div class="margin">
    <Searchbar />
    <b-container class="center">
      <h3>Ergebnisse:</h3>
      <b-row>
        <VerdictTileList />
      </b-row>
    </b-container>
  </div>
</template>

<script>
import VerdictTileList from "@/components/VerdictTileComponents/VerdictTileList";
import Searchbar from "@/components/Searchbar";

export default {
  name: "Search",
  components: {
    Searchbar,
    VerdictTileList
  },
  computed: {
    query() {
      return this.$store.getters.getQuery
    }
  },
  mounted() {
    this.$store.dispatch('setQuery', this.query)
  }
}
</script>

<style scoped>
  .center {
    max-width: 480px;
  }

  .margin {
    margin-top: 27px;
  }
</style>