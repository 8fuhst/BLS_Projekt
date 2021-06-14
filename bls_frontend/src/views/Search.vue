<template>
  <div class="pt-4">
    <Searchbar />
    <b-container fluid>
      <VerdictTileList @newPageEvent="fetchNextPage" />
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
  },
  methods: {
    fetchNextPage() {
      this.$store.dispatch('getNewest')
    }
  }
}
</script>

<style scoped>
</style>