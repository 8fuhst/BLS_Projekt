<template>
  <svg :width="width" :height="height">
    <ReferenceNode v-for="(node, index) in data.incoming" :key="`in_${index}`" :text="node" :index="index" :xOffset="inComingOffsetX" :yOffset="inComingOffsetY" />
    <ReferenceNode :text="data.self" :index="0" :xOffset="centerOffsetX" :yOffset="centerOffsetY" />
    <ReferenceNode v-for="(node, index) in data.outgoing" :key="`out_${index}`" :text="node" :index="index" :xOffset="outGoingOffsetX" :yOffset="outGoingOffsetY"/>
  </svg>
</template>

<script>
import ReferenceNode from "@/components/VerdictViewComponents/VerdictGraph/ReferenceNode";
import * as d3 from 'd3';

export default {
  name: "VerdictGraph",
  components: {ReferenceNode},
  props: {
    data: {
      type: Object
    }
  },
  data() {
    return {
      width: 200,
      height: 200,
      inComingOffsetX: 0,
      inComingOffsetY: 0,
      outGoingOffsetX: 100,
      outGoingOffsetY: 0,
      centerOffsetX: 50,
      centerOffsetY: 175,
    }
  },
  methods: {
    updateSize() {
      const {
        width
      } = this.$el.parentElement.getBoundingClientRect()
      this.width = width

      this.height = Math.max(this.data.incoming.length * 50 * 1.2 - 0.2 * 50, this.data.outgoing.length * 50 * 1.2 - 0.2 * 50, 50)

      this.inComingOffsetY = this.height * 0.5 - (this.data.incoming.length * 50 * 1.2 - 0.2 * 50) * 0.5

      this.outGoingOffsetX = this.width - 104
      this.outGoingOffsetY = this.height * 0.5 - (this.data.outgoing.length * 50 * 1.2 - 0.2 * 50) * 0.5
      this.centerOffsetX = this.width * 0.5 - 50
      this.centerOffsetY = this.height * 0.5 - 25
    }
  },
  mounted() {
    this.updateSize()
  },
  computed: {
    lineGen() {
      return d3.line()
          .x(node => node.x)
          .y(node => node.y)
    }
  }
}
</script>

<style scoped>
</style>