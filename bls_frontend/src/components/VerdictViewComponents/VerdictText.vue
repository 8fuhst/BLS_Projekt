<template>
  <div class="scroll-margin">
    <div :class="[isDivider(prefix) ? 'divider' : 'verdict-text']" @mouseover="setHover(true)" @mouseleave="setHover(false)">
      <HoverMenu v-if="!isDivider(prefix, text) && hover" class="hover-menu" :copy="true" :copyTextId="id" />
      <h5 v-if="hasPrefix">{{ prefix }}</h5>
      <b-card-text v-if="!isDivider(prefix, text)" :id="id" class="text-padding">{{ displayedText }}</b-card-text>
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
    divider: {
      type: Boolean,
    }
  },
  data() {
    return {
      hover: false,
      id: '',
      hasPrefix: true,
      displayedText: '',
    }
  },
  methods: {
    setHover(hover) {
      this.hover = hover
    },
    setProperties() {
      this.displayedText = this.text
      if (!/^[0-9.]+$/.test(this.prefix)) {
        this.displayedText = this.prefix
        this.hasPrefix = this.isDivider(this.prefix)
      }

      if (this.text && this.prefix) {
        const id = 'a' + this.prefix + this.text.substr(0, 10)
        this.id = id.replace(/\s/g, '')
      }
    },
    isDivider(prefix)  {
      return /^[XIV.]+$/.test(prefix) || this.divider
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

  .scroll-margin {
    scroll-margin-top: 66px;
  }
</style>