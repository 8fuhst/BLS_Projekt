<template>
  <div class="dropdown-text" v-click-outside="hide">
    <b-list-group class="list-group" >
      <b-list-group-item class="list-item first-item" block>
        <b-card-text class="siblings text">
          {{ main }}
        </b-card-text>
        <div class="icon-container">
          <b-icon-list-ul class="siblings icon" v-b-toggle="id" />
        </div>
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

  .icon-container {
    float: right;
    height: 24px;
    width: 24px;
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
    position: relative;
    top: 4px;
    width: 24px;
  }

  .icon:focus {
    outline: 0;
  }

  .text {
    cursor: auto;
    margin: 0 12px 0 0;
  }
</style>