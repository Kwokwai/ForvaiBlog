<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
  body,div,dl,dt,dd,ul,ol,li,
  h1,h2,h3,h4,h5,h6,pre,code,
  form,fieldset,legend,input,
  textarea,p,blockquote,th,td,button,span {
    margin: 0;
    padding: 0;
  }
  ul,li{
    list-style: none;
  }
  body {
    min-height: 1600px;
    background-image: url(/static/back.png);
    background-position: left top;
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
  }
</style>
