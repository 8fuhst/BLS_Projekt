<template>
  <svg @mouseover="setHover()" class="node" :x="x" :y="index * height + index * padding + yOffset" :width="currentWidth" :height="currentHeight">
    <rect x="0" y="0" :width="width" :height="height" stroke="black" fill="white" stroke-width="1px" />
    <text x="50%" y="50%" text-anchor="middle" font-size="16" fill="black">{{ text }}</text>

    <svg @click="getNewVerdict" :id="'panel' + type + index" v-if="hover" :x="0" :y="0" :width="currentWidth" :height="87">
      <rect x="0" y="0" width="100%" height="100%" stroke="black" fill="white" stroke-width="1px" />
      <text x="12" y="24" font-size="16" fill="black">{{ text }}</text>
      <text v-if="keywords.length > 0" x="12" y="47" font-size="16" font-weight="bold" fill="black" >Keywords</text>
      <text v-if="keywords.length > 0" :id="'keywords' + type + index" x="16" y="70" font-size="16" fill="black">{{ keywords }}</text>
    </svg>
    <use :id="'use' + type + index" :xlink:href="'panel' + type + index" />
  </svg>
</template>

<script>
export default {
  name: "ReferenceNode",
  props: {
    text: String,
    index: Number,
    xOffset: Number,
    yOffset: {
      type: Number,
      default: 0
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
    }
  },
  methods: {
    setHover() {
      this.$emit('hoverEvent', this.type + this.index + '')
    },
    async getNewVerdict() {
      const newVerdict = await this.$store.dispatch('getVerdictByFilenumber', this.text)
      if (newVerdict) {
        await this.$router.push({name: 'Verdict', query: {docnr: newVerdict.documentnumber}})

        window.scroll({
          top: 0,
          left: 0,
        });

        this.$emit('removeHover')
      }
    },
    async getKeywords() {
      const verdict = await this.$store.dispatch('getVerdictByFilenumber', this.text)
      if (verdict && verdict.keywords) {
        this.keywords = verdict.keywords.slice(0,3).join(', ')
      } else {
        this.keywords = ''
      }
    },
    resizeSVG() {
      const svg = document.getElementById('panel' + this.type + this.index);
      const text = document.getElementById('keywords' + this.type + this.index);

      const bbox = text ? text.getBoundingClientRect() : svg.getBoundingClientRect()
      const newWidth = text ? Math.max((bbox.right - bbox.left + 28), 165) : 110

      svg.setAttribute("width", newWidth + '');
      this.currentWidth = newWidth
    },
    setProperties() {
      this.getKeywords()

      if (this.hover) {
        this.resizeSVG()
      }

      if (this.type === '1') {
        this.x = this.xOffset
      } else if (this.type === '2') {
        this.x = this.xOffset - this.currentWidth / 2 + 55
      } else if (this.type === '3') {
        this.x = this.xOffset - this.currentWidth + 110
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
    whichHovers() {
      if (this.type + this.index + '' === this.whichHovers) {
        this.hover = true

        this.currentHeight = 87

        const topmost = document.getElementById('use' + this.type + this.index)
        topmost.setAttributeNS('http://www.w3.org/1999/xlink',
            'xlink:href',
            'panel' + this.type + this.index);
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