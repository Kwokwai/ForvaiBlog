<template>
    <div class="left-main">
      <div class="left-content">
        <div class="article-list" v-for="result in results" :key="result.title">
          <router-link :to="'/article/' + result.aid">
          <div class="card">
            <div class="card-date">
              {{ result.createYear}}
              <div class="date-line"></div>
              {{ result.createDate }}
            </div>
            <div class="card-category">
              <div id="article_category" v-for="cate in result.category">
                <router-link :to="'/category/' + cate.cid">{{ cate.name }}</router-link>
              </div>
            </div>
            <!--<div class="card-top">-->
                <!--<p style="background: rgb(80, 144, 128);height: 25px;width: 50px;-->
                <!--text-align: center;float: right">时刻</p>-->
                <!--<p style="float: right;margin-right: 5px;margin-top: 5px">{{ result.createDate }}</p>-->
            <!--</div>-->
            <!--<div class="card-cate">-->
              <!--<div class="card-category" v-for="cate in result.category">-->
                  <!--<router-link :to="'/category/' + cate.cid">{{ cate.name }}</router-link>-->
              <!--</div>-->
            <!--</div>-->
            <div class="card-title" id="article_title">
              <router-link :to="'/article/' + result.aid"><p id="main_titile">{{ result.title }}</p></router-link>
            </div>
            <div class="card-line"></div>
            <div class="card-summery" id="article_summery">
              <p>{{ result.summery }}</p>
            </div>
            <!--<div class="card-tag" v-for="tag in result.tag">-->
              <!--<div class="tag-box">-->
                <!--<router-link :to="'/tag/' + tag.tid">{{ tag.name }}</router-link>-->
              <!--</div>-->
            <!--</div>-->
          </div>
          </router-link>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      results: []
    }
  },
  created () {
    this.$api.get('article', null, response => {
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
  #article_title {
    font-size: 20px;
    color: #555;
    padding-top: 15px;
  }
  #main_title {
    background: #f9ccd9;
  }
  #article_summery {
    font-size: 20px;
    margin-left: 40px;
  }
  .article-date {
    float: left;
    /*padding-top: 5px;*/
  }
  .tag-box {
    border: 1px solid;
    margin: 10px;
    width: 75px;
    text-align: center;
    border-radius: 25px;
  }
</style>
