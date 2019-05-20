<template>
  <div>
    <app-header></app-header>
    <div class="d-flex justify-content-center bg-pattern" style="padding-top: 80px;">
      <div class="d-flex justify-content-start pb-3" style="width: 75%">
        <h4 class="font-weight-bold">Login</h4>
      </div>
    </div>
    <div class="alert alert-danger container pl-5 mt-5" role="alert" v-if='error'>
      {{ message }}
    </div>
    <div v-else>
      <div class="alert alert-success container pl-5 mt-5" role="alert" v-if='success'>
        {{ notifs }}
      </div>
    </div>
    <div class="container pl-5 mt-5">
      <form class="col-md-5" id="registerForm" id="loginForm" method="post" @submit.prevent="login">
        <div class="form-group">
          <label class="font-weight-bold">Email</label>
          <input type="email" class="form-control" name="email" placeholder="johndoe@test.com">
        </div>
        <div class="form-group">
          <label class="font-weight-bold">Password</label>
          <input type="password" class="form-control" name="password">
        </div>
        <input type="submit" value="Login" class="btn btn-primary btn-block font-weight-bold">
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  props: ['notifs', 'success'],
  data: function() {
    return {
      error: false,
      message: ''
    }
  },
  methods: {
    login: function() {
      let self = this;
      let loginForm = document.getElementById('loginForm');
      let loginInfo = new FormData(loginForm);

      fetch("/api/auth/login", {
        method: 'Post',
        body: loginInfo,
        headers: {
          'X-CSRFToken': token
        },
        credentials: 'same-origin'
      })
      .then(function (response){
        return response.json();
      })
      .then(function (jsonResponse){
        console.log(jsonResponse);
        if(jsonResponse.hasOwnProperty('token')){
          let jwt_token = jsonResponse.token;
          let id = jsonResponse.user_id;

          /*Stores the jwt locally to be accessed later*/
          localStorage.setItem('token', jwt_token);
          localStorage.setItem('current_user', id);

          router.push('/');
        }else{
          self.error = true;
          self.message = jsonResponse.error;
        }
      })
      .catch(function (error){
        console.log(error);
      })
    }
  }
}
</script>
