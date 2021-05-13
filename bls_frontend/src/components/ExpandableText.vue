<template>
  <div class="exp-text">
    <b-button block v-b-toggle.accordion-1 class="btn-secondary" @click="toggleShowFullContent">
      {{ showFullContent ? '' : contentBrief }}
      <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
        <b-card-text>{{ content }}</b-card-text>
      </b-collapse>
    </b-button>

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
      this.showFullContent = !this.showFullContent;

      const button = document.getElementById("button");
      button.classList.toggle("expanded");
    }
  }
}
</script>

<style scoped>
  .exp-text {
    min-height: 54px;
    width: 100%;
  }

  .btn-secondary {
    color: black;
    background: white;
    border-color: black;
    min-height: 54px;
  }

  .btn-secondary:hover {
    color: black;
    background: white;
    box-shadow: none;
  }

  .btn-secondary:focus {
    box-shadow: none;
  }
</style>