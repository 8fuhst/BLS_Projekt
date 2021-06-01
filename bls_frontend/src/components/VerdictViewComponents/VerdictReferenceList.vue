<template>
  <div class="references">
    <VerdictReference />
  </div>
</template>

<script>
import VerdictReference from "@/components/VerdictViewComponents/VerdictReference";
export default {
  name: "VerdictReferenceList",
  components: {VerdictReference}
}
</script>

<style scoped>
  .references {
    padding: 54px 0;
    display: inline-block;
    width: 38%;
    height: 500px;
    background-color: rgba(206, 206, 206, 0.5);
  }
</style>