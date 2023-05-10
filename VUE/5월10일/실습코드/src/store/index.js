import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    users: [
      {
        id: 'admin',
        pw: '1234',
        isAdmin: true,
      },
      {
        id: 'test',
        pw: 'test',
        isAdmin: false
      }
    ],
    loginUser: {}
  },
  getters: {
    isLoggedIn(state) {
      // state 의 loginUser 가 비어있다면 false / 아니라면 true 반환
      return Object.keys(state.loginUser).length === 0 ? false : true
    },
  },
  mutations: {
    LOGIN(state, user) {
      state.loginUser = user
    }
  },
  actions: {
    login(context, form) {
      // state.users 에 form.id 와 같은 유저가 있는가 ?
      // 없다면 -> 그런 사용자는 없다 !
      const user = context.state.users.find((user) => user.id === form.id)
      if(!user) { 
        // alert('그런 사용자는 없습니다!')
        return Promise.reject('그런 사용자는 없습니다!')
      }

      // 해당 유저의 pw 가 form.pw 와 같은가 ?
      // 틀렸다면 -> 비밀 번호가 틀렸다 !
      if(user.pw !== form.pw) {
        // alert('비밀번호가 틀렸습니다!')
        return Promise.reject('비밀번호가 틀렸습니다!')
      }

      // 모두 통과했다면, loginUser 업데이트
      context.commit('LOGIN', user)
    }
  },
  modules: {
  }
})
