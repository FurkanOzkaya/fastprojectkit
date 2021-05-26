<template>
   <v-app-bar app :color="$root.themeColor">
      <v-app-bar-nav-icon @click="toggleNavigationBar">

      </v-app-bar-nav-icon>
      <v-toolbar-title>FastProject Kit Admin Panel</v-toolbar-title>
       <v-spacer></v-spacer>
      <v-btn
        class="ma-2"
        color="secondary"
        @click="getToken"
      > Copy Token </v-btn>
       <v-btn
        class="ma-2"
        color="secondary"
        @click="LogOut"
      >Log Out </v-btn>
    </v-app-bar>
</template>

<script>
export default {
  data() {
    return {
      token: ""
    }
  },
  methods:{
      toggleNavigationBar() {
        const vm = this;

        vm.$emit('toggleNavigationBar');
      },
      getToken(){
        let token = this.$store.getters.token
        var textArea = document.createElement("textarea");
        textArea.value = token;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand("copy")
        document.body.removeChild(textArea); 
      },
      LogOut(){
        this.$store.dispatch("updateToken", null)
        this.$router.push("Login")
      }
  }
}
</script>

<style>

</style>