<template>
    <footer id="navCentre"
    class="fixed-bottom bg-white rounded-top-xtra 
          shadow-sm nav-centre d-flex flex-column 
          align-items-center">
    <div @click="extendNavCentre" class="clickable notch mt-2"></div>
    <div class="container pt-3 pl-3 pr-3 d-flex flex-row justify-content-between align-items-center overflow-x-scroll">
        <category-icon title="Stays" type="Accomodation" icon="business"></category-icon>
        <category-icon title="Attractions" type="Attraction" icon="paper"></category-icon>
        <category-icon title="Services" type="Services" icon="build"></category-icon>
        <category-icon title="More" type="More" icon="code-working"></category-icon>
    </div>
  </footer>
</template>

<script>
import CategoryIcon from '@/components/CategoryIcon.vue'

export default {
  name: 'map-footer',
  data: function() {
    return {
      isExtended: false
    }
  },
  methods: {
    extendNavCentre: function() {
    }
  },
  components: {
      CategoryIcon
  }
};
</script>

<style lang="scss" scoped>

</style>
