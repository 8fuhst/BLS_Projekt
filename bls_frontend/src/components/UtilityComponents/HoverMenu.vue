<template>
  <div class="hover-menu">
    <LinkButton v-if="link" :filenumber="linkFilenumber"></LinkButton>
    <CopyButton v-if="copy" :textId="copyTextId"></CopyButton>
  </div>
</template>

<script>
import CopyButton from "@/components/UtilityComponents/ActionButtons/CopyButton";
import LinkButton from "@/components/UtilityComponents/ActionButtons/LinkButton";

/**
 * Component for the hover menu
 *
 * @param copy Boolean - true when the copy function should be displayed, else false
 * @param copyTextId String to be copied
 * @param link Boolean - true when the link function should be displayed, else false
 * @param linkFilenumber String of filenumber to be navigated to
 *
 */
export default {
  name: "HoverMenu",
  components: {LinkButton, CopyButton},
  props: {
    copy: Boolean,
    copyTextId: String,
    link: Boolean,
    linkFilenumber: String,
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