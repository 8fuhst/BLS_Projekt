<template>
  <svg :width="width" :height="height">
    <ReferenceNode v-for="(node, index) in references.incoming" :key="`in_${index}`" :text="node" :index="index" :xOffset="inComingOffsetX" :yOffset="inComingOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" />
    <ReferenceNode :text="references.self" :index="0" :xOffset="centerOffsetX" :yOffset="centerOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" />
    <ReferenceNode v-for="(node, index) in references.outgoing" :key="`out_${index}`" :text="node" :index="index" :xOffset="outGoingOffsetX" :yOffset="outGoingOffsetY" :width="nodeWidth" :height="nodeHeight" :padding="padding" />
    <path v-for="(_, index) in references.incoming" :key="`in_p_${index}`" :d="lineGen(index, true)" stroke="black" />
    <path v-for="(_, index) in references.outgoing" :key="`out_p_${index}`" :d="lineGen(index, false)" stroke="black" />
  </svg>
</template>

<script>
import ReferenceNode from "@/components/VerdictViewComponents/VerdictGraph/ReferenceNode";

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
      nodeWidth: 110,
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
      this.centerOffsetX = this.width * 0.5 - this.nodeWidth * 0.5
      this.centerOffsetY = this.height * 0.5 - this.nodeHeight * 0.5
    },
    lineGen(index, isIncoming) {
      let startX = 0
      let startY = 0
      let endX = 0
      let endY = 0
      if (isIncoming) {
        startX = this.nodeWidth
        startY = index * (this.nodeHeight + this.padding) + 0.5 * this.nodeHeight + this.inComingOffsetY
        endX = this.width * 0.5 - this.nodeWidth * 0.5
        endY = this.height * 0.5
      } else {
        startX = this.width - this.nodeWidth
        startY = index * (this.nodeHeight + this.padding) + 0.5 * this.nodeHeight + this.outGoingOffsetY
        endX = this.width * 0.5 + this.nodeWidth * 0.5
        endY = this.height * 0.5
      }
      return 'M ' + startX + ' ' + startY + ' L ' + endX + ' ' + endY
    }
  },
  mounted() {
    window.addEventListener("resize", this.updateSize);
    this.updateSize()
  },
  computed: {
    references() {
      return {
        incoming: ['2 BvE 4/21', '458jhfgsd', '191msnd', 'dasda', 'asdja', 'sda', 'asd'],
        outgoing: ['ndvy.ask', 'aljsdjow9', '-9kakpkapfghfghdf00'],
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
  }
}
</script>

<style scoped>
</style>