<template>
  <div class="icon-container" @click="getNewVerdict" v-b-tooltip.hover :title="'Zum Urteil'">
    <b-icon-link45deg class="icon" />
  </div>
</template>

<script>
export default {
  name: "LinkButton",
  props: {
    filenumber: String,
  },
  methods: {
    async getNewVerdict() {
      const newVerdict = await this.$store.dispatch('getVerdictByFilenumber', this.filenumber)
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
  .icon-container {
    height: 24px;
    width: 24px;
    border-radius: 4px;
    cursor: pointer;
    display: inline-block;
    margin-top: -4px;
  }

  .icon-container:hover {
    background: rgba(75,75,75,0.15);
  }

  .icon {
    position: relative;
    left: 4px;
  }
</style>