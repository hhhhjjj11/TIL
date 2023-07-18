<template>
  <div id="app">
    <h1>SSAFY TUBE</h1>
    <div>
      <iframe
        width="560"
        height="315"
        :src="videoUrl"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      video: null,
    };
  },
  computed:{
    Id() {
      return this.video ? this.video.id.videoId : null;
    },
    videoUrl(){
      return `https://www.youtube.com/embed/${this.Id}`
    }
  },
  async created(){
    const { data } = await axios.get(
      'https://www.googleapis.com/youtube/v3/search',
      {
        params: {
          part: 'snippet',
          q: '코딩노래',
          type: 'video',
          key: process.env.VUE_APP_YOUTUBE_API_KEY,
        },
      }
    );
    this.video = data.items[0];
  },
};
</script>


<!-- 코드를 보면 axios.get 메소드는 Promise를 반환하기 때문에, created 훅에서 비동기 작업을 수행할 때 Promise를 처리하기 위한 then 메소드를 사용해야 합니다. 그러나 현재 코드에서는 this.video를 then 메소드 내부에서 할당하고 있으므로, created 훅이 끝나기 전에 this.video가 아직 할당되지 않습니다.

해결 방법은 async/await를 사용하여 비동기 작업을 처리하고, created 훅에서 async 키워드를 사용하고 axios.get 메소드 앞에 await 키워드를 추가해야 합니다. 이렇게 하면 Promise가 완료될 때까지 created 훅이 끝나지 않고 기다립니다.

다음은 수정된 코드입니다. -->