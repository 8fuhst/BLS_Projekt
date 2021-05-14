<template>
  <div class="home">
    <b-container class="center">
      <h3>Neue Urteile:</h3>
      <b-row>
        <VerdictTileList :verdicts="verdicts" />
      </b-row>
    </b-container>

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

      return await res.json()
    }
  },
  async created() {
    try {
      const data = await this.fetchVerdicts()
      this.verdicts = [
        {
          id: '1',
          metaData: {
            gericht: data.gericht,
            datum: data.entscheidungsdatum,
            aktenzeichen: data.aktenzeichen,
            ecli: data.ecli,
            normen: data.normen,
          },
          docType: data.dokumenttyp,
          keySentence: data.Kurztext,
          tenor: data.tenor,
          langtext: data.Langtext
        },
        {
          id: '2',
          metaData: {
            gericht: data.gericht,
            datum: data.entscheidungsdatum,
            aktenzeichen: data.aktenzeichen,
            ecli: data.ecli,
            normen: data.normen.slice(0, 3),
          },
          docType: data.dokumenttyp,
          keySentence: data.Kurztext,
          tenor: data.tenor,
          langtext: data.Langtext
        },
        {
          id: '3',
          metaData: {
            gericht: data.gericht,
            datum: data.entscheidungsdatum,
            aktenzeichen: data.aktenzeichen,
            ecli: data.ecli,
            normen: data.normen,
          },
          docType: data.dokumenttyp,
          keySentence: data.Kurztext,
          tenor: data.tenor,
          langtext: data.Langtext
        }
      ]
    } catch (e) {
      console.log('Error')
    }
  }
}
</script>

<style scoped>
.center {
  max-width: 480px;
}
</style>
