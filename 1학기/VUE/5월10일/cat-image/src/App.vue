<template>
  <div id="app">
    <h1>CatImage</h1>
    <img :src="url" alt="">
    <div>
      <button @click="newCat">GetCat</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data(){
    return {
      url:null,
    }
  },
  async created(){
    const data = await axios.get(
      'https://api.thecatapi.com/v1/images/search',
    );
    console.log(data.data[0].url)
    this.url = data.data[0].url
  },
  methods:{
    async newCat(){
      const data = await axios.get(
      'https://api.thecatapi.com/v1/images/search',
    );
    console.log(data.data[0].url)
    this.url = data.data[0].url
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
