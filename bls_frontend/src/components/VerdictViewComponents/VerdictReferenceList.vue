<template>
  <div class="references">
    <VerdictReference v-for="(reference, index) in verdictNode.outgoingReferenceList[0][1].gruende" v-bind:key="index"
      :section="'bewertung'" :indexInput="reference[0]" :text="reference[1]"/>
  </div>
</template>

<script>
import VerdictReference from "@/components/VerdictViewComponents/VerdictReference";
export default {
  name: "VerdictReferenceList",
  components: {VerdictReference},
  computed: {
    verdictNode() {
      return this.$store.getters.getVerdictNode
    }
  },
  mounted() {
  }
}
</script>

<style scoped>
  .references {
    padding: 54px 0;
    display: inline-block;
    width: 38%;
    background-color: rgba(206, 206, 206, 0.5);
  }
</style>