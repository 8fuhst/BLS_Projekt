<template>
  <div>
    <div v-if="!isDivider" class="verdict-text" @mouseover="setHover(true)" @mouseleave="setHover(false)">
      <HoverMenu class="hover-menu" :copy="true" :copyTextId="id" v-if="hover"/>
      <h5 v-if="hasPrefix">{{ prefix }}</h5>
      <b-card-text :id="id" class="text-padding">{{ text }}</b-card-text>
    </div>
    <div v-if="isDivider" class="divider">
      <h5>{{ prefix }}</h5>
    </div>
  </div>
</template>

<script>
import HoverMenu from "@/components/UtilityComponents/HoverMenu";

export default {
  name: "VerdictText",
  components: {HoverMenu},
  props: {
    prefix: String,
    text: String,
  },
  data() {
    return {
      hover: false,
      isDivider: false,
      id: '',
    }
  },
  methods: {
    setHover(hover) {
      this.hover = hover
    },
    hasPrefix() {
      if (this.prefix === 'noPrefix') {
        console.log('askdhjf')
        return false
      }
      return this.prefix && this.prefix.length > 0
    }
  },
  created() {
    if (!this.text) {
      this.isDivider = true
    }

    if (this.text && this.prefix) {
      const id = 'a' + this.prefix + this.text.substr(0, 10)
      this.id = id.replace(/\s/g, '')
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