<template>
  <div class="hover-menu">
    <CopyButton v-if="copy" :textId="copyTextId"></CopyButton>
  </div>
</template>

<script>
import CopyButton from "@/components/UtilityComponents/CopyButton";
export default {
  name: "HoverMenu",
  components: {CopyButton},
  props: {
    copy: Boolean,
    copyTextId: String,
  }
}
</script>

<style scoped>
  .hover-menu {
    border: 1px solid black;
    border-radius: 4px;
    background-color: white;
    height: 30px;
    width: fit-content;
    padding: 2px;
  }
</style>