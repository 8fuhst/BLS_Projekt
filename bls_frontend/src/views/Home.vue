<template>
  <div>
    <b-container class="center">
      <h3>Neue Urteile:</h3>
      <b-row>
        <VerdictTileList />
      </b-row>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import VerdictTileList from "@/components/VerdictTileList";

export default {
  name: 'Home',
  components: {
    VerdictTileList,
  },
  mounted() {
    this.$store.dispatch('setQuery', '')
  }
}
</script>

<style scoped>
.center {
  max-width: 480px;
}
</style>
