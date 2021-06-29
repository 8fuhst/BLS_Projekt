<template>
  <svg @mouseover="hover = true" @mouseout="hover = false">
    <svg v-if="!hover" @click="getNewVerdict" class="node"  :x="xOffset" :y="index * height + index * padding + yOffset" :width="width" :height="height">
      <rect x="0" y="0" width="100%" height="100%" stroke="black" stroke-width="1px" />
      <text x="50%" y="50%" text-anchor="middle" font-size="16" fill="black">{{ text }}</text>
    </svg>
    <svg v-if="hover" :x="xOffset" :y="index * height + index * padding + yOffset" :width="width" :height="height">

    </svg>
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
  data() {
    return {
      hover: {
        type: Boolean,
        default: false
      }
    }
  },
  methods: {
    async getNewVerdict() {
      this.$store.commit('setPage', 0)
      await this.$store.dispatch('setQuery', this.text)
      const newVerdict = this.$store.getters.getVerdicts[0]
      await this.$router.push({name: 'Verdict', query: {docnr: newVerdict.documentnumber}})

      window.scroll({
        top: 0,
        left: 0,
      });
    }
  }
}
</script>

<style scoped>
  svg {
    fill: white;
  }

  svg:hover {
    fill: rgb(187,187,187);
    cursor: pointer;
  }
</style>