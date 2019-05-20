<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
body {
  padding: 0;
  margin: 0;
}

.text-small {
    font-size: 14px; 
}

.rounded-top-xtra {
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
}

.type-icon {
  width: 40px;
  height: 40px;
  background-color: #ececec;
}

.shadow-sm {
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}

.nav-centre {
    height: 100px;
    transition: all 0.2s ease-in-out;
}

.notch {
    height: 6px;
    width: 40px;
    border-radius: 15px;
    background-color: rgba(0, 0, 0, 0.15)
}

#mainNav {
    transition: all 0.2s ease-in-out;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
