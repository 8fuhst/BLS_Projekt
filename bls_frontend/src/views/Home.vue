<template>
  <div class="margin">
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
  .center {
    max-width: 480px;
  }

  .margin {
    margin-top: 27px;
  }
</style>
