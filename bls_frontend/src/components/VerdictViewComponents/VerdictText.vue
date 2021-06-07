<template>
  <div>
    <div :class="[isDivider ? 'divider' : 'verdict-text']" @mouseover="setHover(true)" @mouseleave="setHover(false)">
      <HoverMenu v-if="!isDivider && hover" class="hover-menu" :copy="true" :copyTextId="id" />
      <h5 v-if="hasPrefix">{{ prefix }}</h5>
      <b-card-text v-if="!isDivider" :id="id" class="text-padding">{{ text }}</b-card-text>
    </div>
  </div>
</template>

<script>
import HoverMenu from "@/components/UtilityComponents/HoverMenu";

export default {
  name: "VerdictText",
  components: {HoverMenu},
  props: {
    prefix: {
      type: String,
    },
    text: {
      type: String,
    },
  },
  data() {
    return {
      hover: false,
      isDivider: false,
      id: '',
      hasPrefix: true,
    }
  },
  methods: {
    setHover(hover) {
      this.hover = hover
    },
    setProperties() {
      console.log(this.text, this.prefix)
      if (!this.text) {
        this.isDivider = true
      } else {
        this.isDivider = false
      }

      if (this.text && this.prefix) {
        const id = 'a' + this.prefix + this.text.substr(0, 10)
        this.id = id.replace(/\s/g, '')
      }

      this.hasPrefix = this.prefix && this.prefix.length > 0 && this.prefix !== 'noPrefix'
    }
  },
  created() {
    this.setProperties()
  },
  watch: {
    text: function () {
      this.setProperties()
    },
    prefix: function () {
      this.setProperties()
    }
  }
}
</script>

<style scoped>
  .verdict-text {
    padding: 14px 30px;
    position: relative;
  }

  .verdict-text:hover {
    background-color: rgb(187,187,187);
  }

  .text-padding {
    padding: 0px 12px;
  }

  .hover-menu {
    position: absolute;
    top: -8px;
    right: 15px;
  }

  .divider {
    height: 52px;
    width: 100%;
    background-color: rgba(206, 206, 206, 0.5);
    padding: 14px 40px;
  }
</style>