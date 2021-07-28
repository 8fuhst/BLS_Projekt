<template>
  <div class="icon-container" @click="copyToClipboard(textId)" v-on:mouseleave="noCopied" v-b-tooltip.hover :title="copied ? 'Kopiert!' : 'Kopieren'">
    <b-icon-clipboard class="icon" />
  </div>
</template>

<script>
/**
 * Component for the copy button
 *
 * @param textId for the verdict documentnumber
 *
 */
export default {
  name: "CopyButton",
  props: {
    textId: String,
  },
  data() {
    return {
      copied: false
    }
  },
  methods: {
    /**
     * Copies the text to clipboard
     *
     * @param id for the text to copy
     */
    copyToClipboard(id) {
      const text = document.querySelector('#' + id).innerHTML
      const elem = document.createElement("textarea")
      document.body.appendChild(elem)
      elem.value = text
      elem.select()
      document.execCommand("copy")
      document.body.removeChild(elem)

      this.copied = true
    },
    async noCopied() {
      setTimeout(() => {this.copied = false}, 300)
    }
  }
}
</script>

<style scoped>
  .icon-container {
    height: 24px;
    width: 24px;
    border-radius: 4px;
    cursor: pointer;
    display: inline-block;
    margin-top: -4px;
  }

  .icon-container:hover {
    background: rgba(75,75,75,0.15);
  }

  .icon {
    position: relative;
    left: 4px;
  }
</style>