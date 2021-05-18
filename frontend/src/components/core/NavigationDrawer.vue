<template>
   <v-navigation-drawer
      v-model="localToggle"
      fixed app
      :color="$root.themeColor">
     <a href="https://furkanozkaya.com">
       <v-sheet
        color="grey lighten-4"
        class="pa-4"
      >
        <v-avatar
          class="mb-4"
          color="grey darken-1"
          size="64"
        >
          <img
          src="https://avatars.githubusercontent.com/u/48178781?v=4"
          alt="Furkan Ozkaya"
          >
        </v-avatar>

        <div>Furkanozkaya.com</div>
      </v-sheet>
     </a>

      <v-divider></v-divider>

      <v-list>
        <v-list-item
          v-for="[icon, text, routeName] in links"
          :key="icon"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content @click="routePage(routeName)">
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

</template>

<script>
export default {
    props: {
        toggle: {
            type: Boolean,
            required: false,
            default: true
        }
    },
    data: () => ({
      localToggle: true,
      cards: ['Today', 'Yesterday'],
      links: [
        ['mdi-view-dashboard', 'Dashboard', "Dashboard"],
        ['mdi-account-convert', 'User Table', "User"],
        ['mdi-rocket', 'Request', "Request"],
        ['mdi-alert-octagon', 'Other 1', "Other1"],
        ['mdi-security-network', 'Other 2', "Other2"],
        ['mdi-server', 'Other 3', "Other3"],
        ['mdi-account-box', 'About', "About"],
      ],
    }),
  methods: {
    routePage(routeName) {
       this.$router.push({ name: routeName });
    }
  }, 
  watch: {
    toggle() {
      this.localToggle = this.toggle
    }
  }
}
</script>

<style>

</style>