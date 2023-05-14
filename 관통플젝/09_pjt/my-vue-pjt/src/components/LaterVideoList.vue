<template>
  <div>
    <div v-for="(video, index) in savedVideos" :key="index">
        <iframe 
          width="560"
          height="315"
          :src="'https://www.youtube.com/embed/' + video.videoId"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
        <div>
            <button @click="removeVideo(index)">Remove</button>
        </div>
        
    </div>
  </div>
</template>

<script>
export default {
    data() {
      return {
        savedVideos: [],
      };
    },
    mounted() {
      // 로컬 스토리지에서 저장된 동영상 목록 가져오기
      const savedVideos = JSON.parse(localStorage.getItem('savedVideos')) || [];
      this.savedVideos = savedVideos;
      console.log('dd', this.savedVideos)
    },
    methods: {
      removeVideo(index) {
        // 동영상 목록에서 삭제하기
        this.savedVideos.splice(index, 1);
        // 로컬 스토리지에서도 삭제하기
        localStorage.setItem('savedVideos', JSON.stringify(this.savedVideos));
      },
    },
}
</script>

<style>

</style>