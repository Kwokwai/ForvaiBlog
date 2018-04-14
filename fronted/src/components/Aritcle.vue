<template>
  <div class="left-main">
    <div class="left-content">
          <div class="detail">
            <div class="detail-date">
              {{ result.createYear}}
              <div class="date-line"></div>
              {{ result.createDate }}
            </div>
            <div class="detail-category">
              <div id="article_category" v-for="cate in result.category">
                <router-link :to="'/category/' + cate.cid">{{ cate.name }}</router-link>
              </div>
            </div>
            <div class="detail-title" id="article_title">
              {{ result.title }}
            </div>
            <div class="line-one"></div>
            <div class="detail-line">
              <div class="card-tag" v-for="tag in result.tag">
              <div class="tag-box">
                  <router-link :to="'/tag/' + tag.tid">{{ tag.name }}</router-link>
              </div>

            </div>
            </div>
            <div class="update-date">
              最后更新时间：{{ result.updateDate }}
            </div>
            <div class="detail-summery">
              <p>{{ result.summery }}</p>
            </div>
            <div class="detail-content">
              {{ result.content }}
            </div>
          </div>
      </div>
    </div>
</template>
<script>export default {
  name: 'aritcle',
  data () {
    return {
      result: {}
    }
  },
  created () {
    let id = this.$route.params.id
    this.$api.get('article/' + id, null, response => {
      this.result = response.data
      console.log(response.data)
    })
  }
}
</script>

<style scoped>
  .detail {
    height:100%;
    margin-left: 60px;
    margin-bottom: 50px;
    position: relative;
    background: #e6ffea;
    border-radius: 20px;
    padding-bottom: 50px;
    box-shadow: 0 0 5px 3px rgba(255, 174, 226, 0.5);
  }
  .detail-date {
    background-color: #ebffd1;
    box-shadow: 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.2), 0 1px 5px 0 rgba(0,0,0,.12);
    position: absolute;
    top: -20px;
    left: -30px;
    height: 60px;
    width: 70px;
    padding-top: 10px;
    border-radius: 100px;
    color: #ff59d0;
    text-align: center;
    line-height: 1.1;
  }
  .detail-title {
    font-size: 35px;
    text-align: center;
    margin: 0 auto;
    padding-left: 70px;
    padding-bottom: 20px;
    padding-top: 20px;
  }
  .detail-category {
    position:relative;
    width:75px;
    height:75px;
    float: right;
    box-sizing:border-box;
    background:linear-gradient(45deg, transparent 49.5%, deeppink 49.5%, deeppink 50.5%, transparent 50.5%);
  }
  .detail-line {
    margin-left: 250px;
  }
  .tag-box {
    display: inline-block;
    float: left;
    margin-left: 10px;
    background: #d9dbe9;
    border: 1px solid;
    width: 65px;
    margin-top: 5px;
    text-align: center;
    border-radius: 20px;
  }
  .detail-summery {
    margin-top: 50px;
    text-align: center;
    font-style: italic;
    color: grey;
  }
  .update-date {
    float: left;
    margin-left: 10px;
    margin-top: 3px;
    font-size: small;
  }
  .line-one {
    border-bottom: 1px dashed;
    width: 50%;
    margin-left: 195px;
    background: white;
    box-shadow: 0 0 5px 3px rgba(255, 174, 226, 0.5);  }

  .detail-content {
    margin-top: 25px;
    text-align: center;
  }
</style>
