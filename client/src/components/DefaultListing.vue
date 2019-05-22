<template>
  <section class="mb-4">
    <h1 class="font-weight-bold section-title">{{ title }}</h1>
    <div class="scrolling-wrapper">
      <resource-card v-for="resource in resources" :resource="resource" :key="resource.id"></resource-card>
    </div>
  </section>
</template>

<script>
import ResourceCard from './ResourceCard.vue';

  export default {
    name: "DefaultListing",
    props: ['title', 'type'],
    components: {ResourceCard},
    data: function() {
      return {
        resources: []
      }
    },
    created: function() {
      let self = this;

      fetch('https://api.opencaribbean.org/api/v1/playtour/resource/search?query=' + self.type, {
        method: 'GET',
        credentials: 'same-origin'
      })
      .then(res => {
        return res.json()
      })
      .then(data => {
        console.log(data);
        self.resources = data;
      })
    }
  }
  
</script>
