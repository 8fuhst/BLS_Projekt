<template>
  <div class="reference bottom-margin" @mouseover="setHover(true)" @mouseleave="setHover(false)">
    <HoverMenu class="hover-menu" :copy="true" :copyTextId="'hi'" v-if="hover"/>
    <b-card-text>{{ 'dkfjhshf fkasdf jhs' }}</b-card-text>
  </div>
</template>

<script>
import HoverMenu from "@/components/UtilityComponents/HoverMenu";

export default {
  name: "VerdictReference",
  components: {HoverMenu},
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
  .reference {
    margin: 0 10%;
    background-color: white;
    border-radius: 4px;
    position: relative;
    padding: 15px 12px
  }

  .reference:hover {
    background-color: rgb(187,187,187);
  }

  .hover-menu {
    position: absolute;
    top: -8px;
    right: 15px;
  }

  .bottom-margin {
    margin-bottom: 15px;
  }
</style>