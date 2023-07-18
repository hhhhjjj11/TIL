<template>
  <div id="app">
    <div>
      <b-nav>
        <b-nav-item active><router-link :to="{ name: 'home' }">Home</router-link></b-nav-item>
        <b-nav-item><router-link :to="{ name: 'search' }">search</router-link></b-nav-item>
        <b-nav-item><router-link :to="{ name: 'later' }">later</router-link></b-nav-item>
        <b-nav-item><router-link :to="{ name: 'detail' }">detail</router-link></b-nav-item>
      </b-nav>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
