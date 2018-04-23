import Vue from 'vue'
import Router from 'vue-router'
import index from '../pages/index'
import alltype from '../pages/alltype'
import mdetail from '../pages/mdetail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/alltype',
      name: 'alltype',
      component: alltype
    },
    {
      path: '/mdetail',
      name: 'mdetail',
      component: mdetail
    }
  ]
})
