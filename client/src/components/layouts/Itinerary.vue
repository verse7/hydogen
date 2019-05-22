<template>
  <div>
		<app-header></app-header>

		<div class="mt-5 container">
			<h2 class="mb-2">My Itinerary</h2>
			<ul class="list-group" v-if="bookings.length">
				<li v-for="booking in bookings" class="list-group-item" :key="booking">{{booking.name}}</li>
			</ul>
		</div>
	</div>
</template>

<script>
import AppHeader from '../AppHeader.vue';

export default {
  name: "Itinerary",
  components: {
    AppHeader
  },
  data() {
    return {
      bookings: []
    }
  },
  created() {
		this.bookings = JSON.parse(localStorage.getItem('booked'));



    // fetch('http://api.opencaribbean.org/api/v1/booking/bookings/history?iduser=' + localStorage.current_user)
			// .then( resp => resp.json()).then(jsonResp => {
			// 	this.bookings = jsonResp.content;
			// });

			// this.bookings.forEach(b => {
			// 	fetch(`http://api.opencaribbean.org/api/v1/playtour/resource/${b.idresource}`)
			// 	.then( resp => resp.json()).then(jsonResp => {
			// 		console.log(`supposed resources ${jsonResp.content}`);
			// 		b.name = jsonResp.content.name;
			// 	});
			// }) ;
  }
}
</script>
