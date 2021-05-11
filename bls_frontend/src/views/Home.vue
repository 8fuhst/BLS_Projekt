<template>
  <div class="home">
    <VerdictTileList :verdicts="verdicts" />
  </div>
</template>

<script>
// @ is an alias to /src
import VerdictTileList from "@/components/VerdictTileList";

export default {
  name: 'Home',
  components: {
    VerdictTileList
  },
  data() {
    return {
      verdicts: [],
    }
  },
  methods: {
    async fetchVerdicts() {
      const res = await fetch(`api/urteil`)

      const data = await res.json()

      return data
    }
  },
  async created() {
    const data = await this.fetchVerdicts()
    this.verdicts = [
      {
        metaData: {
          gericht: data.gericht,
          datum: data.entscheidungsdatum,
          aktenzeichen: data.aktenzeichen,
          ecli: data.ecli,
          normen: data.normen,
        },
        docType: data.dokumenttyp,
        keySentence: data.Kurztext,
        langtext: data.Langtext
      }
    ]
  }
}
</script>
