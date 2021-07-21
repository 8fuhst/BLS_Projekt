<template>
    <b-container fluid class="pt-4">
      <h3>Neue Urteile:</h3>
      <VerdictTileList @newPageEvent="fetchNextPage" />
    </b-container>
</template>

<script>
// @ is an alias to /src
import VerdictTileList from "@/components/VerdictTileComponents/VerdictTileList";

export default {
  name: 'Home',
  components: {
    VerdictTileList,
  },
  created() {
    window.document.title = 'BLS Tool - Home'
  },
  mounted() {
    this.$store.dispatch('getNewest')
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
