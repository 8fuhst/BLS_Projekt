<template>
  <div class="key-words-container">
    <div v-for="(item, idx) in keyWords" :key="idx" class="badges">
      <b-badge>{{ item }}</b-badge>
    </div>
  </div>
</template>

<script>
export default {
  name: "KeyWordTags",
  props: {
    keyWords: Array,
  }
}
</script>

<style scoped>
  .key-words-container {
    margin-bottom: 4px;
    padding: 0 8px;
  }

  .badges {
    display: inline;
    margin-right: 5px;
  }
</style>