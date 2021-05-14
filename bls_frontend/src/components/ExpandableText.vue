<template>
  <div class="expandable-text transition">
    <b-card-text :class="['siblings', 'text', 'collapse', showFullContent? '' : 'brief-text']">
      {{ content }}
    </b-card-text>
    <img class="siblings icon" src="@/assets/show-more.png" v-b-toggle="id" @click="toggleShowFullContent" v-show="!showFullContent">
    <img class="icon" src="@/assets/show-less.png" v-b-toggle="id" @click="toggleShowFullContent" v-show="showFullContent">
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
    border: 1px solid rgba(0, 0, 0, .3);
    border-radius: .25rem;

    text-align: center;
    vertical-align: middle;

    padding: 14px 12px;

    text-align: left;
  }

  .siblings {
    float:left;
    display:inline;
    width: auto;
  }

  .icon {
    float: right;
    width: 24px;
  }

  .text {
    cursor: auto;
    margin: 0 12px 0 0;
  }

  .brief-text {
    text-overflow: ellipsis;
    height: 24px;
    overflow: hidden;
    max-width: 376px;
    white-space: nowrap;
  }
</style>