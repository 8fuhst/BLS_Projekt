<template>
  <div class="hero">
    <div class="bottom-margin">
      <b-icon-chevron-left @click="goBack" class="inline back"></b-icon-chevron-left>
      <b-card-text class="inline headline">{{ verdict.documenttype + ' | ' + date + ' | ' + verdict.court + ' ' + verdict.spruchkoerper }}</b-card-text>
    </div>
    <KeyWordTags class="bottom-margin" :keyWords="['Ablehnung', 'GKG', 'Kostenverzeichnisses', 'Gerichtskosten', 'etc', 'usw', 'Ich bin ein Keyword']"/>

    <div v-if="keysentence" class="bottom-margin">
      <h5 class="inline">Leitsatz</h5>
      <CopyButton class="inline-block" :textId="verdict.documentnumber + 'keysentence'" />
      <b-card-text class="text-padding" :id="verdict.documentnumber + 'keysentence'">{{ keysentence }}</b-card-text>
    </div>


    <div class="button-group">
      <b-button-group>
        <b-button>Zum Leitsatz</b-button>
        <b-button href="#tenor">Zum Tenor</b-button>
        <b-button href="#sachverhalt">Zur Sachverhaltsdarstellung</b-button>
        <b-button href="#bewertung">Zur rechtlichen Bewertung</b-button>
      </b-button-group>
    </div>
  </div>
</template>

<script>
import KeyWordTags from "@/components/KeyWordTags";
import CopyButton from "@/components/UtilityComponents/CopyButton";

export default {
  name: "VerdictHero",
  components: { KeyWordTags, CopyButton },
  computed: {
    verdict() {
      return this.$store.getters.getCurrentVerdict
    }
  },
  methods: {
    goBack() {
      this.$router.back()
    },
    setProperties() {
      if (this.verdict.keysentence) {
        this.keysentence = this.verdict.keysentence.join(', ')
      }

      const date = this.verdict.date + ''
      this.date = date.substr(6, 2) + '.' + date.substr(4, 2) + '.' + date.substr(0, 4)
    }
  },
  data() {
    return {
      keysentence: null,
      date: '',
    }
  },
  created() {
    this.setProperties()
  },
  watch: {
    verdict: function () {
      this.setProperties()
    }
  }
}
</script>

<style scoped>
  .hero {
    min-height: 345px;
    width: 80%;
    margin: 0 10%;
    position: relative;
    padding: 20px 40px;
  }

  .inline {
    display: inline;
  }

  .inline-block {
    display: inline-block;
  }

  .headline {
    font-size: 26px;
  }

  .back {
    cursor: pointer;
    font-size: 26px;
    margin-right: 12px;
  }

  .bottom-margin {
    margin-bottom: 15px;
  }

  .text-padding {
    padding: 0 12px;
  }

  h5 {
    margin-right: 8px;
  }

  .button-group {
    position: absolute;

    bottom: 12px;
  }
</style>