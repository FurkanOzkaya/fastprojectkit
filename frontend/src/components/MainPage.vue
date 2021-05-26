<template>
  <div>
    <template v-if="!$route.meta.allowAnonymous">
      <v-app id="inspire">
        <div class="app-container">
          <toolbar @toggleNavigationBar="drawer = !drawer" />
          <navigation :toggle="drawer" />
          <v-main>
            <router-view/>
          </v-main>
        </div>
      </v-app>
    </template>
    <template v-else>
      <transition>
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </transition>
    </template>
  </div>
</template>

<script>
import { mapState } from "vuex";
import UserService from '../service/services/UserService';

export default {
  name: 'Main',
  mounted() {
    this.checkUser()
  },
  data() {
    return {
      drawer: true,
      token: undefined
    }
  },
  computed: {
    ...mapState({
      tokenStore: (state) => state.tokenStore.token,
    }),
  },
  watch: {
    tokenStore(newValue) {
      this.token = newValue
      this.$nextTick()
      {
        if(this.token == null || this.token == undefined)
        {
           this.goLogin()
        }
      }
    },
  },
  methods: {
    goLogin(){
      this.$store.dispatch("updateToken", null)
      this.$router.push({ name:"Login" });
    },
    checkUser()
    {
      if(this.$store.getters.token == null || this.$store.getters.token == undefined)
      {
        this.goLogin()
      }
      else{
        UserService.getUser(this.$store.getters.token).then((response) => {
          if(response.status != 200) {
            // alert here
          }
        }).catch((error) =>{ 
          if(error.response.status == 401)
            {
              this.goLogin()
            }
            else {
              // her give alert box
            }
        })
      }
    }
  }
};
</script>

<style scoped>

</style>
