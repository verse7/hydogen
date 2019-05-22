<template>
  <div>
    <app-header></app-header>
    <div class="bg-pattern">
      <div style="padding: 80px 0 30px 80px;">
        <p class="font-weight-bold"> Search Results Below </p>
        <h4 class="font-weight-bold"> Avaible Bookings: {{ start }} - {{ end }} </h4>
      </div>
    </div>
    <div class="container mt-4">
      <div class="card shadow-sm p-4 mb-5 rounded" v-for="category in Object.entries(filteredItems)" :key="category"> 
        <h4 class="font-weight-bold">{{ category[0] }}</h4>
        <div v-if="category[1].length" class="scrolling-wrapper pt-3">
          <a v-for="resource in category[1]" :key="resource" data-toggle="modal" href="#myModal" @click="select(resource, $event)">
            <resource-card :resource="resource" :key="resource.id" v-on:click="select(resource)"></resource-card>
          </a>
        </div>
        <div v-else>
          No results
        </div>
      </div>     
    </div>

    <div class="modal fade" id="myModal" v-if="selectedResource !== null">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
          </div>
          <div class="model-body">
            <resource-details :resource="selectedResource"></resource-details>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ResourceCard from './ResourceCard.vue';
import AppHeader from './AppHeader.vue';
import ResourceDetails from './ResourceDetails.vue';

export default {
  name: "ResourcePicker",
  components: {
    ResourceCard,
    ResourceDetails,
    AppHeader
  },
  data() {
    return {
      filteredItems: {Accommodation: [], Attraction: [], Service: [], Tour: [], Event: [], Transportation_Operators: []},
			empty: false,
      selectedResource: null,
      start: '',
      end: '',
    }
  },
  methods: {
		select: function(res, event) {
			console.log('select function called');
			event.preventDefault();
			console.log(res);
			this.selectedResource = res;
			event.returnValue = true;
		}
  },
  created: function(){
    let self = this;
    let resources = JSON.parse(localStorage.getItem('resources'));	
		resources.forEach(element => {
			if(self.filteredItems[element['__type']] != null){
				self.filteredItems[element['__type']].push(element)
			}
    });
    let s = (localStorage.getItem('startDate')).split(/\D+/);
    let e = (localStorage.getItem('endDate')).split(/\D+/);
    s = new Date(Date.UTC(s[0], --s[1], s[2], s[3], s[4], s[5], s[6]));
    e = new Date(Date.UTC(e[0], --e[1], e[2], e[3], e[4], e[5], e[6]));
    this.start = self.months[s.getMonth()]+" "+(s.getDate()+1)+", "+s.getFullYear();
    this.end = self.months[e.getMonth()]+" "+(e.getDate()+1)+", "+e.getFullYear();
  }
}
</script>

<style scoped>
  .card {
    width: 100%
  }
</style>

