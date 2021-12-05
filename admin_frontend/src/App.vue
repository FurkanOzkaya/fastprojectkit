<template>
  <div id="app">
    <MainPage/>
  </div>
</template>
<script>
import MainPage from './components/MainPage'

export default {
  components: {
    MainPage,
  }
}
</script>


<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
