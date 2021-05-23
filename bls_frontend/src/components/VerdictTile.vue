<template>
  <div class="card-div">
    <b-card :class="colorClass">
      <b-container>
        <!-- Doctype row !-->
        <b-row class="bottom-margin">
          <b-col class="no-side-padding">
            <b-button  to="/urteil" class="doc-type-tag">
              <b-card-text class="inline-text">
                {{ verdict.documenttype }}
              </b-card-text>
              <img src="@/assets/forward.png">
            </b-button>
          </b-col>
        </b-row>

        <b-row class="bottom-margin text-padding">
          <b-card-text>{{ verdict.date }} | {{ verdict.court + ' ' + verdict.spruchkoerper }}</b-card-text>
        </b-row>

        <b-row class="bottom-margin">
          <KeyWordTags :keyWords="['Ablehnung', 'GKG', 'Kostenverzeichnisses', 'Gerichtskosten', 'etc', 'usw', 'Ich bin ein Keyword']" />
        </b-row>

        <!-- Aktenzeichen row !-->
        <b-row class="bottom-margin">
          <b-col class="aktenzeichen no-side-padding">
            <DropDownText :items="verdict.filenumber" :id="verdict.documentnumber + 'drop'" />
          </b-col>
        </b-row>
      </b-container>

      <!-- Texte !-->
      <div v-if="verdict.keysentence" class="bottom-margin">
        <h5>Leitsatz</h5>
        <CopyButton :id="verdict.documentnumber + 'keysentence'" />
        <b-card-text class="text-padding" :id="verdict.documentnumber + 'keysentence'">{{ verdict.keysentence }}</b-card-text>
      </div>
      <div v-if="verdict.tenor" class="bottom-margin">
        <h5>Tenor</h5>
        <CopyButton :id="verdict.documentnumber + 'tenor'" />
        <b-card-text class="text-padding" :id="verdict.documentnumber + 'tenor'">{{ verdict.tenor }}</b-card-text>
      </div>

      <b-container v-if="verdict.norms">
        <!-- Normen row !--> <!-- TODO: Dafür sorgen, dass die collapsables unabhängig offen bleiben !-->
        <b-row>
          <ExpandableText :content="norms" :id="verdict.documentnumber + 'exp'" />
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

import DropDownText from "@/components/DropDownText";
import ExpandableText from "@/components/ExpandableText";
import {ColorService} from "@/services/ColorService";
import CopyButton from "@/components/CopyButton";
import {VerdictModel} from "@/models/verdict-model";
import KeyWordTags from "@/components/KeyWordTags";

const colorService = new ColorService()

export default {
  name: "VerdictTile",
  props: {
    verdict: VerdictModel,
  },
  components: {
    KeyWordTags,
    CopyButton,
    ExpandableText,
    DropDownText,
  },
  data() {
    return {
      norms: '',
      normsBrief: '',
      colorClass: '',
    }
  },
  created() {
    if (this.verdict.norms) {
      const norms = this.verdict.norms.slice(0)
      this.norms = norms.join(',   ');
    }

    this.colorClass = colorService.colorClass(this.verdict.documenttype)
  },
}
</script>

<style scoped>
  .card-div {
    margin-bottom: 20px;
    min-width: 480px;
  }

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
    border-radius: .25rem;
    padding: 14px 12px;
    border: none;
    color: white;
  }

  .footer-color {
    color: rgba(69,69,69,0.5);
  }
</style>