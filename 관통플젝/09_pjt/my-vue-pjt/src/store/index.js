import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    Datas: null,
  },
  getters: {
  },
  mutations: {
    SEARCH(state, youtubeData){
      state.Datas = youtubeData
    }
  },
  actions: {
    async search(context, InputData){
      const res = await axios.get('https://www.googleapis.com/youtube/v3/search',
            {
                params: {
                    part: 'snippet',
                    q: `${InputData}`,
                    type: 'video',
                    key: process.env.VUE_APP_YOUTUBE_API_KEY,
                    },
            }                
        )
        const youtubeData = res.data.items

        console.log(youtubeData)
        console.log("유튜브데이터가져옴")
            
        context.commit('SEARCH', youtubeData)
    }
  },
  modules: {
  }
})
