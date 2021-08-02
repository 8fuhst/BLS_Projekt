<template>
  <div class="margin">
    <b-container fluid>
      <b-row class="justify-content-center" align-v="stretch">
        <b-col xxl="4" xl="5" lg="6" md="8" sm="10">
          <b-form @submit.prevent="onSubmit" class="d-flex" inline>
            <b-form-input class="searchbar mr-sm-3" v-model="newQuery" :placeholder="'Search...'"></b-form-input>
            <b-button class="my-2 my-sm-0 btn" type="submit">
              <b-card-text class="text">
                {{ 'Search ' }}
              </b-card-text>
              <div class="icon-container">
                <b-icon-search class="icon" />
              </div>
            </b-button>
          </b-form>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

/**
 * Component for the searchbar on the search page
 */
export default {
  name: "Searchbar",
  data() {
    return {
      newQuery: '',
    }
  },
  created() {
    this.newQuery = this.$route.query.query
  },
  methods: {
    /**
     * Submits a new query
     */
    onSubmit() {
      this.$router.push({ name: 'Search', query: { query: this.newQuery } })
    }
  }
}
</script>

<style scoped>
  .margin {
    margin-bottom: 24px;
  }

  .searchbar {
    height: 54px;
    padding: 14px 12px;
    flex-grow: 1;
  }

  .btn {
    float: right;
    height: 54px;
    padding: 14px 12px;
  }

  .text {
    display: inline;
    margin-right: 4px;
  }

  .icon-container {
    float: right;
    height: 24px;
    width: 24px;
  }

  .icon {
    float:left;
    display:inline;
    width: auto;
    position: relative;
    top: 2px;
    width: 24px;
  }

  .icon:focus {
    outline: 0;
  }

</style>