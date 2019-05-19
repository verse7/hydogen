<template>
  <nav id="mainNav" class="navbar navbar-expand-md navbar-light bg-transparent fixed-top">
      <router-link class="navbar-brand title-font" to="/">DevCa</router-link>
    
      <button @click="extendNav" class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link class="nav-link" to="/">Home <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/explore">Explore</router-link>
          </li>
          <li class="nav-item" v-if="!logged">
            <router-link class="nav-link" to="/register">Register</router-link>
          </li>
          <li class="nav-item" v-if="!logged">
            <router-link class="nav-link" to="/login">Login</router-link>
          </li>
          <li class="nav-item" v-if="logged">
            <router-link class="nav-link" to="/calendar">Calendar</router-link>
          </li>
          <li class="nav-item" v-if="logged">
            <router-link class="nav-link" to="/itinerary">Itinerary</router-link>
          </li>
          <li class="nav-item" v-if="logged">
            <router-link class="nav-link" to="/logout">Logout</router-link>
          </li>
        </ul>
      </div>
    </nav>
</template>

<script>
  export default {
    name: 'AddHeader',
    data: function() {
      return {
        logged: false,
        isCollapsed: true
      }
    },
    created: function() {
      this.logged = localStorage.getItem('current_user') !== null;
    },
    methods: {
      extendNav: function() {
        const nav = document.getElementById('mainNav');

        this.isCollapsed = !this.isCollapsed;

        nav.classList.toggle('bg-transparent');
        nav.classList.toggle('bg-white');
      }
    } 
  }
</script>



