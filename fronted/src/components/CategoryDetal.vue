<template>
  <div class="left-main">
    <div class="left-content">
        <div class="card-title" id="cate-title">
          <h1>{{ name }}</h1>
        </div>
      <div class="article-list" v-for="article in articles" :key="article.title">
        <router-link :to="'/article/' + article.aid">
          <div class="card" id="cate-detail">
            <div class="cate-date">
              {{ article.createYear}}
              <div class="cate-line"></div>
              {{ article.createDate }}
            </div>
            <div class="card-title" id="article_title">
              <router-link :to="'/article/' + article.aid">
                <p id="main_titile">{{ article.title }}</p></router-link>
            </div>
            <!--<div class="card-line"></div>-->
            <!--<div class="card-summery" id="article_summery">-->
              <!--<p>{{ article.summery }}</p>-->
            <!--</div>-->
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>export default {
  name: 'category',
  data () {
    return {
      articles: {},
      name: {}
    }
  },
  created () {
    let id = this.$route.params.id
    this.$api.get('category/' + id, null, response => {
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
    /*color: #555;*/
  }
  #cate-detail {
    min-height: 100%;
  }
  #cate-title {
    color: grey;
    height: 100%;
    width: 20%;
    margin: 30px;
    background: #ffaee2;
    box-shadow: 0 0 5px 3px rgba(255, 174, 226, 0.5);
  }
  .cate-date {
    background-color: #ebffd1;
    box-shadow: 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.2), 0 1px 5px 0 rgba(0,0,0,.12);
    position: absolute;
    top: -20px;
    left: -30px;
    height: 50px;
    width: 50px;
    padding-top: 10px;
    border-radius: 100px;
    color: #ff59d0;
    text-align: center;
    line-height: 1.1;
  }
  .cate-line {
    border: 1px solid;
  }
</style>
