<template>
  <div>
    <app-header></app-header>
    <div class="d-flex justify-content-center bg-pattern" style="padding-top: 80px;">
      <div class="d-flex justify-content-start pb-3" style="width: 75%">
        <h4 class="font-weight-bold">Registration</h4>
      </div>
    </div>
    <div class="alert alert-danger container pl-5 mt-5" role="alert" v-if="error">
      {{ message }}
    </div>
    <div class="container pl-5 mt-5">
      <form class="col-md-5" id="registerForm" method="post" @submit.prevent="register" enctype="multipart\form-data">
        <div class="form-group">
          <label class="font-weight-bold">Firstname</label>
          <input type="text" name="firstname" class="form-control">
        </div>
        <div class="form-group">
          <label class="font-weight-bold">Lastname</label>
          <input type="text" name="lastname" class="form-control">
        </div>
        <div class="form-group">
          <label class="font-weight-bold">Email</label>
          <input type="email" name="email" placeholder="eg. johndoe@test.com" class="form-control">
        </div>
        <div class="form-group">
          <label class="font-weight-bold">Password</label>
          <input type="password" name="password" class="form-control">
        </div>
        <input type="submit" name="register" value="Submit" class="btn btn-primary btn-block font-weight-bold">
      </form>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Register",
    props: [],
    methods: {
    register: function() {
      let self = this;
      let registerForm = document.getElementById('registerForm');
      let registerInfo = new FormData(registerForm);

      fetch("/api/register", {
        method: 'POST',
        body: registerInfo,
        headers: {
          'X-CSRFToken': token
        },
        credentials: 'same-origin'
      })
      .then(function (response) {
        return response.json();
      })
      .then(function (jsonResponse) {
        if (jsonResponse.hasOwnProperty("error")){
          self.error = true;
          self.message = jsonResponse.error;
        }else{
          if(jsonResponse.hasOwnProperty('message')){
            router.push({name: 'login', params: {notifs: jsonResponse.message, success: true}});
          }
        }
      })
      .catch(function (error) {
        console.log(error);
      })
    }
  },
    data: function() {
      return {
        error: false,
        message: ''
      }
    }
  }
</script>