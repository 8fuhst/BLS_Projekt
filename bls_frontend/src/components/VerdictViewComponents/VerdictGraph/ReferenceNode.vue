<template>
  <svg @mouseover="setHover" class="node" :x="xOffset" :y="index * height + index * padding + yOffset" :width="width" :height="height">
    <rect x="0" y="0" width="100%" height="100%" stroke="black" fill="white" stroke-width="1px" />
    <text x="50%" y="50%" text-anchor="middle" font-size="16" fill="black">{{ text }}</text>
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
    }
  },
  methods: {
    setHover() {
      this.$emit('typeEvent')
      this.$emit('hoverEvent', this.xOffset, this.index * this.height + this.index * this.padding + this.yOffset, this.text, this.index)
    }
  }
}
</script>

<style scoped>
</style>