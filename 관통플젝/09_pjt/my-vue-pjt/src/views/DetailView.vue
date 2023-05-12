<template>
  <div>
    <div>
        <b-button variant="outline-primary"><router-link :to="{ name: 'home' }">뒤로가기</router-link> </b-button>
    </div>
    <h2>Video Detail</h2>
    <p>Video ID: {{ $route.params.videoId }}</p>
    <!-- video detail 정보 표시 -->
    <h2> {{ $route.params.title }} </h2>
    <h4>{{ $route.params.publishTime }}</h4>
    <div>
      <iframe
        width="560"
        height="315"
        :src="'https://www.youtube.com/embed/' + $route.params.videoId"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
    <h4>{{ $route.params.descripttion }}</h4>

    <button v-if="isSaved" @click="removeFromLocalStorage">저장 취소</button>
    <button v-else @click="saveToLocalStorage">저장</button>
  </div>
</template>

<script>

export default {
    data(){
        return{
            isSaved:false
        }
  },
  methods: {
    saveToLocalStorage() {
        // console.log('save로컬')
      const savedVideos = JSON.parse(localStorage.getItem('savedVideos')) || [];
      savedVideos.push({ videoId: this.$route.params.videoId });
      localStorage.setItem('savedVideos', JSON.stringify(savedVideos));
      this.isSaved=true
    },
    removeFromLocalStorage() {
    //   console.log('remove로컬')
      const savedVideos = JSON.parse(localStorage.getItem('savedVideos')) || [];
      const index = savedVideos.findIndex(video => video.videoId === this.$route.params.videoId);
      savedVideos.splice(index, 1);
      localStorage.setItem('savedVideos', JSON.stringify(savedVideos));
      this.isSaved=false
    }
  }
}



</script>

<style>

</style>