<template>
    <b-container fluid class="pt-4">
      <h3>Neue Urteile:</h3>
      <VerdictTileList />
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
  mounted() {
    this.$store.dispatch('getNewest')
  }
}
</script>

<style scoped>
</style>
