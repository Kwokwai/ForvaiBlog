import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/views/index'
import History from '@/views/history'
import Category from '@/views/category'
import About from '@/views/about'
import Article from '@/views/article'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: resolve => require(['@/views/index'], resolve)
    },
    {
      path: '/article',
      name: 'Article',
      component: resolve => require(['@/views/article'], resolve)
    },
    {
      path: '/history',
      name: 'History',
      component: resolve => require(['@/views/history'], resolve)
    },
    {
      path: '/category',
      name: 'Category',
      component: resolve => require(['@/views/category'], resolve)
    },
    {
      path: '/about',
      name: 'About',
      component: resolve => require(['@/views/about'], resolve)
    },
    {
      path: '/todo',
      name: 'Todo',
      component: resolve => require(['@/views/todo'], resolve)
    }
  ]
})

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'Index',
//       component: Index
//     },
//     {
//       path: '/article',
//       name: 'Article',
//       component: Article
//     },
//     {
//       path: '/history',
//       name: 'History',
//       component: History
//     },
//     {
//       path: '/category',
//       name: 'Category',
//       component: Category
//     },
//     {
//       path: '/about',
//       name: 'About',
//       component: About
//     }
//   ]
// })
