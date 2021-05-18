<template>
  <div>
    <Header @searchQuery="onSearchQuery" />
    <router-view @searchQuery="onSearchQuery" :query="this.query" />
  </div>
</template>

<script>
import Header from "@/components/Header";
export default {
  components: {Header},
  data() {
    return {
      query: '',
    }
  },
  methods: {
    onSearchQuery(query) {
      this.$router.push('suche')
      this.query = query
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
