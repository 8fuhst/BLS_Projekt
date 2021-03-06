<template>
  <div class="ref-container" :style="'top: ' + height + 'px'">
    <b-tabs v-if="tabs" class="margin tabs-c">
      <b-tab v-for="(reference, idx) in references" :key="idx" :title="(idx + 1) + ''">
        <div class="reference" @mouseover="setHover(true)" @mouseleave="setHover(false)">
          <HoverMenu class="hover-menu-tabs" :copy="true" :copyTextId="section + reference.index + 'ref'" :link="hasLink[idx]" :linkFilenumber="reference.referenz" v-if="hover"/>
          <b-card-text class="mb-2" :id="section + reference.index + 'ref'" >{{ reference.referenz }}</b-card-text>

          <div v-if="keywords[idx] && keywords[idx].length > 0" class="mb-2">
            <h4>Keywords</h4>
            <KeyWordTags style="margin-left: -6px" :keyWords="keywords[idx]"/>
          </div>
        </div>
      </b-tab>
    </b-tabs>

    <div v-if="!tabs" class="reference margin" @mouseover="setHover(true)" @mouseleave="setHover(false)">
      <HoverMenu class="hover-menu" :copy="true" :copyTextId="section + references[0].index + 'ref'" :link="hasLink[0]" :linkFilenumber="references[0].referenz" v-if="hover"/>
      <b-card-text class="mb-2" :id="section + references[0].index + 'ref'" >{{ references[0].referenz }}</b-card-text>

      <div v-if="keywords[0] && keywords[0].length > 0" class="mb-2">
        <h4>Keywords</h4>
        <KeyWordTags style="margin-left: -6px" :keyWords="keywords[0]"/>
      </div>
    </div>

  </div>
</template>

<script>
import HoverMenu from "@/components/UtilityComponents/HoverMenu";
import KeyWordTags from "@/components/KeyWordTags";

/**
 * Component for the references in the VerdictReferenceList.
 *
 * @param section Describes the section where the reference was found
 * @param references Array of the references that were found for an entry of the longtext
 */
export default {
  name: "VerdictReference",
  components: {HoverMenu, KeyWordTags},
  props: {
    section: {
      type: String,
    },
    references: {
      type: Array,
    }
  },
  data() {
    return {
      hover: false,
      height: 0,
      index: 0,
      stopUpdating: false,
      keywords: [],
      hasLink: [],
    }
  },
  computed: {
    /**
     * Returns whether the references shall be tabulated.
     */
    tabs() {
      return this.references.length > 1
    }
  },
  methods: {
    /**
     * Sets the hover property according to the parameter hover
     *
     * @param hover boolean for whether hover is set or not. True if hover shall be set to true. Else false
     */
    setHover(hover) {
      this.hover = hover
    },
    /**
     * Sets height according to needed height
     */
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

      if (element) {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const rect = element.getBoundingClientRect()
        if (!this.stopUpdating) {
          this.height = rect.top + scrollTop - 47
        }
      }
    },
    /**
     * Gets first five keywords by reference
     */
    async getKeywords() {
      for (let i = 0; i < this.references.length; i++) {
        const verdict = await this.$store.dispatch('getVerdictByFilenumber', this.references[i].referenz)
        if (verdict && verdict.keywords && verdict.keywords.length > 0) {
          this.keywords.push(verdict.keywords.slice(0,5))
          this.hasLink.push(true)
        } else {
          this.keywords.push([])
          this.hasLink.push(false)
        }
      }
    },
  },
  mounted() {
    this.index = parseInt(this.references[0].index)
    this.getKeywords()
    window.addEventListener("resize", this.setHeight)
  },
  updated() {
    this.setHeight()
  }
}
</script>

<style scoped>
  .reference {
    position: relative;
    background-color: white;
    border-radius: 4px;
    padding: 15px 12px;
    z-index: 0;
  }

  .margin {
    margin: 0 10%
  }
  .reference:hover {
    background-color: rgb(187,187,187);
    z-index: 2;
  }

  .hover-menu {
    position: absolute;
    top: -8px;
    right: 15px;
  }

  .hover-menu-tabs {
    position: absolute;
    top: -8px;
    right: 15px;
  }

  .ref-container {
    width: 34.2%;
  }
</style>

<style>
  .tabs-c div ul li a:not(.active) {
    background-color: #d2d2d2;
    color: black;
  }

  .tabs-c div ul li a.active {
    color: rgb(162, 30, 41) !important;
  }
</style>