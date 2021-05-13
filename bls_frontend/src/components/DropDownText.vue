<template>
  <div class="dropdown">
    <!-- Wir wollen hier wahrscheinlich eher ne andere bootstrap component anstatt dieses dropdown !-->
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
      options: [],
      data: [],
    }
  },
  created() {
    this.data = this.items.slice(0)
    this.main = this.data[0]
    this.data.shift()
    this.options = this.data
  }
}
</script>

<style scoped>
  .dropdown {
    min-height: 54px;
    width: auto;
    margin-right: -4px;
  }

  button {
    background-color: white;
  }
</style>