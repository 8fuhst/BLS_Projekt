<template>
  <div class="hero" id="verdictHero">
    <b-container fluid>
      <b-row>
        <b-col>
          <div class="bottom-margin">
            <b-icon-chevron-left @click="goBack" class="d-inline back"></b-icon-chevron-left>
            <b-card-text class="d-inline headline">{{ verdict.documenttype + ' | ' + date + ' | ' + verdict.court + ' ' + verdict.spruchkoerper + ' | ' + filenumber }}</b-card-text>
            <DownloadButton class="download-button" :documentnumber="verdict.documentnumber"/>
          </div>

          <b-card-text class="font-weight-bold" v-if="verdict.title">{{ verdict.title }}</b-card-text>

          <KeyWordTags class="bottom-margin" :keyWords="verdict.keywords"/>

          <div v-if="keysentence">
            <h5 class="d-inline">Leitsatz</h5>
            <CopyButton class="d-inline-block" :textId="verdict.documentnumber + 'keysentence'" />
            <b-card-text class="text-padding" :id="verdict.documentnumber + 'keysentence'">{{ keysentence }}</b-card-text>
          </div>
        </b-col>
      </b-row>
      <b-row class="py-3" v-show="graphShown">
        <div :class="scrollHidden ? 'graph-container-hidden' : 'graph-container'">
          <VerdictGraph @showGraphEvent="showGraph" @scrollHidden="hideScroll" />
        </div>
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
import DownloadButton from "@/components/UtilityComponents/ActionButtons/DownloadButton";

/**
 * Component to build the header on the detailed view of the current verdict
 *
 */
export default {
  name: "VerdictHero",
  components: {DownloadButton, VerdictGraph, KeyWordTags, CopyButton },
  computed: {
    /**
     * Returns the current verdict
     */
    verdict() {
      return this.$store.getters.getCurrentVerdict
    },
  },
  methods: {
    /**
     * To navigate back to Home view
     */
    goBack() {
      this.$router.back()
    },
    /**
     * Sets the properties for keysentence, filenumber, resultColorClass and date according to current value
     */
    setProperties() {
      if (this.verdict.keysentence) {
        this.keysentence = this.verdict.keysentence.join(' ')
      }
      if (this.verdict.filenumber) {
        this.filenumber = this.verdict.filenumber.join(', ')
      }

      const date = this.verdict.date + ''
      this.date = date.substr(6, 2) + '.' + date.substr(4, 2) + '.' + date.substr(0, 4)
    },
    /**
     * Scrolls to the requested part of verdict
     *
     * @param id String of the part to scroll to
     */
    scrollTo(id) {
      document.querySelector(id).scrollIntoView({
        behavior: 'smooth'
      });
    },
    /**
     * Sets the hidden property according to the parameter hidden
     *
     * @param hidden boolean for whether hidden is set or not. True if hidden shall be set to true. Else false
     */
    hideScroll(hidden) {
      this.scrollHidden = hidden
    },
    /**
     * Sets the graphShown property according to the parameter show
     *
     * @param show Boolean for whether the graph should be shown or not. True if graph should be shown
     */
    showGraph(show) {
      this.graphShown = show
    }
  },
  data() {
    return {
      keysentence: null,
      date: '',
      filenumber: null,
      stickyNavButtons: false,
      resultColorClass: '',
      scrollHidden: true,
      graphShown: false
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
    margin-left: 4px;
    bottom: 12px;
  }

  .scroll {
    scroll-behavior: smooth;
  }

  .download-button {
    position: relative;
    top: -5px;
    left: 12px;
  }

  .graph-container {
    width: 100%;
    max-height: 369px;
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .graph-container-hidden {
    width: 100%;
    max-height: 369px;
    overflow: hidden;
  }

  .graph-container::-webkit-scrollbar { width: 0 !important }
</style>