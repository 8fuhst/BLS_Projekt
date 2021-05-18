<template>
  <div>
    <Searchbar @searchQuery="onSearchQuery" :query="query" />
    <b-container class="center">
      <h3>Ergebnisse:</h3>
      <b-row>
        <VerdictTileList :verdicts="verdicts" />
      </b-row>
    </b-container>
  </div>
</template>

<script>
import VerdictTileList from "@/components/VerdictTileList";
import ApiService from "../services/ApiService.js";
import Searchbar from "@/components/Searchbar";

const apiService = new ApiService()

export default {
  name: "Search",
  components: {
    Searchbar,
    VerdictTileList
  },
  props: {
    query: String,
  },
  data() {
    return {
      verdicts: []
    }
  },
  async created() {
    this.verdicts = await apiService.fetchVerdicts(this.query)
  },
  methods: {
    async onSearchQuery(query) {
      this.verdicts = await apiService.fetchVerdicts(query)
    }
  }
}
</script>

<style scoped>
  .center {
    max-width: 480px;
  }
</style>