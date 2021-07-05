<template>
  <div class="icon-container" @click="download(documentnumber)" v-b-tooltip.hover :title="'Download'">
    <b-icon-download class="icon" />
  </div>
</template>

<script>
import ApiService from "@/services/ApiService";

const apiService = new ApiService()

export default {
  name: "DownloadButton",
  props: {
    documentnumber: String,
  },
  methods: {
    download(documentnumber){
      apiService.downloadVerdictData(documentnumber)
    },
  },
}
</script>

<style scoped>
  .icon-container {
    height: 30px;
    width: 30px;
    border-radius: 4px;
    cursor: pointer;
    display: inline-block;
  }

  .icon-container:hover {
    background: rgba(75,75,75,0.15);
  }

  .icon {
    position: relative;
    left: 4px;
    top: 4px;
    font-size: 22px;
  }
</style>