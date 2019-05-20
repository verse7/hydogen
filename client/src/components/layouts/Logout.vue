<template>
  
</template>

<script>
  export default {
    name: "Logout",
    props: [],
    data: function() {
      return {
      }
    },
    created: function(){
      let message;
      localStorage.clear();
      message = "User successfully logged out";
      router.push({name: 'home', params:{notifs: message, success: true}});
    }
  }
</script>