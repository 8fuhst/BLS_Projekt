<template>
  <div>
    <b-row align-v="stretch" class="justify-content-center" v-if="!fetching">
      <b-col class="mb-4" lg="4" md="10" sm="10" v-for="(verdict, index) in verdicts" :key="index">
        <VerdictTile :verdict="verdict" />
      </b-col>
    </b-row>

    <div class="text-center py-3" id="spinner" >
      <b-spinner class="spinner"></b-spinner>
    </div>
  </div>

</template>

<script>
import VerdictTile from "@/components/VerdictTileComponents/VerdictTile";

export default {
  name: "VerdictTileList",
  created () {
    window.addEventListener('scroll', this.onScroll);
  },destroyed () {
    window.removeEventListener('scroll', this.onScroll);
  },
  data () {
    return {
      offsetTop: 0
    }
  },
  watch: {
    offsetTop() {
      if (this.isElementInViewport(document.getElementById('spinner'))) {
        this.getNextPage()
      }
    }
  },
  methods: {
    onScroll() {
      this.offsetTop = window.pageYOffset || document.documentElement.scrollTop
    },
    isElementInViewport(el) {
      const rect = el.getBoundingClientRect();
      return (
          rect.top >= 0 &&
          rect.left >= 0 &&
          rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
          rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
    },
    getNextPage() {
      const currentPage = this.$store.getters.getPage
      const nextPage = currentPage + 1
      this.$store.commit('setPage', nextPage)
      this.$emit('newPageEvent')
    }
  },
  computed: {
    verdicts() {
      return this.$store.getters.getVerdicts
    },
    firstPage() {
      return this.$store.getters.getPage === 0
    },
    fetching() {
      return this.$store.getters.getFetching && this.firstPage
    },
  },
  components: {VerdictTile},
  mounted() {
    this.$store.commit('setPage', 0)
  }
}
</script>

<style scoped>
  .spinner {
    color: #A21E29;
    width: 50px;
    height: 50px;
  }
</style>