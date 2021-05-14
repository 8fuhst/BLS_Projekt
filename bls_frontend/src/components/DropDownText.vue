<template>
  <div class="dropdown-text">
    <b-list-group class="list-group" >
      <b-list-group-item class="list-item first-item" block>
        <b-card-text class="siblings text">
          {{ main }}
        </b-card-text>
        <img class="siblings icon" src="@/assets/list-icon.svg" v-b-toggle="id">
      </b-list-group-item>
      <b-collapse :id="id" accordion="my-accordion" role="tabpanel">
        <div :key="item.id" v-for="item in options">
          <b-list-group-item class="list-item">{{ item }}
            <b-card-text></b-card-text>
          </b-list-group-item>
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
  .dropdown-text {
    min-height: 54px;
    width: auto;
    margin-top: -15px;
  }

  .list-item {
    background-color: white;
    border: 1px solid transparent;
    border-top-color: black;
    border-bottom-left-radius: .25rem;
    border-bottom-right-radius: .25rem;

    min-height: 54px;
    width: auto;
    text-align: left;

    z-index: 1;
  }

  .first-item {
    border-top-color: transparent;
  }

  .list-group {
    border: 1px solid black;
    border-radius: .25rem;
    background-color: white;
  }

  .siblings {
    float:left;
    display:inline;
    width: auto;
  }

  .icon {
    float: right;
    width: 24px;
  }

  .text {
    cursor: auto;
    margin: 0;
    margin-right: 12px;
  }
</style>