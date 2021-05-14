<template>
  <div class="card-div">
    <b-card>
      <template #header>
        <b-card-text>{{ verdict.court }}</b-card-text>
      </template>

      <b-container>
        <!-- Doctype row !-->
        <b-row class="bottom-margin">
          <b-col class="al-left no-col-padding">
            <div class="doc-type-tag">
              <b-card-text class="doc-type-text">
                {{ verdict.documenttype }}
              </b-card-text>
            </div>
          </b-col>
        </b-row>

        <!-- Gericht/Aktenzeichen row !-->
        <b-row class="bottom-margin">
          <b-col class="al-right entry no-col-padding">
            <DropDownText :items="verdict.filenumber" :id="verdict.documentnumber + 'drop'" />
          </b-col>
        </b-row>



        <!-- Normen row !--> <!-- TODO: Dafür sorgen, dass die collapsables unabhängig offen bleiben !-->
        <b-row class="bottom-margin">
          <ExpandableText :content="norms" :content-brief="normsBrief" :id="verdict.documentnumber + 'exp'" />
        </b-row>


      </b-container>

      <!-- Texte !-->
      <h5>Leitsatz</h5>
      <b-card-text class="text-padding">{{ verdict.keysentence }}</b-card-text>
      <h5>Tenor</h5>
      <b-card-text class="text-padding">{{ verdict.tenor }}</b-card-text>

      <template #footer>
        <!-- Date/Ecli row !-->
        <b-row>
          <b-col class="footer-color">
            <b-card-text>
              {{ verdict.date }}
            </b-card-text>
          </b-col>
          <b-col class="al-right footer-color">
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
    }
  },
  created() {
    const norms = this.verdict.norms.slice(0)
    this.norms = norms.join(', ');
    if (norms.length > 3) {
      this.normsBrief = norms.slice(0, 3).join(', ') + ' ...'
    } else {
      // TODO: Dann auch dafür sorgen, dass das Ding nicht expandable ist
      this.normsBrief = norms.join(', ')
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
    padding: 0px 8px;
  }

  .doc-type-tag {
    display: inline-block;
    height: 54px;
    width: auto;
    cursor: auto !important;
    border-radius: .25rem;
    padding: 14px 12px;

    background-color: rgba(255, 0, 0, 0.59);
  }

  .doc-type-text {
    color: white;
  }

  .bottom-margin {
    margin-bottom: 15px;
  }

  .no-col-padding {
    padding-left: 0px;
    padding-right: 0px;
  }

  .footer-color {
    color: rgba(69,69,69,0.5);
  }
</style>