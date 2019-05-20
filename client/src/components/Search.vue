<template>
  <div>
    <div class="search-form">
      <p class="font-weight-bold">Search Details Below</p>
      <h4 class="font-weight-bold">Book Your Next Adventure</h4>
      <form class="row pl-3" @submit.prevent="search" method="post">
          <div class="form-group pr-2">
            <label>Country</label>
            <input id="country" type="text" v-on:blur="findCountry" name="country" class="form-control" placeholder="Enter Country">
          </div>
          <div class="form-group pr-2">
            <label>Start Date</label>
            <input type="date" id="startDate" name="startDate" class="form-control"placeholder="Start Date">
          </div>
          <div class="form-group pr-2">
            <label>End Date</label>
            <input type="date" id="endDate" name="endDate" class="form-control"placeholder="End Date">
          </div>
          <div class="form-group d-flex align-items-end">
            <input type="submit" value="Search" class="btn btn-primary">
          </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Search",
  data: function() {
    return {
      countryId: ''
    }
  }
}
</script>
