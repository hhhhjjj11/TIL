<template>
    <div>
        <div>
            <b-button variant="outline-primary"><router-link :to="{ name: 'home' }">뒤로가기</router-link> </b-button>
        </div>
      <h2>Saved Videos</h2>
        <LaterVideoList/>


      <!-- <ul>
        <li v-for="(video, index) in savedVideos" :key="index">
          <router-link :to="{ name: 'detail', params: { videoId: video.id } }">{{ video.title }}</router-link>
          <button @click="removeVideo(index)">Remove</button>
        </li>
      </ul> -->
    </div>
  </template>
  
  <script>
  import LaterVideoList from '@/components/LaterVideoList'

  export default {
    components:{
        LaterVideoList
    }
  };
  </script>
  