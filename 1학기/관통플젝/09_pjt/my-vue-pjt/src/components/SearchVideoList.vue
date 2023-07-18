<template>
  <div>
        <!-- 영상목록  -->
        <div>
    <h4>검색결과</h4>
    <div class="row">
  <b-card v-for="data in Datas" :key="data.id.videoId"
    no-body
    style="max-width: 20rem;"
    :img-src="`${data.snippet.thumbnails.default.url}`"
    img-alt="Image"
    img-top
    class="col-md-4 mb-4"
  >

    <b-card-body>
      <b-card-text>
        {{ data.snippet.title }}
      </b-card-text>
    </b-card-body>

    <b-card-body>
        <router-link :to="{ name: 'detail', params: { videoId: data.id.videoId, title: data.snippet.title, descripttion:data.snippet.description, publishTime:data.snippet.publishTime }}">
  보러가기
</router-link>
    </b-card-body>

  </b-card>
    </div>

</div>
  </div>
</template>

<script>
export default {
    computed:{
        Datas(){
            return this.$store.state.Datas
        }
    }
}
</script>

<style>

</style>