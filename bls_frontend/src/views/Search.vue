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
  created() {
    window.document.title = this.$route.query.query ? 'BLS Tool - Suche - ' + this.$route.query.query : 'BLS Tool - Suche'
  },
  mounted() {
    this.$store.dispatch('setQuery', this.$route.query.query)
  },
  methods: {
    fetchNextPage() {
      this.$store.dispatch('setQuery', this.$route.query.query)
    }
  },
  watch: {
    $route() {
      this.$store.commit('setPage', 0)
      this.$store.dispatch('setQuery', this.$route.query.query)
      window.document.title = 'BLS Tool - Suche - ' + this.$route.query.query
    }
  }
}
</script>

<style scoped>
</style>