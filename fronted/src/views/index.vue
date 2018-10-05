<template>
  <div class="index">
    <navbar></navbar>
    <div class="headpic">
      <div class="container headtitle">
        <div class="title">
          <router-link to="about"><h1>怜也</h1></router-link>
        </div>
      </div>
    </div>
    <div class="content">
      <div class="content-list">
        <articles></articles>
        <articles></articles>
        <articles></articles>
        <articles></articles>
        <articles></articles>
        <articles></articles>
        <articles></articles>
      </div>
    </div>
    <scroll-top></scroll-top>
  </div>
</template>

<script>
import Navbar from '@/components/navbar.vue'
import ScrollTop from '@/components/scrollTop'
import Articles from '@/components/article'

export default {
  name: 'index',
  components: {
    Navbar,
    ScrollTop,
    Articles
  }
}
</script>

<style lang="scss">
  .headpic {
    height: 280px;
    background: url(/static/head.jpg) center -52px no-repeat;
    -webkit-background-size: cover;
    background-size: cover;
    position: relative;
  }

  .headtitle {
     top: 100px;
     max-width: 1100px;
     margin: 0 auto;
     padding: 0 50px;
     position: relative;
     font-family: 'Geo', sans-serif;
     font-size: 34px;
     text-shadow: 0 3px 3px #616066;
   }

  .content {
    max-width: 80%;
    margin: 0 auto;
    position: relative;
    &-list {
      width: 100%!important;
      float: left;
      margin-top: -50px;
      -webkit-transition: all .5s ease-out;
      transition: all .5s ease-out;
    }
  }
</style>
