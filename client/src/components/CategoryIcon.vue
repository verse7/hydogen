<template>
    <div @click="filterResources" class="clickable d-flex flex-column justify-content-center align-items-center">
        <div style="background-color: #007bff;"
        class="shadow-sm rounded-circle type-icon d-flex justify-content-center align-items-center text-white">
        <ion-icon :name="icon"></ion-icon>
        </div>
        <small class="text-muted">{{ title }}</small>
    </div>
</template>

<script>
export default {
  name: 'category-icon',
  data: function() {
    return {
      isExtended: false
    }
  },
  props: {
      title: String,
      type: String,
      icon: String

  },
  methods: {
    filterResources: function() {
      const results = this.$store.getters.typeResources(this.type);
      this.$emit('filter-resources', results);
      console.log(results);
    }
  }
};
</script>

<style lang="scss" scoped>

</style>
