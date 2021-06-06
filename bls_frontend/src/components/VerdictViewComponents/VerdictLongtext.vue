<template>
  <div class="longtext">
    <div class="button-group">
      <b-button-group>
        <b-button>Zum Leitsatz</b-button>
        <b-button href="#tenor">Zum Tenor</b-button>
        <b-button href="#sachverhalt">Zur Sachverhaltsdarstellung</b-button>
        <b-button href="#bewertung">Zur rechtlichen Bewertung</b-button>
      </b-button-group>
    </div>

    <verdictText id="tenor" :prefix="'Tenor'"/>
    <verdictText :prefix="'noPrefix'" :text="tenor"/>
    <verdictText id="sachverhalt" :prefix="'Sachverhaltsdarstellung'"/>
    <VerdictText v-for="reason in offense" v-bind:key="reason.id" :prefix="reason.prefix" :text="reason.text" />
    <verdictText id="bewertung" :prefix="'Rechtliche Bewertung'"/>
    <VerdictText v-for="reason in reasonsForDecision" v-bind:key="reason.id" :prefix="reason.prefix" :text="reason.text" />
  </div>
</template>

<script>
import VerdictText from "@/components/VerdictViewComponents/VerdictText";

export default {
  name: "VerdictLongtext",
  components: {VerdictText},
  props: {
    tenor: String,
    offense: Array,
    reasonsForDecision: Array,
  },
}
</script>

<style scoped>
  .longtext {
    display: inline-block;
    width: 62%;
    position: relative;
  }

  .button-group {
    position: absolute;
    top: -54px;
    left: 12px;
  }
</style>