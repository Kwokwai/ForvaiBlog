<template>
  <div class="left-main">
    <div class="left-content">
      <div class="cate">
          <div class="article-list" v-for="result in results" :key="result.name">
            <div class="category">
            <router-link :to="'/category/' + result.cid"><span>{{ result.name }}</span></router-link>
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
    this.$api.get('category', null, response => {
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
  .cate {
    height: 100%;
    width: 80%;
    margin: 0 auto;
  }
  .category {
    display: inline-block;
    margin-top: 5%;
    padding: 10px 20px;
    font-size: 25px;
    color: #fff;
    font-family: arial, sans-serif;
    text-decoration: none;
    border-radius: 0.3em;
    position: relative;
    background-color: #ccc;
    background-image: linear-gradient(to top, #6d8aa0, #8ba2b4);
    -webkit-backface-visibility: hidden;
    z-index: 1;
  }
  .category:after {
    position: absolute;
    content: '';
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 0.3em;
    background-image: linear-gradient(to top, #ca5f5e, #d68584);
    transition: opacity 0.5s ease-out;
    z-index: 2;
    opacity: 0;
  }
  .category:hover:after {
    opacity: 1;
  }
  .category span {
    position: relative;
    z-index: 3;
  }
</style>
