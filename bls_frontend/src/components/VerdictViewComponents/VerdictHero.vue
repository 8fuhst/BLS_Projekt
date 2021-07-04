<template>
  <div class="hero" id="verdictHero">
    <b-container fluid>
      <b-row>
        <b-col xl="8" sm="12">
          <div class="bottom-margin">
            <b-icon-chevron-left @click="goBack" class="d-inline back"></b-icon-chevron-left>
            <b-card-text class="d-inline headline">{{ verdict.documenttype + ' | ' + date + ' | ' + verdict.court + ' ' + verdict.spruchkoerper + ' | ' + filenumber }}</b-card-text>
            <DownloadButton :verdictInfo="verdict"/>
          </div>

          <b-card-text class="font-weight-bold" v-if="verdict.title">{{ verdict.title }}</b-card-text>

          <KeyWordTags class="bottom-margin" :keyWords="verdict.keywords"/>

          <h2><b-badge :class="resultColorClass">{{ verdict.result }}</b-badge></h2>

          <div v-if="keysentence">
            <h5 class="d-inline">Leitsatz</h5>
            <CopyButton class="d-inline-block" :textId="verdict.documentnumber + 'keysentence'" />
            <b-card-text class="text-padding" :id="verdict.documentnumber + 'keysentence'">{{ keysentence }}</b-card-text>
          </div>
        </b-col>
        <b-col class="py-3" xl="4" sm="0">
          <VerdictGraph />
        </b-col>
      </b-row>
    </b-container>

    <div class="button-group" >
      <b-button-group>
        <b-button v-if="verdict.tenor" @click="scrollTo('#tenor')" class="scroll">Zum Tenor</b-button>
        <b-button v-if="verdict.modelledOffense.length > 0" @click="scrollTo('#sachverhalt')" class="scroll">Zur Sachverhaltsdarstellung</b-button>
        <b-button v-if="verdict.modelledReasonsForDecision.length > 0" @click="scrollTo('#bewertung')" class="scroll">Zur rechtlichen Bewertung</b-button>
      </b-button-group>
    </div>

  </div>
</template>

<script>
import KeyWordTags from "@/components/KeyWordTags";
import CopyButton from "@/components/UtilityComponents/ActionButtons/CopyButton";
import VerdictGraph from "@/components/VerdictViewComponents/VerdictGraph/VerdictGraph";
import {ColorService} from "@/services/ColorService";
import DownloadButton from "@/components/UtilityComponents/ActionButtons/DownloadButton";

const colorService = new ColorService()

export default {
  name: "VerdictHero",
  components: {DownloadButton, VerdictGraph, KeyWordTags, CopyButton },
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
        this.keysentence = this.verdict.keysentence.join(' ')
      }
      if (this.verdict.filenumber) {
        this.filenumber = this.verdict.filenumber.join(', ')
      }

      this.resultColorClass = colorService.resultColorClass(this.verdict.result)

      const date = this.verdict.date + ''
      this.date = date.substr(6, 2) + '.' + date.substr(4, 2) + '.' + date.substr(0, 4)
    },
    scrollTo(id) {
      document.querySelector(id).scrollIntoView({
        behavior: 'smooth'
      });
    }
  },
  data() {
    return {
      keysentence: null,
      date: '',
      filenumber: null,
      stickyNavButtons: false,
      resultColorClass: '',
    }
  },
  mounted() {
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
    width: 90%;
    margin: 0 5%;
    position: relative;
    padding: 20px 24px 62px 24px;
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

  .scroll {
    scroll-behavior: smooth;
  }
</style>