import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

const API_URL="http://127.0.0.1:8000"

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    articles: [
      {
        id: 1,
        title: '제목',
        content: '내용'
      },
      {
        id: 2,
        title: '제목2',
        content: '내용2'
      },
    ],
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles){
      state.articles = articles 
    }
  },
  actions: {
    getArticles(context){
      // context.commit() // 커밋할 필요 없음 state를 바꿀 필요가 없기 때문에
      // api로 데이터 불러올때는 actions에서 axios쓴다.
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
        .then((res)=>{
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  },
  modules: {
  }
})
