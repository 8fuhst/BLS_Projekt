<template>
  <div class="longtext">
    <div class="button-group">
      <b-button-group>
        <b-button>Zum Leitsatz</b-button>
        <b-button>Zum Tenor</b-button>
        <b-button>Zur Sachverhaltsdarstellung</b-button>
        <b-button>Zur rechtlichen Bewertung</b-button>
      </b-button-group>
    </div>

    <VerdictDivider :text="'Tenor'"></VerdictDivider>
    <VerdictText :prefix="'1.'" :text="'asdfghasdgf asfiug asdiufgiasgdfiusgadfgisudfg sdfuigsdfguisgdfui suid g usgfugasudgfuigsdf'"></VerdictText>
  </div>
</template>

<script>
import VerdictDivider from "@/components/VerdictViewComponents/VerdictDivider";
import VerdictText from "@/components/VerdictViewComponents/VerdictText";
export default {
  name: "VerdictLongtext",
  components: {VerdictText, VerdictDivider}
}
</script>

<style scoped>
  .longtext {
    display: inline-block;
    width: 62%;
    height: 500px;
    position: relative;
  }

  .button-group {
    position: absolute;
    top: -54px;
    left: 12px;
  }
</style>