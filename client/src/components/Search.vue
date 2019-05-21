<template>
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
          <input type="date" id="startDate" name="startDate" class="form-control" placeholder="Start Date">
        </div>
        <div class="form-group pr-2">
          <label>End Date</label>
          <input type="date" id="endDate" name="endDate" class="form-control" placeholder="End Date">
        </div>
        <div class="form-group d-flex align-items-end">
          <input type="submit" value="Search" class="btn btn-primary">
        </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Search",
  data: function() {
    return {
      countryId: ''
    }
  },
  methods: {
    findCountry() {
      let self = this;
      let country = document.getElementById('country').value;

      fetch('https://api.opencaribbean.org/api/v1/location/countries/search?name='+ country +'&page=0&size=1', {
        method: 'GET'
      })
      .then(function(res) {
        return res.json();
      })
      .then(function (jsonResponse) {
        console.log(jsonResponse)
        self.countryId = jsonResponse.content[0]['id']
      })
      .catch(function(err) {
        console.log(err);
      })
    },
		search() {
			let self = this;
			let startDate =document.getElementById("startDate");
      let endDate =document.getElementById("endDate");
      
			let s = new Date(startDate.value).toISOString();
			let e = new Date(endDate.value).toISOString();
			
			localStorage.setItem('startDate', s);
			localStorage.setItem('endDate', e);
      
      fetch('https://api.opencaribbean.org/api/v1/playtour/resource/page/availables?countryId='+ self.countryId +'&startDate='+ s +'&endDate='+ e +'&onlybookable=true&page=0&size=100', {
        method: 'GET'
      })
      .then(function (response) {
        return response.json();
      })
      .then(function (jsonResponse) {
        console.log(jsonResponse);
				
        //router.push({name:"results", params:{resources: jsonResponse.content}});
        
        localStorage.setItem('resources', JSON.stringify(jsonResponse.content));
        router.push("/results");
      })
      .catch(function (error) {
        console.log(error);
      })
		}
	}
}
</script>
