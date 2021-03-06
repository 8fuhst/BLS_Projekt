<template>
  <svg :width="width" :height="height">
    <text x="0" y="20" font-size="16" font-weight="bold" fill="black" v-if="references.incoming.length > 0">Eingehend</text>
    <text text-anchor="end" :x="width" y="20" font-size="16" font-weight="bold" fill="black" v-if="references.outgoing.length > 0">Ausgehend</text>

    <svg fill="white" fill-opacity="0" stroke="#000" stroke-width="1">
      <path v-for="(_, index) in references.incoming" :key="`in_p_${index}`" :d="lineGen(index, true)"/>
      <path v-for="(_, index) in references.outgoing" :key="`out_p_${index}`" :d="lineGen(index, false)"/>
    </svg>

    <ReferenceNode @hoverEvent="hoverEvent" @newCoordinates="newCoordinates" :whichHovers="hoverId" v-for="(node, index) in references.incoming" :key="`in_${index}`" :text="node" :index="index" :xOffset="inComingOffsetX" :yOffset="inComingOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" type="1"/>
    <ReferenceNode :text="references.self" :whichHovers="hoverId" :index="0" :xOffset="centerOffsetX" :yOffset="centerOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" type="2" />
    <ReferenceNode @hoverEvent="hoverEvent" @newCoordinates="newCoordinates" :whichHovers="hoverId" v-for="(node, index) in references.outgoing" :key="`out_${index}`" :text="node" :index="index" :xOffset="outGoingOffsetX" :yOffset="outGoingOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" type="3" />
    <use id="use" :x="hoverConfig.x" :y="hoverConfig.y" />
  </svg>
</template>

<script>
import ReferenceNode from "@/components/VerdictViewComponents/VerdictGraph/ReferenceNode";

/**
 * Component to create the reference graph
 *
 */
export default {
  name: "VerdictGraph",
  components: {ReferenceNode},
  data() {
    return {
      width: 200,
      height: 200,
      inComingOffsetX: 0,
      inComingOffsetY: 37,
      outGoingOffsetX: 100,
      outGoingOffsetY: 37,
      centerOffsetX: 50,
      centerOffsetY: 175,
      nodeHeight: 50,
      nodeWidth: 110,
      padding: 10,
      headingHeight: 32,
      extendedNodeHeight: 87,
      hoverConfig: {
        x: 0,
        y: 0,
      },
      currentType: 1,
      hoverId: '0'
    }
  },
  methods: {
    /**
     * Brings the hovered element on top (z-axis)
     */
    hoverEvent(hoverId) {
      this.hoverId = hoverId
      const topmost = document.getElementById('use')
      topmost.setAttributeNS('http://www.w3.org/1999/xlink',
          'xlink:href',
          '#panel' + hoverId);
    },
    /**
     * Sets x and y to new values
     */
    newCoordinates(x,y) {
      this.hoverConfig = {x, y}
    },
    /**
     * Updates size of graph according to contained elements
     */
    updateSize() {
      const {
        width
      } = this.$el.parentElement.getBoundingClientRect()
      this.width = width

      this.height = Math.max(this.references.incoming.length * (this.nodeHeight + this.padding) + this.headingHeight + this.extendedNodeExtraHeight,
          this.references.outgoing.length * (this.nodeHeight + this.padding) - this.padding + this.headingHeight + this.extendedNodeExtraHeight,
          this.nodeHeight)

      this.inComingOffsetY = (this.height - this.extendedNodeExtraHeight) * 0.5 + this.headingHeight * 0.5 - (this.references.incoming.length * (this.nodeHeight + this.padding) - this.padding) * 0.5

      this.outGoingOffsetX = this.width - this.nodeWidth
      this.outGoingOffsetY = (this.height - this.extendedNodeExtraHeight) * 0.5 + this.headingHeight * 0.5 - (this.references.outgoing.length * (this.nodeHeight + this.padding) - this.padding) * 0.5
      this.centerOffsetX = this.width * 0.5 - this.nodeWidth * 0.5
      this.centerOffsetY = (this.height - this.extendedNodeExtraHeight) * 0.5 + this.headingHeight * 0.5 - this.nodeHeight * 0.5
    },
    /**
     * Generates the edges
     */
    lineGen(index, isIncoming) {
      let startX = 0
      let startY = 0
      let mid1X = 0
      let mid1Y = 0
      let mid2X = 0
      let mid2Y = 0
      let endX = 0
      let endY = 0
      if (isIncoming) {
        startX = this.nodeWidth
        startY = index * (this.nodeHeight + this.padding) + 0.5 * this.nodeHeight + this.inComingOffsetY
        endX = this.width * 0.5 - this.nodeWidth * 0.5
        endY = (this.height - this.extendedNodeExtraHeight) * 0.5 + this.headingHeight * 0.5
      } else {
        startX = this.width - this.nodeWidth
        startY = index * (this.nodeHeight + this.padding) + 0.5 * this.nodeHeight + this.outGoingOffsetY
        endX = this.width * 0.5 + this.nodeWidth * 0.5
        endY = (this.height - this.extendedNodeExtraHeight) * 0.5 + this.headingHeight * 0.5
      }
      mid1X = startX + (endX - startX) / 2
      mid1Y = startY
      mid2X = startX + (endX - startX) / 2
      mid2Y = endY

      return 'M ' + startX + ' ' + startY + ' C ' + mid1X + ' ' + mid1Y + ', ' + mid2X + ' ' + mid2Y + ', ' + endX + ' ' + endY
    }
  },
  mounted() {
    window.addEventListener("resize", this.updateSize);
    this.updateSize()
    //const showGraph = this.references.outgoing > 0 || this.references.incoming > 0
    //this.$emit('showGraphEvent', showGraph)
  },
  updated() {
    this.updateSize()
  },
  computed: {
    references() {
      const node = this.$store.getters.getVerdictNode
      const outgoing = node.outgoingReferenceSet
      const incoming = node.incomingReferenceSet
      const self = this.$store.getters.getCurrentVerdict.filenumber[0]
      this.$emit('scrollHidden', Math.max(outgoing.length, incoming.length) <=5)
      this.$emit('showGraphEvent', outgoing.length > 0 || incoming.length > 0)
      return {
        outgoing: outgoing,
        incoming: incoming,
        self: self,
      }
    },
    extendedNodeExtraHeight() {
      return this.extendedNodeHeight - this.nodeHeight
    }
  }
}
</script>

<style scoped>
  use:hover {
    cursor: pointer;
  }
</style>