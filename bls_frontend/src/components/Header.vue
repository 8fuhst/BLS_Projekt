<template>
  <div class="sticky-top">
    <b-navbar toggleable="lg" type="dark" class="color">
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

    <div id="back-to-top" @click="topFunction">
      <b-icon-chevron-down class="back-to-top-icon" :rotate="180" />
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      currentRoute: this.$route,
      newQuery: '',
      mybutton: null,
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
    scrollFunction() {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        this.mybutton.style.display = "block";
      } else {
        this.mybutton.style.display = "none";
      }
    },
    topFunction() {
      window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth'
      });
    }
  },
  mounted() {
    this.mybutton = document.getElementById("back-to-top");
    window.onscroll = () => this.scrollFunction()
  }
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

  #back-to-top {
    display: none;
    position: fixed;
    bottom: 20px;
    right: 30px;
    z-index: 99;
    background-color: #FFFFFF;
    cursor: pointer;
    padding: 15px 16.5px;
    border-radius: 100000px;
    font-size: 18px;
    box-shadow: 2px 2px 3px #6c6c6c;
  }

  #back-to-top svg {
    color: rgb(162, 30, 41);;
  }

  .back-to-top-icon {
    font-size: 26px;
  }
</style>