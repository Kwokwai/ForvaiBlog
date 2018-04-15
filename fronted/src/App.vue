<template>
  <div class="container" id="app">
    <div class="header" id="black_line"></div>
    <div class="content">
      <div class="left">
        <div class="left-main">
          <div class="left-header">
            <ul>
              <li><router-link to="/" exact><h2 style="color:#b4c7ff;">首页</h2></router-link> </li>
              <li><router-link to="/category"><h2 style="color:#b4c7ff;">分类</h2></router-link> </li>
              <li><router-link to="/tag"><h2 style="color:#b4c7ff;">标签</h2 ></router-link> </li>
              <li><router-link to="/archive"><h2 style="color:#b4c7ff;">时刻</h2></router-link>
              <li><router-link to="/article"><h2 style="color:#b4c7ff;">文章</h2></router-link> </li>
            </ul>

          </div>
        </div>
          <div class="left-content"><router-view></router-view></div>
      </div>
      <div class="right" id="photo">
        <div class="right-main">
          <div class="right-top">
            <canvas class="canvas"></canvas>
          </div>
          <div class="right-down">
            <div class="dog"></div>
          </div>
        </div>
      </div>
      </div>
    <div class="footer" :class="{footer_line: bottom}">
      <div>
        <a class="back-top" @click="backTop()" v-show="backTopShow"></a>
      </div>
    </div>
  </div>
</template>

<script>export default {
  name: 'app',
  data () {
    return {
      bottom: false,
      backTopShow: false
    }
  },
  mounted () {
    window.addEventListener('scroll', this.topScroll)
  },
  methods: {
    backTop () {
      let back = setInterval(() => {
        if (document.body.scrollTop || document.documentElement.scrollTop) {
          document.body.scrollTop -= 1000
          document.documentElement.scrollTop -= 100
        } else {
          clearInterval(back)
        }
      })
    },
    topScroll () {
      if (document.documentElement.scrollTop + document.body.scrollTop > 100) {
        this.backTopShow = true
      } else {
        this.backTopShow = false
      }
    }
  }
}
</script>

<style>
  html {
    /*background: #d9dbe9;*/
  }
  * {
    margin: 0;
    padding: 0;
    list-style: none;
    text-decoration: none;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }
  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    width: 100%;
    height: 100%;
    min-height: 100%;
  }
  ul {
    display: flex;
    position: absolute;
    width: 800px;
    top: 15%;
    margin-left: 500px;
    transform: translate(-50%, -50%);
  }

  li {
    position: relative;
    padding: 20px;
    font-size: 20px;
    color: #000;
    line-height: 1;
    transition: 0.1s all linear;
    cursor: pointer;
  }
  .router-link-active {
    border-bottom: 3px solid #ffaee2;
    display: block;
    padding-bottom: 10px;
  }
  #black_line {
    width: 100%;
    height: 50px;
    background: #ffffff;
    border-bottom: 1px #f9ccd9;
    box-shadow: 0 0 5px 3px rgba(255, 174, 226, 0.5);
  }
  .content {
    margin: 10px;
    height: 100%;
    min-height: 100%;
  }
  .left {
    float:left;
    width: 70%;
    height: 100%;
    margin-bottom: 100px;
  }
  .right {
    width: 30%;
    float: right;
    height: 100%;
  }
  .left-main {
    /*margin: 10px;*/
  }
  .right-main {
    margin: 50px;
  }
  .right-top {
    border: 1px solid;
    height: 200px;
    margin: 10px;
    right:35px;
    top:80px;
    width:300px;
    position:fixed;
  }
  .right-down {
    border: 1px solid;
    height: 200px;
    margin: 10px;
    right:35px;
    top:320px;
    width:300px;
    position:fixed;
  }
  .left-header {
    margin: 20px;
    padding-top: -50px;
    padding-bottom: 50px;
    padding-left: 100px;
  }
  .left-content {
    width: 100%;
  }

  .card {
    min-height:200px;
    margin-left: 60px;
    margin-bottom: 50px;
    position: relative;
    background: #e6ffea;
    border-radius: 20px;
  }
  .card:hover {
    box-shadow: 2px 4px 6px #ffaee2;
  }
  .card-top {
    height: 25px;
    border: 1px solid;
    background: #ffffff;
    border-radius: 2px;
    box-shadow: 0 0 5px 3px rgba(255, 132, 221, 0.5);
  }
  .card-date {
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
  .card-title {
    margin: 20px;
    text-align: center;
  }
  .card-category {
    position:relative;
    width:75px;
    height:75px;
    float: right;
    box-sizing:border-box;
    background:linear-gradient(45deg, transparent 49.5%, deeppink 49.5%, deeppink 50.5%, transparent 50.5%);
  }
  .card-line {
    border-bottom: 1px dashed;
    width: 50%;
    margin-left: 185px;
    background: white;
    box-sizing:border-box;
    box-shadow: 0 0 5px 3px rgba(255, 174, 226, 0.5);
  }
  .date-line {
    border: 1px solid;
    margin: 5px;
  }
  .card-summery {
    margin: 10px;
    padding-top: 20px;
  }
  .card-tag {
    margin: 10px;
  }
  .title {
    size: 30px;
    margin: 50px;
  }
  .footer {
    /*margin: 0;*/
    /*height: 50px;*/
    /*width: 100%;*/
    /*background: #232323;*/
  }
  .footer_line {
    position: fixed;
    bottom: 0;
    margin: 0;
    height: 50px;
    width: 100%;
    background: #f9f1e1;
    z-index: -9999;
  }
  .back-top {
    position: fixed;
    right: 50px;
    bottom: 50px;
    width: 32px;
    height: 32px;
    background: url("assets/rocket.png");
  }
  #article_category {
    box-sizing:border-box;
    transform:rotate(45deg);
    text-align: center;
    margin-top: 15px;
    margin-left: 20px;
  }
</style>
