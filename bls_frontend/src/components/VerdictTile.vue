<template>
  <div class="card-div">
    <b-card :class="colorClass">
      <b-container>
        <!-- Doctype row !-->
        <b-row class="bottom-margin">
          <b-col class="al-left no-side-padding">
            <b-button  to="/urteil" variant="danger" class="doc-type-tag doc-type-text">
              <b-card-text style="display: inline;">
                {{ verdict.documenttype }}
              </b-card-text>
              <img src="@/assets/forward.png">
            </b-button>
          </b-col>
        </b-row>

        <b-row class="bottom-margin text-padding">
          <b-card-text>{{ verdict.date }} | {{ verdict.court + ' ' + verdict.spruchkoerper }}</b-card-text>
        </b-row>

        <!-- Gericht/Aktenzeichen row !-->
        <b-row class="bottom-margin">
          <b-col class="al-right entry no-side-padding">
            <DropDownText :items="verdict.filenumber" :id="verdict.documentnumber + 'drop'" />
          </b-col>
        </b-row>
      </b-container>

      <!-- Texte !-->
      <div v-if="verdict.keysentence" class="bottom-margin">
        <h5>Leitsatz</h5>
        <div class="icon-container" @click="copyToClipboard(verdict.documentnumber + 'keysentence')" v-b-tooltip.click title="Kopiert">
          <b-icon-clipboard class="icon" />
        </div>
        <b-card-text class="text-padding" :id="verdict.documentnumber + 'keysentence'">{{ verdict.keysentence }}</b-card-text>
      </div>
      <div v-if="verdict.tenor" class="bottom-margin">
        <h5>Tenor</h5>
        <div class="icon-container" @click="copyToClipboard(verdict.documentnumber + 'tenor')" v-b-tooltip.click title="Kopiert">
          <b-icon-clipboard class="icon" />
        </div>
        <b-card-text class="text-padding" :id="verdict.documentnumber + 'tenor'">{{ verdict.tenor }}</b-card-text>
      </div>

      <b-container>
        <!-- Normen row !--> <!-- TODO: Dafür sorgen, dass die collapsables unabhängig offen bleiben !-->
        <b-row>
          <ExpandableText :content="norms" :content-brief="normsBrief" :id="verdict.documentnumber + 'exp'" />
        </b-row>
      </b-container>

      <template #footer>
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
import { colorDictionary } from "@/services/ColorService";

export default {
  name: "VerdictTile",
  props: {
    verdict: Object,
  },
  components: {
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
    const norms = this.verdict.norms.slice(0)
    this.norms = norms.join(',   ');
    if (norms.length > 3) {
      this.normsBrief = norms.slice(0, 3).join(', ') + ' ...'
    } else {
      // TODO: Dann auch dafür sorgen, dass das Ding nicht expandable ist
      this.normsBrief = norms.join(', ')
    }

    this.colorClass = colorDictionary[this.verdict.documenttype]
  },
  methods: {
    copyToClipboard(id) {
      const text = document.querySelector('#' + id).innerHTML
      const elem = document.createElement("textarea")
      document.body.appendChild(elem)
      elem.value = text
      elem.select()
      document.execCommand("copy")
      document.body.removeChild(elem)
    }
  }
}
</script>

<style scoped>
  .card-div {
    margin-bottom: 20px;
    min-width: 480px;
  }

  .al-right {
    text-align: right;
  }

  .al-center {
    text-align: center;
  }

  .entry {
    padding: 15px 12px;
    height: 54px;
  }

  .text-padding {
    padding: 0px 12px;
  }

  .doc-type-tag {
    display: inline-block;
    height: 54px;
    width: auto;
    border-radius: .25rem;
    padding: 14px 12px;
    border: none;
  }

  .doc-type-text {
    color: white;
  }

  .bottom-margin {
    margin-bottom: 15px;
  }

  .no-side-padding {
    padding-left: 0px;
    padding-right: 0px;
  }

  .footer-color {
    color: rgba(69,69,69,0.5);
  }

  h5 {
    display: inline;
    margin-right: 8px;
  }

  .icon-container {
    height: 24px;
    width: 24px;
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
  }
</style>