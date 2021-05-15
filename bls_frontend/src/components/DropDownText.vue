<template>
  <div class="dropdown-text" v-click-outside="hide">
    <b-list-group class="list-group" >
      <b-list-group-item class="list-item first-item" block>
        <b-card-text class="siblings text">
          {{ main }}
        </b-card-text>
        <img class="siblings icon" src="@/assets/list-icon.png" v-b-toggle="id">
      </b-list-group-item>
      <b-collapse :id="id" role="tabpanel" v-model="visible">
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
import ClickOutside from 'vue-click-outside'

export default {
  name: "DropDownText",
  props: {
    items: Array,
    id: String,
  },
  methods: {
    hide() {
      this.visible = false
    }
  },
  data() {
    return {
      main: '',
      options: [],
      data: [],
      visible: false,
    }
  },
  created() {
    this.data = this.items.slice(0)
    this.main = this.data[0]
    this.data.shift()
    this.options = this.data
  },
  directives: {
    ClickOutside
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
    border-top-color: rgba(0, 0, 0, .1);
    border-bottom-left-radius: .25rem;
    border-bottom-right-radius: .25rem;

    min-height: 52px;
    width: auto;
    text-align: left;

    padding: 13px 12px;

    z-index: 1;
  }

  .first-item {
    border-top-color: transparent;
  }

  .list-group {
    border: 1px solid rgba(0, 0, 0, .3);
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
    margin: 0 12px 0 0;
  }
</style>