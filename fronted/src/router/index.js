import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/views/index'
import History from '@/views/history'
import Category from '@/views/category'
import About from '@/views/about'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/history',
      name: 'History',
      component: History
    },
    {
      path: '/category',
      name: 'Category',
      component: Category
    },
    {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})
