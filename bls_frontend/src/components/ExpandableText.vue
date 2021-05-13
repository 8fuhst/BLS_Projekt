<template>
  <div>
    <b-button @click="toggleShowFullContent" block>{{ showFullContent ? content : contentBrief }}</b-button>
  </div>
</template>

<script>
export default {
  name: "ExpandableText",
  props: {
    content: String,
  },
  data() {
    return {
      contentBrief: '',
      showFullContent: false,
    }
  },
  created() {
    this.contentBrief = this.content.substr(0, 40) + '...'
  },
  methods: {
    toggleShowFullContent() {
      this.showFullContent = !this.showFullContent
    }
  }
}
</script>

<style scoped>
  .normal {
    max-height: 30px;
  }
</style>