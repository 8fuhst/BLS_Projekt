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

/**
 * Component for the verdict text entries
 *
 * @param prefix Prefix of the text entry
 * @param text Text of text entry
 * @param indices Describes the indices in this text entry from the data for referencing purposes
 * @param section Describes the section of the text entry
 * @param divider Whether this text entry shall be a divider
 *
 */
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
    indices: {
      type: Array,
    },
    section: {
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
    /**
     * Sets the hover property according to the parameter hover
     *
     * @param hover boolean for whether hover is set or not. True if hover shall be set to true. Else false
     */
    setHover(hover) {
      this.hover = hover
    },
    /**
     * Sets the properties for displayedText, hasPrefix and id according to current value
     */
    setProperties() {
      this.displayedText = this.text
      if (!/^[0-9.]+$/.test(this.prefix)) {
        this.displayedText = this.prefix
        this.hasPrefix = this.isDivider(this.prefix)
      }

      if (this.indices) {
        const id = this.section + this.indices.join('x')
        this.id = id.replace(/\s/g, '')
      }
    },
    /**
     * Determines if a prefix is a divider as defined
     *
     * @param prefix String to check if it defines a prefix
     */
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