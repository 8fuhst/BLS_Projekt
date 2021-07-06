<template>
  <svg @click="getNewVerdict" id="panel" v-if="config.show" :x="x" :y="y" :width="width" :height="height">
    <rect x="0" y="0" width="100%" height="100%" stroke="black" fill="white" stroke-width="1px" />
    <text x="12" y="24" font-size="16" fill="black">{{ config.text }}</text>
    <text v-if="keywords.length > 0" x="12" y="47" font-size="16" font-weight="bold" fill="black" >Keywords</text>
    <text v-if="keywords.length > 0" id="keywords" x="16" y="70" font-size="16" fill="black">{{ keywords }}</text>
  </svg>
</template>

<script>
export default {
  name: "ExtendedNode",
  props: {
    config: Object,
    width: Number,
    height: Number,
  },
  data() {
    return {
      x: 0,
      y: 0,
      keywords: '',
      currentWidth: 0,
    }
  },
  methods: {
    async getNewVerdict() {
      const newVerdict = await this.$store.dispatch('getVerdictByFilenumber', this.config.text)
      await this.$router.push({name: 'Verdict', query: {docnr: newVerdict.documentnumber}})

      window.scroll({
        top: 0,
        left: 0,
      });

      this.$emit('removeHover')
    },
    async getKeywords() {
      const verdict = await this.$store.dispatch('getVerdictByFilenumber', this.config.text)
      if (verdict && verdict.keywords) {
        this.keywords = verdict.keywords.slice(0,3).join(', ')
      } else {
        this.keywords = ''
      }
    },
    resizeSVG() {
      const svg = document.getElementById("panel");
      const text = document.getElementById("keywords");

      const bbox = text ? text.getBoundingClientRect() : svg.getBoundingClientRect()
      const newWidth = text ? Math.max((bbox.right - bbox.left + 28), 165) : this.width

      svg.setAttribute("width", newWidth + '');
      this.currentWidth = newWidth
    },
    setProperties() {
      if (this.config.isLast) {
        this.y = this.config.y - 37
      } else {
        this.y = this.config.y
      }

      if (this.config.type === 1) {
        this.x = this.config.x
      } else if (this.config.type === 2) {
        this.x = this.config.x - this.currentWidth / 2 + 55
      } else if (this.config.type === 3) {
        this.x = this.config.x - this.currentWidth + 110
      }

      this.getKeywords()

      if (this.config.show) {
        this.resizeSVG()
      }
    }
  },
  mounted() {
    this.setProperties()
  },
  updated() {
    this.setProperties()
  }
}
</script>

<style scoped>
  svg:hover {
    cursor: pointer;
  }
</style>