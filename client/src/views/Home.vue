<template>
  <div class="home">
    <Header />
    <ExploreMap/>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import ExploreMap from '@/components/ExploreMap.vue';
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'home',
  components: {
    ExploreMap, Header, Footer
  },
};
</script>
