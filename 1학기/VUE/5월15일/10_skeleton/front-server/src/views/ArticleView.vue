<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
    <ArticleList />
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin //로그인 여부 
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if(this.isLogin){
        this.$store.dispatch('getArticles')   // 로그인 되어있으면 dispatch작동 ㄱ
      }else{
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({name: 'LoginView'}) // 로그인 페이지로 이동..
      }
    }
  }
}
</script>

<style>

</style>
