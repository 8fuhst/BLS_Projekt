<template>
  <svg :width="width" :height="height" @click="removeHover">
    <text x="0" y="20" font-size="16" font-weight="bold" fill="black" v-if="references.incoming.length > 0">Eingehend</text>
    <text text-anchor="end" :x="width" y="20" font-size="16" font-weight="bold" fill="black" v-if="references.outgoing.length > 0">Ausgehend</text>

    <svg fill="white" fill-opacity="0" stroke="#000" stroke-width="1">
      <path v-for="(_, index) in references.incoming" :key="`in_p_${index}`" :d="lineGen(index, true)"/>
      <path v-for="(_, index) in references.outgoing" :key="`out_p_${index}`" :d="lineGen(index, false)"/>
    </svg>

    <ReferenceNode @typeEvent="setType(1)" @hoverEvent="hoverEvent" v-for="(node, index) in references.incoming" :key="`in_${index}`" :text="node" :index="index" :xOffset="inComingOffsetX" :yOffset="inComingOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" />
    <ReferenceNode :text="references.self" :index="0" :xOffset="centerOffsetX" :yOffset="centerOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" />
    <ReferenceNode @typeEvent="setType(3)" @hoverEvent="hoverEvent" v-for="(node, index) in references.outgoing" :key="`out_${index}`" :text="node" :index="index" :xOffset="outGoingOffsetX" :yOffset="outGoingOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" />

    <ExtendedNode @removeHover="removeHover" v-bind:config="hoverNodeConfig" :width="nodeWidth * 2" :height="87" />
  </svg>
</template>

<script>
import ReferenceNode from "@/components/VerdictViewComponents/VerdictGraph/ReferenceNode";
import ExtendedNode from "@/components/VerdictViewComponents/VerdictGraph/ExtendedNode";

export default {
  name: "VerdictGraph",
  components: {ReferenceNode, ExtendedNode},
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
      nodeHeight: 50,
      nodeWidth: 110,
      padding: 10,
      headingHeight: 32,
      extendedNodeHeight: 87,
      hoverNodeConfig: {
        x: 0,
        y: 0,
        text: '',
        show: false,
        type: 3,
        isLast: false
      },
      currentType: 1,
    }
  },
  methods: {
    setType(type) {
      this.currentType = type
    },
    hoverEvent(x, y, text, index) {
      let isLast = false
      if (this.currentType === 1) {
        isLast = index === this.references.incoming.length - 1 && index !== 0
      } else if (this.currentType === 3) {
        isLast = index === this.references.outgoing.length - 1 && index !== 0
      }
      this.hoverNodeConfig = {
        x,
        y,
        text,
        show: true,
        type: this.currentType,
        isLast
      }
    },
    removeHover() {
      this.hoverNodeConfig = {
        ...this.hoverNodeConfig,
        show: false,
      }
    },
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
  },
  updated() {
    this.updateSize()
  },
  computed: {
    references() {
      return {
        incoming: ['VI ZR 498/19', 'dd', 'dliua', 'asdjha'],
        outgoing: ['asd', 'asdkhasdik', 'asdkjh'],
        self: '79123hj'
      }
      /*
      const node = this.$store.getters.getVerdictNode
      const outgoing = node.outgoingReferenceSet
      const incoming = node.incomingReferenceSet
      const self = this.$store.getters.getCurrentVerdict.filenumber[0]
      return {
        outgoing: outgoing,
        incoming: incoming,
        self: self,
      }

       */
    },
    extendedNodeExtraHeight() {
      return this.extendedNodeHeight - this.nodeHeight
    }
  }
}
</script>

<style scoped>
</style>