<template>
  <div class="shadow-sm bg-white d-sm-block d-md-none py-3 fixed-bottom">
    <ul class="d-flex flex-row justify-content-around align-items-center text-center">
      <li>
        <router-link to="/">
          <ion-icon class="text-dark tab-icon" name="home"></ion-icon>
        </router-link>
      </li>
      <li>
        <router-link to="/events/create">
          <ion-icon class="text-dark tab-icon" name="add"></ion-icon>
        </router-link>
      </li>
      <li>
        <router-link to="/events/popular">
          <ion-icon class="text-dark tab-icon" name="pulse"></ion-icon>
        </router-link>
      </li>
      <li>
        <router-link to="/itinerary">
          <ion-icon class="text-dark tab-icon" name="person"></ion-icon>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "AppFooter",

}
</script>
