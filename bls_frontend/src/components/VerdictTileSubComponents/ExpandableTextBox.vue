<template>
  <div :key="text.id" v-for="text in texts">
    <span>{{ text }}</span>
  </div>
</template>

<script>
export default {
  name: "ExpandableTextBox",
  props: {
    texts: Array
  }
}
</script>

<style scoped>

</style>