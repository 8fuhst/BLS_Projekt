<template>
  <div class="expandable-text" v-b-toggle="id" @click="toggleShowFullContent">
    <b-card-text block >
      {{ showFullContent ? '' : contentBrief }}
      <b-collapse :id="id" accordion="my-accordion" role="tabpanel">
        <b-card-text>{{ content }}</b-card-text>
      </b-collapse>
    </b-card-text>

  </div>
</template>

<script>
export default {
  name: "ExpandableText",
  props: {
    content: String,
    contentBrief: String,
    id: String,
  },
  data() {
    return {
      showFullContent: false,
    }
  },
  methods: {
    toggleShowFullContent() {
      this.showFullContent = !this.showFullContent;
    }
  }
}
</script>

<style scoped>
  .expandable-text {
    min-height: 54px;
    width: 100%;

    color: black;
    background: white;
    border: 1px solid black;
    border-radius: .25rem;

    text-align: center;
    vertical-align: middle;

    padding: 14px 12px;

    text-align: left;
  }
</style>