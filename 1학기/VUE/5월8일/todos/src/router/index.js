import Vue from 'vue'
import VueRouter from 'vue-router'

import todoAll from '../components/TodoPage/todoAll'
import todoImportant from '../components/TodoPage/todoImportant'
import todoToday from '../components/TodoPage/todoToday'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'all-todo',
    component: todoAll
  },{
    path: '/important',
    name: 'important-todo',
    component: todoImportant
  },{
    path: '/today',
    name: 'today-todo',
    component: todoToday
  },
]


const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  export default router
  