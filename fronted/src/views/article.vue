<template lang="html">
<div class="article">
  <navbar></navbar>
  <div class="headpic">
    <div class="container headtitle full">
      <div class="title">
        <!-- <h1 href="/blog">四月</h1> -->
      </div>
    </div>
  </div>
  <div class="container full">
    <div class="list">
      <div class="main-full">
        <div class="full-content">
          <header>
            <h2>{{article.title}}</h2>
            <p class="byline">by Kwok
              <span class="sep">|</span>
              <span class="date">{{article.createDate}}</span>
            </p>
          </header>
         <!--  <div class="post-content wysiwyg" v-html="article.content">
          </div> -->
          <vue-markdown :source="content" class="article-content"></vue-markdown>
        </div>
      </div>
    </div>
  </div>
  <scroll-top></scroll-top>
</div>
</template>

<script>
import Navbar from '@/components/navbar.vue'
import ScrollTop from '@/components/scrollTop'
import Articles from '@/components/article'
import VueMarkdown from 'vue-markdown'

export default {
  name: 'index',
  components: {
    Navbar,
    ScrollTop,
    Articles,
    VueMarkdown
  },
  data() {
    return {
      list: [],
      article: '',
      content: ''
    }
  },
  mounted() {
    this.articleDetial()
  },
  methods: {
    articleDetial() {
		let mk = this.$route.query.mk
		let param = {
		mk: mk
		}
		this.$api.get('/article', param, response => {
		  console.log(response)
		  this.article = response.data
      this.content = this.article.content
		})
    //   axios.get("/api/articleDetial", {
    //     params: param
    //   }).then((result) => {
    //     let res = result.data
    //     if (res.status == "0") {
    //       this.article = res.result
    //     } else {
    //       this.article = ''
    //     }
    //   })
    // }
  }
}
}
</script>

<style media="screen">
body {
  background-color: #f4f4f4;;
}
.headpic {
    height: 160px;
    background: url(/static/head.jpg) center -52px no-repeat;
    -webkit-background-size: cover;
    background-size: cover;
    position: relative;
  }
.main-full {
  opacity:0.8;
  width: 100%;
  margin: 0 0 30px 0;
  margin-top: -50px;
  background: #fff;
  border-radius: 8px;
  /*box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.08);*/
  box-shadow: #a9649f 0px 0px 30px 5px;
  overflow: hidden;
  -webkit-transition: all .5s ease-out;
  transition: all .5s ease-out;
}

.full-content {
  padding: 60px 0;
}

.full-content header {
  width: 66%;
  margin: 0 auto 50px auto;
}

.post-content {
  width: 66%;
  margin: 0 auto;
  margin-bottom: 20px;
}

.full-content h2 {
  margin: 0 20px 0 0;
  font-size: 40px;
  font-weight: 500;
  line-height: 1;
  letter-spacing: -.03em;
  color: #444;
}

.article-content {
    width: 100%;
    height: 100%;
    padding: 8px 25px 15px 65px;
    overflow-y: auto;
    box-sizing: border-box;
    overflow-x: hidden;
    background: #fbfbfb;
}

.article-content h1, .article-content h2, .article-content h3, .article-content h4, .article-content h5, .article-content h6 {
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
}

.article-content ul {
    margin-top: 0;
    margin-bottom: 16px;
    padding-left: 2em;
    list-style: disc;
}

.article-content h1 {
    padding-bottom: .3em;
    font-size: 2em;
    border-bottom: 1px solid #eaecef;
}

.article-content h2 {
    padding-bottom: .3em;
    font-size: 1.5em;
    border-bottom: 1px solid #eaecef;
}

.byline {
  width: auto;
  margin: 12px 0;
  font-weight: 500;
}

.byline span.sep {
  margin: 0 4px;
  font-weight: normal;
  color: #ddd;
}

.byline span.date {
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: .03em;
  color: #bbb;
}

/*markdown补充*/
.wysiwyg img {
  max-width: 100%;
  display: block;
}

.wysiwyg ul li{
  list-style-type: disc;
}
.wysiwyg ol li {
    list-style-type: decimal;
}
</style>
