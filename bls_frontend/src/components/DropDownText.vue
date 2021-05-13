<template>
  <div>
    <b-dropdown :text="main">
      <div :key="item.id" v-for="item in options">
        <b-dropdown-item>{{ item }}</b-dropdown-item>
      </div>
    </b-dropdown>
  </div>
</template>

<script>
export default {
  name: "DropDownText",
  props: {
    items: Array,
  },
  data() {
    return {
      main: '',
      options: []
    }
  },
  created() {
    this.main = this.items[0]
    this.items.shift()
    this.options = this.items
  }
}
</script>

<style scoped>
  .btn-secondary.focus, .btn-secondary:focus {
    color: #fff;
    background-color: #ffffff;
    border-color: #6c757d;
  }
</style>