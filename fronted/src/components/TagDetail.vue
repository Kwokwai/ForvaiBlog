<template>
  <div class="left-main">
    <div class="left-content">
        <div class="tag-title">
          <h1>{{ name }}</h1>
        </div>
        <div class="article-list" v-for="article in articles" :key="article.title">
        <router-link :to="'/article/' + article.aid">
          <div class="card">
            <div class="card-date">
              {{ article.createYear}}
              <div class="date-line"></div>
              {{ article.createDate }}
            </div>
            <div class="card-category">
              <div id="article_category" v-for="cate in article.category">
                <router-link :to="'/category/' + cate.cid">{{ cate.name }}</router-link>
              </div>
            </div>
            <div class="card-title" id="article_title">
              <router-link :to="'/article/' + article.aid"><p id="main_titile">{{ article.title }}</p></router-link>
            </div>
            <div class="card-line"></div>
            <div class="card-summery" id="article_summery">
              <p>{{ article.summery }}</p>
            </div>
          </div>
        </router-link>
      </div>
      </div>
      </div>
  </div>
</template>
<script>export default {
  name: 'tag',
  data () {
    return {
      articles: {},
      name: {}
    }
  },
  created () {
    let id = this.$route.params.id
    this.$api.get('tag/' + id, null, response => {
      this.articles = response.data.articlelist
      this.name = response.data.name
      console.log(response.data)
    })
  }
}
</script>

<style scoped>
  #article_title {
    font-size: 20px;
    color: #555;
    padding-top: 15px;
  }
  .tag-title{
    border-radius: 20px;
    border: 1px solid;
    width: 15%;
    text-align: center;
    margin: 40px;
    background: #ffaee2;
    color: #e6ffea;
  }
</style>
