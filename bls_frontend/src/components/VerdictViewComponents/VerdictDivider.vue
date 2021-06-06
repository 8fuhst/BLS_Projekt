<template>
  <div class="divider">
    <h5>{{ text }}</h5>
  </div>
</template>

<script>
export default {
  name: "VerdictDivider",
  props: {
    text: String,
  }
}
</script>

<style scoped>
  .divider {
    height: 52px;
    width: 100%;
    background-color: rgba(206, 206, 206, 0.5);
    padding: 14px 40px;
  }
</style>