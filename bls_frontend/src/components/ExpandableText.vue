<template>
  <div class="expandable-text">
    <b-collapse :id="id">
      <b-card-text class="siblings text">
        {{ content }}
      </b-card-text>
      <b-icon-chevron-down :rotate="showFullContent ? -180 : 0" class="show-more-less" v-b-toggle="id" @click="toggleShowFullContent" />
    </b-collapse>
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

  .text {
    float:left;
    display:inline;
    width: auto;
    max-width: 365px;
  }

  .show-more-less {
    float: right;
    width: 24px;
    position: absolute;
    bottom: 0;
    right: 0;
    transition: all .25s;
    text-decoration: none;
  }

  .expandable-text .collapse:before {
    content: ' ...';
    position: absolute;
    right: 2rem;
    bottom: 0;
  }

  .show-more-less:focus {
    outline: 0;
  }

  .expandable-text .collapse, .expandable-text .collapsing {
    height: 1.5rem;  /* [NUM_OF_LINES] x [LINE_HEIGHT] */
    min-height: 1.5rem !important;
  }

  .expandable-text .collapse {
    position: relative;  /* For ...'s content absolute positioning */
    display: block !important;
    overflow: hidden;
  }

  .expandable-text .collapse.show {
    height: auto;  /* You need to reset the height when not collapsed */
  }

  .expandable-text .collapse.show:before {
    display: none;  /* Of course you don't want to display ... */
  }
</style>