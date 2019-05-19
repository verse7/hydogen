<template>
  <div id="map"></div>
</template>

<script>
export default {
  name: 'Map',
  data: function() {
    return {
      map: null
    }
  },
  mounted: function() {
    const mapboxgl = require('mapbox-gl/dist/mapbox-gl.js');
 
    mapboxgl.accessToken = 'pk.eyJ1IjoiemRtd2kiLCJhIjoiY2l6a3EyOW1wMDAzbjJ3cHB2aHQ5a2N1eCJ9.xOIXUuzA4pJt7cLIR-wUSg';
    this.map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11'
    });
  }
};
</script>

<style lang="scss" scoped>
  #map {
    height: 100vh;
  }
</style>
