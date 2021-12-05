import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
import TokenStore from './modules/TokenStore'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    tokenStore: TokenStore
  },
  plugins: [createPersistedState()]
})
