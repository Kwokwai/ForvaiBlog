<template>
  <div class="category">
    <navbar></navbar>
    <scroll-top></scroll-top>
  </div>
</template>

<script>
import Navbar from '@/components/navbar.vue'
import scrollTop from '@/components/scrollTop'

export default {
  name: 'category',
  components: {
    Navbar,
    scrollTop
  }
}
</script>

<style>
</style>
