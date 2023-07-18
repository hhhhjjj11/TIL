import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter:0,
  },
  getters: {
    //getters사용해보기
    getPlusCounter(state){
      console.log('getters호출!')
      // 가능은 하다! 
      state.counter += 10
      return state.counter
    }
  },
  mutations: {
    PLUS(state, counter){
      console.log(counter)
      state.counter ++
    },
    MINUS(state, counter){
      console.log(counter)
      state.counter --
    }
  },
  actions: {
    plus(context, counter){
      context.commit('PLUS', counter)
    },
    minus(context, counter){
      context.commit('MINUS', counter)
    }
  },
  modules: {
  }
})
