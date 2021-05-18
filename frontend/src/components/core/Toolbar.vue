<template>
   <v-app-bar app :color="$root.themeColor">
      <v-app-bar-nav-icon @click="toggleNavigationBar">

      </v-app-bar-nav-icon>
      <v-toolbar-title>FastProject Kit Admin Panel</v-toolbar-title>
    </v-app-bar>
</template>

<script>
export default {
  methods:{
      toggleNavigationBar() {
        const vm = this;

        vm.$emit('toggleNavigationBar');
      }
  }
}
</script>

<style>

</style>