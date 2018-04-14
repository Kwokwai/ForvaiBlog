// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import Home from './components/Home'
import Archive from './components/Archive'
import Category from './components/Category'
import Tag from './components/Tag'
import api from './api/index'
import Article from './components/Aritcle'
import CategoryDetail from './components/CategoryDetal'
import TagDetail from './components/TagDetail'

Vue.use(VueRouter)
Vue.prototype.$api = api
const routes = [
  {
    path: '/',
    component: Home
  }, {
    path: '/archive',
    component: Archive
  }, {
    path: '/category',
    component: Category
  }, {
    path: '/category/:id',
    component: CategoryDetail
  }, {
    path: '/tag',
    component: Tag
  }, {
    path: '/tag/:id',
    component: TagDetail
  }, {
    path: '/article/:id',
    component: Article
  }, {
    path: 'article',
    component: Article
  }
]
const router = new VueRouter({
  mode: 'history',
  routes
})

new Vue({
  router,
  ...App
}).$mount('#app')
