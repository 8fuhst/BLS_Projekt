<template>
  <div class="verdict-text" @mouseover="setHover(true)" @mouseleave="setHover(false)">
    <HoverMenu class="hover-menu" :copy="true" :copyTextId="'hi'" v-if="hover"/>
    <h5>{{ prefix }}</h5>
    <b-card-text id="hi" class="text-padding">{{ text }}</b-card-text>
  </div>
</template>

<script>
import HoverMenu from "@/components/UtilityComponents/HoverMenu";
export default {
  name: "VerdictText",
  components: {HoverMenu},
  props: {
    prefix: String,
    text: String,
  },
  data() {
    return {
      hover: false,
    }
  },
  methods: {
    setHover(hover) {
      this.hover = hover
    }
  }
}
</script>

<style scoped>
  .verdict-text {
    padding: 14px 30px;
    position: relative;
  }

  .verdict-text:hover {
    background-color: rgb(187,187,187);
  }

  .text-padding {
    padding: 0px 12px;
  }

  .hover-menu {
    position: absolute;
    top: -8px;
    right: 15px;
  }
</style>