<template>
    <div>
      <b-navbar toggleable="lg" type="dark" class="color">
        <!-- TODO: Logo größe anpassen !-->
        <b-navbar-brand to="/"><img class="logo" src="@/assets/buc-white.svg" /></b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item v-for="(route,index) in routes" :key="index" :active="currentRoute.name === route.name" :to="route.path">{{ route.name }}</b-nav-item>
          </b-navbar-nav>
        </b-collapse>

        <b-nav-form class="d-none d-lg-block w-50 ml-auto" @submit.prevent="onSubmit" v-if="currentRoute.name !== 'Search'">
          <b-form-input size="sm" v-model="newQuery" class="mr-sm-2 w-75 ml-auto" placeholder="Search..."></b-form-input>
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
      this.$store.commit('setQuery', this.newQuery)
      this.$router.push('suche')
    },
  },
}
</script>

<style scoped>
  .color {
    background-color: rgb(162, 30, 41);
  }

  .logo {
    height: 40px;
    width: 140px;
  }
</style>