<template>
  <div class="margin">
    <b-form @submit.prevent="onSubmit" inline class="mx-auto form">
      <b-form-input class="searchbar" v-model="queryReal" placeholder="Search..."></b-form-input>
      <b-button class="my-2 my-sm-0 btn" type="submit">
        <b-card-text class="text">
          {{ 'Search ' }}
        </b-card-text>
        <div class="icon-container">
          <b-icon-search class="icon" v-b-toggle="id" />
        </div>
      </b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "Searchbar",
  props: {
    query: String,
  },
  data() {
    return {
      queryReal: ''
    }
  },
  created() {
    this.queryReal = this.query
  },
  methods: {
    onSubmit() {
      this.$emit('searchQuery', this.queryReal)
    }
  }
}
</script>

<style scoped>
  .margin {
    margin-bottom: 54px;
  }

  .form {
    display: block;
    width: 600px;
  }

  .searchbar {
    height: 54px;
    padding: 14px 12px;
    width: 480px;
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