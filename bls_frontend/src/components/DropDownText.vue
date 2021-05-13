<template>
  <div class="dropdown">
    <b-list-group v-b-toggle="id">
      <b-list-group-item class="background" block>
        {{ main }}
      </b-list-group-item>
      <b-collapse :id="id" accordion="my-accordion" role="tabpanel">
        <div :key="item.id" v-for="item in options">
          <b-list-group-item class="background">{{ item }}</b-list-group-item>
        </div>
      </b-collapse>
    </b-list-group>

  </div>
</template>

<script>
export default {
  name: "DropDownText",
  props: {
    items: Array,
    id: String,
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

  .background {
    background-color: white;
    z-index: 1;
  }
</style>