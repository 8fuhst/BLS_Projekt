<template>
  <div class="reference bottom-margin" @mouseover="setHover(true)" @mouseleave="setHover(false)" :style="'top: ' + height + 'px'">
    <HoverMenu class="hover-menu" :copy="true" :copyTextId="section + index + 'ref'" :link="true" :linkFilenumber="text" v-if="hover"/>
    <b-card-text :id="section + index + 'ref'" >{{ text }}</b-card-text>
  </div>
</template>

<script>
import HoverMenu from "@/components/UtilityComponents/HoverMenu";

export default {
  name: "VerdictReference",
  components: {HoverMenu},
  props: {
    section: {
      type: String,
    },
    indexInput: {
      type: String,
    },
    text: {
      type: String,
    }
  },
  computed: {
    change() {
      return this.$store.getters.getChange
    }
  },
  data() {
    return {
      hover: false,
      height: 0,
      index: 0,
      stopUpdating: false,
    }
  },
  methods: {
    setHover(hover) {
      this.hover = hover
    },
    setHeight() {
      let element
      element = document.getElementById(this.section + this.index)
      if (element === null) {
        const previous = this.index - 1
        element = document.getElementById(this.section + previous + 'x' + this.index)
      }
      if (element === null) {
        const next = this.index + 1
        element = document.getElementById(this.section + this.index + 'x' + next)
      }

      const heroHeight = document.getElementById('verdictHero').offsetHeight
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

      const rect = element.getBoundingClientRect()
      if (!this.stopUpdating) {
        this.height = rect.top - heroHeight + scrollTop
      }
    }
  },
  mounted() {
    this.index = parseInt(this.indexInput)
  },
  updated() {
    this.setHeight()
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