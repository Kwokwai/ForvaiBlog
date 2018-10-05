<template>
  <div class="about">
    <navbar></navbar>
    <scroll-top></scroll-top>
  </div>
</template>

<script>
import Navbar from '@/components/navbar.vue'
import scrollTop from '@/components/scrollTop'

export default {
  name: 'about',
  components: {
    Navbar,
    scrollTop
  }
}
</script>

<style>
</style>
