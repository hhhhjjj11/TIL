import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLotto from '../views/TheLotto.vue'
import TheLunch from '../views/TheLunch.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'lunch',
    component: TheLunch,
  },
  {
    path: '/lotto',
    name: 'lotto',
    component: TheLotto,
  },
  {
    path: '/lotto/:count',  //count라는 변수를 받을거다.
    name: 'lotto',
    component: TheLotto,
  },
  // {
  //   path: '/about',
  //   name: 'about',

  //   // 지연 로딩
  //   // 한 번에 받아오는 게 아니라
  //   // 필요할 때 마다 서버로 요청
  //   // 초기 로딩이 빠름
  //   // 서버로 추가적인 요청이 발생
  //   // 예시) 랭킹 시스템
  //   // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),

  //   // 서버로부터 한 번에 다 받아옴
  //   // JS 코드 외의 추가적인
  //   component: AboutView
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
