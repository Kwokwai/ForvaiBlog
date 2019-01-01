<template lang="html">
  <div class="article-list">
    <article class="block post wysiwyg" v-for="item in list">
      <h2>{{item.title}}</h2>
      <p class="article-meta">发布于 {{item.createDate}}</p>
      <div class="ui ribbon label red">
        <router-link :to="{path:'/category', query:{mk:item.category.mk}}">{{item.category.name}}</router-link>
      </div>
      <div class="abstract" v-html="item.summary">
      </div>
      <p class="more"><router-link :to="{ path:'/article', query:{mk:item.mk}}">阅读全文</router-link></p>
    </article>
    <!--<page total="total" :current-page='current' @pagechange="pagechange"></page>-->
    <div class="pages">
      <a href="javascript:;" @click="go(page-=1)" style="float: left;">上一页</a>
      <a href="javascript:;" @click="go(page+=1)" style="float: right;">下一页</a>
    </div>
  </div>
</template>

<script>
import page from './page'
// import axios from 'axios'
export default {
  components: {
    page
  },
  props: [
    'tagSelect'
  ],
  data () {
    return {
      total: 10,
      list: [],
      page: 1,
      pageSize: 10,
      count: 0
    }
  },
  watch: {
    tagSelect () {
      this.getTagList()
    }
  },
  mounted () {
    this.getlist()
  },
  methods: {
    getlist () {
      // var param = {
      //   page: this.page,
      //   pageSize: this.pageSize
      // }
      this.$api.get('/article', null, response => {
        console.log(response)
        if (response.status === 200) {
          console.log(this.page)
          if (response.data.list.length === 0) {
            this.page -= 1
            console.log(this.page)
          } else {
            this.list = response.data.list
          }
        } else {
          this.list = []
        }
      })
      // axios.get('/api/articleList', {
      //   params: param
      // }).then((result) => {
      //   let res = result.data
      //   if (res.status == '0') {
      //     if (res.result.count == 0) {
      //       this.page -= 1
      //     } else {
      //       this.list = res.result.list
      //     }
      //   } else {
      //     this.list = []
      //   }
      // })
    },
    // getTagList () {
    //   var param = {
    //     page: this.page,
    //     pageSize: this.pageSize,
    //     tag: this.tagSelect
    //   }
    //   axios.get('/api/tagsDetial', {
    //     params: param
    //   }).then((result) => {
    //     let res = result.data
    //     if (res.status == '0') {
    //       if (res.result.count == 0) {
    //         this.page -= 1
    //       } else {
    //         this.list = res.result.list
    //       }
    //     } else {
    //       this.list = []
    //     }
    //   })
    // },
    go () {
      if (this.page < 1) {
        this.page = 1
      } else {
        this.getlist()
      }
    }
  }
}
</script>

<style media="screen" lang="scss">
  .article-list {
    padding: 20px;
    opacity:0.5;
    background: #fff;
    border-radius: 10px;
    /*box-shadow: 1px 1px 2px rgba(0,0,0,0.08)*/
    box-shadow: 0 16px 24px 1px rgba(0, 0, 0, 0.14),
    0 6px 50px 1px rgba(0, 0, 0, 0.12),
    0 6px 10px -5px rgba(0, 0, 0, 0.2);
  }
  .content .post, .recent-comments {
    white-space: normal;
    word-break: break-all;
    word-wrap: break-word;
  }
  .block.post {
    background: #fff;
  }
  .block {
    position: relative;
    background: #fff;
    padding: 15px;
    border-bottom: 1px solid #e0e0e0;
  }

  article h1 {
    text-align: center;
    padding: 0.1em 80px 0 80px;
    color: #363636;
    position: relative;
  }
  article h2 {
    text-align: center;
    padding: 0.1em 80px 0 80px;
    color: #363636;
    position: relative;
  }

  /*小标*/
  .ui.red.ribbon.label {
    border-color: #47456d;
    box-shadow: 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.2), 0 1px 5px 0 rgba(0,0,0,.12);
  }
  .ui.red.label, .ui.red.labels .label {
    background-color: #97dffd;
    border-color: #97dffd;
    color: #fff;
    margin: 5px 0 15px 2px;
    font-size: 14px;
  }
  .ui.ribbon.label {
    position: relative;
    margin: 0 .2em;
    left: -3.3rem;
    padding-left: 2rem;
    border-radius: 0 4px 4px 0;
    border-color: rgba(0,0,0,.15);
  }
  .ui.label:last-child {
    margin-right: 0;
  }
  .ui.ribbon.label {
    margin-top: 5px;
    margin-bottom: 5px;
  }
  .ui.label {
    display: inline-block;
    padding: .5em .8em;
  }
  .ui.ribbon.label:after {
    position: absolute;
    content: "";
    top: 100%;
    left: 0;
    border-top: 0 solid transparent;
    border-right-width: 1em;
    border-right-color: inherit;
    border-right-style: solid;
    border-bottom: 1em solid transparent;
    border-left: 0 solid transparent;
    width: 0;
    height: 0;
  }
  .ui.label a {
    color: inherit;
  }

  .article-meta {
    color: #555;
    font-size: 14px;
    word-break: break-word;
    line-height: 20px;
  }

  .abstract {
    font-size: 1.1rem;
    line-height: 1.8em;
    margin: 1em 0;
    color: #333;
    text-indent: 2em
  }
  .abstract img {
    max-width: 100%;
    display: block;
  }

  .article-meta, .more {
    text-align: center;
  }
  .more a {
    background-color: #96e1fc;
    color: #fff;
    font-size: 12px;
    padding: 5px 10px;
    border-radius: 5px;
    /*background-color: #e8e8e8;*/
    transition: .5s;
    -o-transition: .5s;
    -moz-transition: .5s;
    -webkit-transition: .5s;
  }
  .pages {
    width: 100%;
    margin: 20px auto 0;
    overflow: hidden;
  }
  .pages a {
    background: #97dffd;
    display: block;
    padding: 8px 10px;
    margin: 0 20px;
    border-radius: 5px;
    text-align: center;
    font-size: 14px;
    color: #fff;
  }
  @media (max-width: 800px) {
    .article-list {
      border-radius: 0!important;
    }
    .ui.ribbon.label:after{
      display: none;
    }
  }

</style>
