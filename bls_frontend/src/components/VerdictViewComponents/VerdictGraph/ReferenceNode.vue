<template>
  <svg @mouseover="setHover()" class="node" :x="x" :y="y" :width="currentWidth" :height="currentHeight">
    <rect x="0" y="0" :width="width" :height="height" stroke="black" fill="white" stroke-width="1px" />
    <text x="50%" y="50%" text-anchor="middle" font-size="16" fill="black">{{ text }}</text>

    <svg @click="getNewVerdict" :id="'panel' + type + index" v-if="hover && keywords.length > 0" :x="0" :y="0" :width="currentWidth" :height="keywords.length > 0 ? 87 : height">
      <rect x="0" y="0" width="100%" height="100%" stroke="black" fill="white" stroke-width="1px" />
      <text x="12" y="24" font-size="16" fill="black">{{ text }}</text>
      <text v-if="keywords.length > 0" x="12" y="47" font-size="16" font-weight="bold" fill="black" >Keywords</text>
      <text v-if="keywords.length > 0" :id="'keywords' + type + index" x="16" y="70" font-size="16" fill="black">{{ keywords }}</text>
    </svg>

  </svg>
</template>

<script>
/**
 * Component to generate the reference graph
 *
 * @param text of incoming or outgoing reference
 * @param index to identify the reference
 * @param xOffset to determine the x-axis offset
 * @param yOffset to determine the y-axis offset
 * @param width of the rectangle for the node
 * @param height of the rectangle for the node
 * @param padding to adjust padding between nodes
 * @param type to identify the reference
 * @param whichHovers to determine which node is hovered
 *
 */
export default {
  name: "ReferenceNode",
  props: {
    text: String,
    index: Number,
    xOffset: Number,
    yOffset: {
      type: Number,
      default: 20,
    },
    width: {
      type: Number,
      default: 100,
    },
    height: {
      type: Number,
      default: 50,
    },
    padding: {
      type: Number,
      default: 10,
    },
    type: String,
    whichHovers: String,
  },
  data() {
    return {
      x: 0,
      y: 0,
      hover: false,
      keywords: '',
      currentWidth: 110,
      currentHeight: 50,
      keywordsFetched: false,
    }
  },
  methods: {
    /**
     * Emits a hover event on a node
     */
    setHover() {
      this.$emit('hoverEvent', this.type + this.index + '')
    },
    /**
     * Gets new referenced verdict
     */
    async getNewVerdict() {
      const newVerdict = await this.$store.dispatch('getVerdictByFilenumber', this.text)
      if (newVerdict) {
        await this.$router.push({name: 'Verdict', query: {docnr: newVerdict.documentnumber}})

        window.scroll({
          top: 0,
          left: 0,
        });
      }
    },
    /**
     * Gets first three keywords by reference
     */
    async getKeywords() {
      if (!this.keywordsFetched) {
        const verdict = await this.$store.dispatch('getVerdictByFilenumber', this.text)
        if (verdict && verdict.keywords) {
          this.keywords = verdict.keywords.slice(0,3).join(', ')
        } else {
          this.keywords = ''
        }
        this.keywordsFetched = true
      }
    },
    /**
     * Sets the current width according to needed width
     */
    resizeSVG() {
      const text = document.getElementById('keywords' + this.type + this.index);
      const bbox = text ? text.getBoundingClientRect() : undefined
      const newWidth = bbox ? Math.max((bbox.right - bbox.left + 28), 165) : 110

      this.currentWidth = newWidth
    },
    /**
     * Sets the properties for to current value
     */
    setProperties() {
      this.getKeywords()

      if (this.hover) {
        this.resizeSVG()
      }

      this.y = this.index * this.height + this.index * this.padding + this.yOffset

      if (this.type === '1') {
        this.x = this.xOffset
      } else if (this.type === '2') {
        this.x = this.xOffset - this.currentWidth / 2 + 55
      } else if (this.type === '3') {
        this.x = this.xOffset - this.currentWidth + 110
      }

      if (this.hover) {
        this.$emit('newCoordinates', this.x, this.y)
      }
    }
  },
  mounted() {
    this.setProperties()
  },
  updated() {
    this.setProperties()
  },
  watch: {
    xOffset() {
      this.setProperties()
    },
    yOffset() {
      this.setProperties()
    },
    whichHovers() {
      if (this.type + this.index + '' === this.whichHovers) {
        this.hover = true

        this.currentHeight = this.keywords.length > 0 ? 87 : 50
      } else {
        this.hover = false
        this.currentHeight = 50
        this.currentWidth = 110
      }
    }
  }
}
</script>

<style scoped>
  svg:hover {
    cursor: pointer;
  }
</style>