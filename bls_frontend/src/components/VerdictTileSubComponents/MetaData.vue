<template>
  <TextBox :text="metaData.gericht"/>
  <DropDownTextBox :texts="metaData.aktenzeichen"/>
  <TextBox :text="metaData.datum"/>
  <TextBox :text="metaData.ecli"/>
  <ExpandableTextBox :texts="metaData.normen"/>
</template>

<script>
import TextBox from "@/components/VerdictTileSubComponents/TextBox";
import DropDownTextBox from "@/components/VerdictTileSubComponents/DropDownTextBox";
import ExpandableTextBox from "@/components/VerdictTileSubComponents/ExpandableTextBox";

export default {
  name: "MetaData",
  props: {
    metaData: Object,
  },
  components: {
    ExpandableTextBox,
    DropDownTextBox,
    TextBox
  }
}
</script>

<style scoped>

</style>