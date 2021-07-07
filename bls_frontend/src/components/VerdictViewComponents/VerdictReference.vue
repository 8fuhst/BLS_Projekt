<template>
  <div class="reference mb-4" @mouseover="setHover(true)" @mouseleave="setHover(false)" :style="'top: ' + height + 'px'">
    <HoverMenu class="hover-menu" :copy="true" :copyTextId="section + index + 'ref'" :link="true" :linkFilenumber="text" v-if="hover"/>
    <b-card-text class="mb-2" :id="section + index + 'ref'" >{{ text }}</b-card-text>

    <div v-if="keywords.length > 0" class="mb-2">
      <h4>Keywords</h4>
      <KeyWordTags style="margin-left: -6px" :keyWords="keywords"/>
    </div>
  </div>
</template>

<script>
import HoverMenu from "@/components/UtilityComponents/HoverMenu";
import KeyWordTags from "@/components/KeyWordTags";

export default {
  name: "VerdictReference",
  components: {HoverMenu, KeyWordTags},
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
  data() {
    return {
      hover: false,
      height: 0,
      index: 0,
      stopUpdating: false,
      keywords: [],
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
    },
    async getKeywords() {
      const verdict = await this.$store.dispatch('getVerdictByFilenumber', this.text)
      if (verdict && verdict.keywords) {
        this.keywords = verdict.keywords.slice(0,5)
      } else {
        this.keywords = []
      }
    },
  },
  mounted() {
    this.index = parseInt(this.indexInput)
  },
  updated() {
    this.setHeight()
    this.getKeywords()
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
</style>