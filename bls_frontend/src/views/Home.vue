<template>
  <div class="home">
    <b-container class="center">
      <h3>Neue Urteile:</h3>
      <b-row>
        <VerdictTileList :verdicts="verdicts" />
      </b-row>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import VerdictTileList from "@/components/VerdictTileList";
import ApiService from "../services/ApiService.js";

const apiService = new ApiService()

export default {
  name: 'Home',
  components: {
    VerdictTileList
  },
  data() {
    return {
      verdicts: [],
    }
  },
  async created() {
    this.verdicts = await apiService.fetchVerdicts('')
  }
}
</script>

<style scoped>
.center {
  max-width: 480px;
}
</style>
