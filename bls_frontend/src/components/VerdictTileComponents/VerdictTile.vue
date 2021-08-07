<template>
  <div class="h-100">
    <b-card :class="colorClass" class="h-100">
      <b-container>
        <!-- Doctype row !-->
        <b-row class="bottom-margin">
          <b-col class="no-side-padding" cols="11">
            <b-button @click="setCurrentVerdict" class="doc-type-tag">
              <b-card-text class="inline-text">
                {{ verdict.documenttype }}
              </b-card-text>
              <img src="@/assets/forward.png">
            </b-button>
          </b-col>

          <b-col class="no-side-padding" cols="1">
            <DownloadButton class="download-button" :documentnumber="verdict.documentnumber"/>
          </b-col>
        </b-row>

        <b-row v-if="verdict.title" class="bottom-margin title">
          <b-card-text class="link" @click="setCurrentVerdict">{{ verdict.title }}</b-card-text>
        </b-row>

        <b-row class="bottom-margin text-padding">
          <b-card-text>{{ date }} | {{ verdict.court + ' ' + verdict.spruchkoerper }}</b-card-text>
        </b-row>

        <b-row class="bottom-margin">
          <KeyWordTags :keyWords="verdict.keywords" />
        </b-row>
      </b-container>

      <!-- Aktenzeichen row !-->
      <div v-if="verdict.filenumber" class="mb-2">
        <h5>Aktenzeichen</h5>
        <CopyButton :textId="verdict.documentnumber + 'filenumber'"/>
        <b-card-text class="text-padding" :id="verdict.documentnumber + 'filenumber'">{{ filenumbers }}</b-card-text>
      </div>

      <!-- Texte !-->
      <div v-if="keysentence" class="bottom-margin">
        <h5 class="link" @click="setCurrentVerdict">Leitsatz</h5>
        <CopyButton :textId="verdict.documentnumber + 'keysentence'"/>
        <b-card-text class="text-padding" :id="verdict.documentnumber + 'keysentence'">{{ keysentence }}</b-card-text>
      </div>
      <div v-if="tenor" class="bottom-margin">
        <h5 class="link" @click="setCurrentVerdict">Tenor</h5>
        <CopyButton :textId="verdict.documentnumber + 'tenor'"/>
        <b-card-text class="text-padding" :id="verdict.documentnumber + 'tenor'">{{ tenor }}</b-card-text>
      </div>


      <b-container v-if="verdict.norms.length > 0">
        <h5 class="no-indent">Normen</h5>
        <CopyButton :textId="verdict.documentnumber + 'norms'"/>
        <!-- Normen row !--> <!-- TODO: Dafür sorgen, dass die collapsables unabhängig offen bleiben !-->

        <b-row v-if="showNormsExpandable">
          <ExpandableText :content="norms" :id="verdict.documentnumber + 'exp'" :textId="verdict.documentnumber + 'norms'" />
        </b-row>

        <b-row class="text-padding" v-if="!showNormsExpandable">
          <b-card-text :id="verdict.documentnumber + 'norms'">{{ norms }}</b-card-text>
        </b-row>
      </b-container>

      <template #footer v-if="verdict.ecli">
        <!-- Date/Ecli row !-->
        <b-row>
          <b-col class="footer-color">
            <b-card-text>
              {{verdict.ecli}}
            </b-card-text>
          </b-col>
        </b-row>
      </template>
    </b-card>
  </div>
</template>


<script>

import ExpandableText from "@/components/UtilityComponents/ExpandableText";
import {ColorService} from "@/services/ColorService";
import CopyButton from "@/components/UtilityComponents/ActionButtons/CopyButton";
import {VerdictModel} from "@/models/verdict-model";
import KeyWordTags from "@/components/KeyWordTags";
import DownloadButton from "@/components/UtilityComponents/ActionButtons/DownloadButton";

const colorService = new ColorService()

/**
 * Component for verdict tile
 *
 * @param verdict a verdict object to be displayed in the tile
 *
 */
export default {
  name: "VerdictTile",
  props: {
    verdict: VerdictModel,
  },
  components: {
    KeyWordTags,
    CopyButton,
    ExpandableText,
    DownloadButton,
  },
  data() {
    return {
      norms: '',
      colorClass: '',
      resultColorClass: '',
      date: '',
      showNormsExpandable: false,
      filenumbers: '',
      keysentence: null,
      tenor: null,
    }
  },
  created() {
    if (this.verdict.norms) {
      const norms = this.verdict.norms.slice(0)
      this.norms = norms.join(', ');
      if (this.norms.length > 50 ) {
        this.showNormsExpandable = true
      }
    }

    if (this.verdict.filenumber) {
      const filenumbers = this.verdict.filenumber.slice(0)
      this.filenumbers = filenumbers.join(', ');
    }

    if (this.verdict.keysentence) {
      this.keysentence = this.verdict.keysentence.join(' ')
    }

    if (this.verdict.tenor) {
      this.tenor = this.verdict.tenor.join(' ')
    }

    this.colorClass = colorService.colorClass(this.verdict.documenttype)

    const date = this.verdict.date + ''
    this.date = date.substr(6, 2) + '.' + date.substr(4, 2) + '.' + date.substr(0, 4)
  },
  methods: {
    /**
     * Set the current verdict
     */
    setCurrentVerdict() {
      this.$router.push({ name: 'Verdict', query: { docnr: this.verdict.documentnumber } })
    }
  }
}
</script>

<style scoped>
  .text-padding {
    padding: 0px 12px;
  }

  .bottom-margin {
    margin-bottom: 15px;
  }

  .no-side-padding {
    padding-left: 0px;
    padding-right: 0px;
  }

  h5 {
    display: inline;
    margin-right: 8px;
  }

  .no-indent {
    margin-left: -15px;
  }

  .inline-text {
    display: inline;
  }

  .aktenzeichen {
    height: 54px;
    padding-top: 15px;
  }

  .doc-type-tag {
    display: inline-block;
    min-height: 54px;
    width: auto;
    border-radius: 4px;
    padding: 14px 12px;
    border: none;
    color: white;
  }

  .footer-color {
    color: rgba(69,69,69,0.5);
  }

  .title {
    font-weight: bold;
  }

  .link {
    cursor: pointer;
  }

  .link:hover {
    text-decoration: underline;
  }
</style>