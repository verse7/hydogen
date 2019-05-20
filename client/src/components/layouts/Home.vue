<template>
  <div>
    <app-header></app-header>
    <div class="bg-pattern mb-4">
      <div role="alert" v-if='success' style="padding: 50px 0 0 80px;">
        <div class="alert alert-success col-md-7">
          {{ notifs }}
        </div>
      </div>
      <search></search>
    </div>
    <div class="container">
      <default-listing title="Hotels" type="HOTEL"></default-listing>
      <default-listing title="Motels" type="MOTEL"></default-listing>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Home",
    props: ['notifs', 'success'],
    data: function() {
      return {

      }
    }
  }
</script>