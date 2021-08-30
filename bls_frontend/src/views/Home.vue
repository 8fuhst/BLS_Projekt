<template>
    <b-container fluid class="pt-4">
      <h3>Neue Urteile:</h3>
      <VerdictTileList @newPageEvent="fetchNextPage" />
    </b-container>
</template>

<script>
import VerdictTileList from "@/components/VerdictTileComponents/VerdictTileList";

/**
 * Home Component.
 * Shows when you start up the App.
 * Shows a list of new Verdicts.
 */
export default {
  name: 'Home',
  components: {
    VerdictTileList,
  },
  created() {
    window.document.title = 'Home - BLS Tool'
  },
  mounted() {
    this.$store.dispatch('getNewest')
  },
  methods: {
    /**
     * Fetches the next page of verdicts in the list.
     */
    fetchNextPage() {
      this.$store.dispatch('getNewest')
    }
  }
}
</script>

<style scoped>
</style>
