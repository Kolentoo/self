import Vue from 'vue'
import Router from 'vue-router'
import index from '../pages/index'
import tvplay from '../pages/tvplay'
import movies from '../pages/movies'
import anime from '../pages/anime'
import mdetail from '../pages/mdetail'
import person from '../pages/person'
import result from '../pages/result'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/tvplay',
      name: 'tvplay',
      component: tvplay
    },
    {
      path: '/mdetail',
      name: 'mdetail',
      component: mdetail
    },
    {
      path: '/movies',
      name: 'movies',
      component: movies
    },
    {
      path: '/anime',
      name: 'anime',
      component: anime
    },
    {
      path: '/person',
      name: 'person',
      component: person
    },
    {
      path: '/result',
      name: 'result',
      component: result
    }
  ]
})
