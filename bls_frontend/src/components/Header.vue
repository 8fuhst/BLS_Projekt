<template>
    <div class="margin">
      <b-navbar toggleable="lg" type="dark" variant="primary">
        <b-navbar-brand to="/">BLS-Tool</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item v-for="(route,index) in routes" :key="index" :active="currentRoute.name === route.name" :to="route.path">{{ route.name }}</b-nav-item>
          </b-navbar-nav>
        </b-collapse>

        <b-nav-form @submit.prevent="onSubmit" v-if="currentRoute.name !== 'Search'">
          <b-form-input size="sm" v-model="newQuery" class="mr-sm-2" placeholder="Search..."></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

      </b-navbar>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      currentRoute: this.$route,
      newQuery: '',
    }
  },
  computed: {
    routes() {
      return this.$router.getRoutes().filter( (route) => !route.meta.hidden)
    }
  },
  watch: {
    $route(to) {this.currentRoute = to}
  },
  methods: {
    onSubmit() {
      this.$store.dispatch('setQuery', this.newQuery)
      this.$router.push('suche')
    },
  },
}
</script>

<style scoped>
  .margin {
    margin-bottom: 54px;
  }
</style>