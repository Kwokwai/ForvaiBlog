<template>
  <div class="history">
    <navbar></navbar>
    <scroll-top></scroll-top>
  </div>
</template>

<script>
import Navbar from '@/components/navbar.vue'
import scrollTop from '@/components/scrollTop'

export default {
  name: 'history',
  components: {
    Navbar,
    scrollTop
  }
}
</script>

<style>
</style>
