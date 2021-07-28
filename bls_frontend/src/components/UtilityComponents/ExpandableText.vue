<template>
  <div class="expandable-text">
    <b-collapse :id="id" class="pr-5">
      <b-card-text class="text" :id="textId">
        {{ content }}
      </b-card-text>
      <b-icon-chevron-down :rotate="showFullContent ? -180 : 0" class="show-more-less" v-b-toggle="id" @click="toggleShowFullContent" />
    </b-collapse>
  </div>
</template>

<script>

/**
 * Component to make text expandable
 *
 * @param content String containing the expandable text
 * @param id String to identify verdict documentnumber
 * @param textId String to identify verdict documentnumber
 *
 */
export default {
  name: "ExpandableText",
  props: {
    content: String,
    id: String,
    textId: String,
  },
  data() {
    return {
      showFullContent: false,
    }
  },
  methods: {
    /**
     * Toggles between showing full content and not showing full content
     */
    toggleShowFullContent() {
      this.showFullContent = !this.showFullContent;
    }
  }
}
</script>

<style scoped>
  .expandable-text {
    min-height: 24px;
    width: 100%;

    color: black;
    background: white;

    text-align: center;
    vertical-align: middle;

    padding: 0px 12px;

    text-align: left;
  }

  .text {
    float:left;
    display:inline;
    width: auto;
    max-width: 365px;
    margin: 0;
  }

  .show-more-less {
    float: right;
    width: 24px;
    position: absolute;
    bottom: 4px;
    right: 0;
    transition: all .25s;
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
    height: 1.5rem;
    min-height: 1.5rem !important;
  }

  .expandable-text .collapse {
    position: relative;
    display: block !important;
    overflow: hidden;
  }

  .expandable-text .collapse.show {
    height: auto;
  }

  .expandable-text .collapse.show:before {
    display: none;
  }
</style>