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

/**
 * Search component.
 * Shows a list of verdicts for a given searchquery.
 * When there is no query it shows the newest verdicts.
 */
export default {
  name: "Search",
  components: {
    Searchbar,
    VerdictTileList
  },
  created() {
    window.document.title = this.$route.query.query ? this.$route.query.query + ' - Suche - BLS Tool' : 'Suche - BLS Tool'
  },
  /**
   * Dispatches new search query on mounted
   */
  mounted() {
    this.dispatchQuery(this.$route.query.query)
  },
  methods: {
    /**
     * Fetches the next page of verdicts
     */
    fetchNextPage() {
      this.$store.dispatch('setQuery', this.$route.query.query)
    },
    /**
     * Dispatches new search query
     */
    dispatchQuery(query) {
      if (query && query.length > 0) {
        this.$store.dispatch('setQuery', query)
      } else {
        this.$store.dispatch('getNewest')
      }
    }
  },
  watch: {
    /**
     * On route change resets the page and dispatches new query
     */
    $route() {
      this.$store.commit('setPage', 0)
      this.dispatchQuery(this.$route.query.query)
      window.document.title = this.$route.query.query ? this.$route.query.query + ' - Suche - BLS Tool' : 'Suche - BLS Tool'
    }
  }
}
</script>

<style scoped>
</style>