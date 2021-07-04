<template>
  <div class="icon-container" @click="downloadAsTXT(verdictInfo)" v-b-tooltip.hover :title="'Download'">
    <b-icon-download class="icon" />
  </div>
</template>

<script>
import {VerdictModel} from "@/models/verdict-model";

export default {
  name: "DownloadButton",
  props: {
    verdictInfo: VerdictModel,
  },
  methods: {
    downloadAsTXT(verdictText){
      const date = verdictText.date + ''
      this.date = date.substr(6, 2) + '.' + date.substr(4, 2) + '.' + date.substr(0, 4)

      const txtData =
          verdictText.documenttype + ' - ' + this.date + ' - ' + verdictText.court + ' - ' + verdictText.spruchkoerper + ' - ' + verdictText.filenumber + '\n\n' +
          verdictText.title + '\n\n' +
          verdictText.keywords + '\n\n' +
          verdictText.result + '\n\n' +
          verdictText.tenor + '\n\n'
          // TODO: alle gewünschten Elemente des Urteils einfügen
      const txtName = "Urteil_" + verdictText.filenumber + ".txt"
      const blob = new Blob([txtData])
      const url = URL.createObjectURL(blob)

      const download = (path, filename) => {
        const anchor = document.createElement('a')
        anchor.href = path
        anchor.download = filename
        document.body.appendChild(anchor)
        anchor.click()
        document.body.removeChild(anchor)
      }
      download(url, txtName)
    },
  },
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