<template>
<nav class="navbar navbar-expand-lg navbar-light bg-transparent fixed-top">
    <div class="input-group shadow-sm text-small">
        <input type="text" v-model="searchTerm"
        class="form-control text-small" placeholder="Search Treasure Beach...">
        <div class="input-group-append">
        <button @click="searchResources" class="btn btn-primary text-center d-flex justify-content-center align-items-center" type="button">
            <ion-icon name="search"></ion-icon>
        </button>
        </div>
    </div>
</nav>
</template>

<script>
export default {
  name: 'map-header',
  data: function() {
    return {
      searchTerm: ''
    }
  },
  methods: {
      searchResources: function() {
          console.log(this.searchTerm);
      }
  }
};
</script>

<style lang="scss" scoped>

</style>
