<template>
  <div class="left-main">
    <div class="left-content">
      <div class="article-list" v-for="result in results" :key="result.name">
        <div class="tag-cloud">
          <div class="tag">
            <router-link :to="'/tag/' + result.tid">{{ result.name }}</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>export default {
  data () {
    return {
      results: []
    }
  },
  created () {
    this.$api.get('tag', null, response => {
      if (response.status >= 200 && response.status < 300) {
        this.results = response.data.list
        console.log(response.data)
      } else {
        console.log(response.message)
      }
    })
  }
}
</script>

<style scoped>
  .tag-cloud {
    line-height: 1.5em;
    list-style: none;
    text-align: center;
    padding-left: 150px;
  }
  .tag {
    border-radius: 20px;
    display: inline-block;
    background: #b4c7ff;
    float: left;
    margin-left: 20px;
    width: 10%;
    text-align: center;
    box-shadow: 2px 4px 6px #ffaee2;
  }
</style>
