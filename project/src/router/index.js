import Vue from 'vue'
import Router from 'vue-router'
import index from '../pages/index'
import anime from '../pages/anime'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/anime',
      name: 'anime',
      component: anime
    }
  ]
})
