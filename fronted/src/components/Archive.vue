<template>
    <div class="left-main">
      <div class="left-content">
        <!--<div class="article-list" v-for="result in results" :key="result.title">-->
          <!--<router-link :to="'/article/' + result.aid"><h1>{{ result.title }}</h1></router-link>-->
        <!--</div>-->
      </div>
    </div>
</template>

<script>export default {
  name: 'archive',
  data () {
    return {
      results: []
    }
  },
  created () {
    this.$api.get('archive', null, response => {
      this.results = response.data.list
      console.log(response.data)
    })
  }
}
</script>

<style scoped>
</style>
