<template>
  <div>
    <div class="card mb-3 pl-5 pr-5 bg-pattern" style="width: 100%;">
      <div class="row no-gutters" style="padding: 80px 0 0 20px;">
        <div class="col-md-4 pb-5">
          <img :src="'https://api.opencaribbean.org/api/v1/media/download/' + resource.mainImage" class="card-img" alt="Image of resource"
          style="width: 90%; height: 100%;">
        </div>
        <div class="col-md-8 pb-5">
          <div class="card-body no-padding">
            <h5 class="card-title">{{ resource.name }}</h5>
            <p class="card-text">{{ resource.street }}</p>
            <p class="card-text">{{ resource.community }}, {{ resource.state }}</p>
            <p class="card-text">{{ resource.email }}</p>
            <p class="card-text">{{ resource.country.name }}</p>
            <p class="card-text"><small class="text-muted">Last updated {{ resource.updatedAt }}</small></p>
          </div>
        </div>
        <p class="card-text">{{ resource.description }}</p>

        <!-- BOOKING LIST HERE -->
        <div class="form pb-3">
          <label for="book-sel">Select Booking Period: </label>
          <select class="form-control" id="book-sel" v-model="selBooking">
            <option v-for="bookable in bookables" :value="bookable" :key="bookable">{{ new Date(bookable.dateStart).toUTCString() }} --> {{ new Date(bookable.dateEnd).toUTCString() }}</option>
          </select> 
        </div>
        <br>
         <button @click="bookStay" style="display:block;" class="btn btn-dark btn-size pl-5 mb-4 d-flex align-items-center" type="submit" data-dismiss="modal">Book</button>
      </div>
    </div>
    <div class="container">
      <ul class="row list-inline">
        <li class="col-sm-4" v-for="photo in resource.images" :key="photo">
          <div class="card-body">
            <img :src="'https://api.opencaribbean.org/api/v1/media/download/' + photo" alt="Additional Images of the resource" 
            class="img-fluid card-img-top">
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "resourceDetails",
  props: {
    resource: {
      type: Object,
      required: true
    }
  },
  data() {
    return{
      bookables: [],
      selBooking: null
    }
  },
  methods: {
    bookStay: function() {

			let booked = [];
			booked.push(this.resource);
			if (localStorage.getItem('booked') != null) {
				resourceArr = JSON.parse(localStorage.getItem('booked'));
				resourceArr.push(this.resource);
				localStorage.setItem('booked', JSON.stringify(resourceArr));
			} else {
				booked.push(this.resource);
				localStorage.setItem('booked', JSON.stringify(booked));
			}


		if(localStorage.getItem('current_user') !== null){
			let bookingForm = new FormData();
			bookingForm.append("bookableId", this.resource.bookeableList[0].bookableId);
			bookingForm.append("dateend", localStorage.endDate);
			bookingForm.append("datestart", localStorage.startDate);
			bookingForm.append("idapp", this.resource.appId);
			bookingForm.append("idresource", this.resource.id);
			bookingForm.append("iduser", localStorage.getItem('current_user'));
			bookingForm.append("status", "CREATED");


			fetch('https://api.opencaribbean.org/api/v1/booking/bookings', {
					method: 'POST', 
					body: bookingForm,
					headers: {
						'X-CSRFToken': token,
						'content-type': 'application/json;charset=UTF-8',
					},
					credentials: 'same-origin'
			})
			.then(res => res.json())
			.then(jsonResp => {
					console.log(jsonResp);
			});
        
		}else{
			alert("Must select a booking time from list before booking " + this.resource.type);
			router.push('login');
		}
    }
  },
  created: function(){
		this.bookables = this.resource.bookeableList;
		console.log(this.bookables);
	} 
}
</script>
