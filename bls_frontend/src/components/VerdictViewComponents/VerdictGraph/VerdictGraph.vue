<template>
  <svg :width="width" :height="height">
    <ReferenceNode v-for="(node, index) in references.incoming" :key="`in_${index}`" :text="node" :index="index" :xOffset="inComingOffsetX" :yOffset="inComingOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" />
    <ReferenceNode :text="references.self" :index="0" :xOffset="centerOffsetX" :yOffset="centerOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" />
    <ReferenceNode v-for="(node, index) in references.outgoing" :key="`out_${index}`" :text="node" :index="index" :xOffset="outGoingOffsetX" :yOffset="outGoingOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" />
  </svg>
</template>

<script>
import ReferenceNode from "@/components/VerdictViewComponents/VerdictGraph/ReferenceNode";
import * as d3 from 'd3';

export default {
  name: "VerdictGraph",
  components: {ReferenceNode},
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
      nodeWidth: 100,
      padding: 10,
    }
  },
  methods: {
    updateSize() {
      const {
        width
      } = this.$el.parentElement.getBoundingClientRect()
      this.width = width

      this.height = Math.max(this.references.incoming.length * (this.nodeHeight + this.padding) - this.padding,
          this.references.outgoing.length * (this.nodeHeight + this.padding) - this.padding,
          this.nodeHeight)

      this.inComingOffsetY = this.height * 0.5 - (this.references.incoming.length * (this.nodeHeight + this.padding) - this.padding) * 0.5

      this.outGoingOffsetX = this.width - this.nodeWidth
      this.outGoingOffsetY = this.height * 0.5 - (this.references.outgoing.length * (this.nodeHeight + this.padding) - this.padding) * 0.5
      this.centerOffsetX = this.width * 0.5 - this.nodeHeight
      this.centerOffsetY = this.height * 0.5 - this.nodeHeight * 0.5
    }
  },
  mounted() {
    window.addEventListener("resize", this.updateSize);
    this.updateSize()
  },
  computed: {
    references() {
      /*return {
        incoming: ['2 BvE 4/21', '458jhfgsd', '191msnd', 'dasda', 'asdja', 'sda', 'asd'],
        outgoing: ['ndvy.ask', 'aljsdjow9', '-9kakpkapfghfghdf00'],
        self: '79123hj'
      }*/
      const node = this.$store.getters.getVerdictNode
      const outgoing = node.outgoingReferenceSet
      const incoming = node.incomingReferenceSet
      const self = this.$store.getters.getCurrentVerdict.filenumber[0]
      return {
        outgoing: outgoing,
        incoming: incoming,
        self: self,
      }
    },
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