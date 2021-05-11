<template>
  <p>{{ keySentence }}</p>
  <p v-if="tenor">{{ tenor }}</p>
</template>

<script>
export default {
  name: "TeaserText",
  props: {
    keySentence: String,
    tenor: String,
  }
}
</script>

<style scoped>

</style>