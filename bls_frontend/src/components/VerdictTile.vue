<template>
  <div class="card-div">
    <b-card class="border-color">
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
          <b-card-text>{{ verdict.court + ' ' + verdict.spruchkoerper }}</b-card-text>
        </b-row>

        <!-- Gericht/Aktenzeichen row !-->
        <b-row class="bottom-margin">
          <b-col class="al-right entry no-side-padding">
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
    this.norms = norms.join(',   ');
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
    padding: 0px 12px;
  }

  .doc-type-tag {
    display: inline-block;
    height: 54px;
    width: auto;
    border-radius: .25rem;
    padding: 14px 12px;
    border: none;

    background-color: rgba(255, 0, 0, 0.59);
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

  .border-color {
    border-color: rgba(255, 0, 0, 0.5);
  }

  .card-footer {
    border-top: 1px solid rgba(255, 0, 0, 0.2);
  }
</style>