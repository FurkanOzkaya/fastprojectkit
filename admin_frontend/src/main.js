import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

import { setupComponents } from './utils/setupComponents';
import router from './router'
import axios from 'axios'
import VueApexCharts from 'vue-apexcharts'
import store from './store'
import _ from 'lodash'
require('dotenv').config()
setupComponents(Vue);

Vue.use(VueApexCharts)
Object.defineProperty(Vue.prototype, "$_", { value: _ })
Vue.component('apexchart', VueApexCharts)
import SwaggerClient from 'swagger-client';

new Vue({
  vuetify,
  render: h => h(App),
  router,
  axios,
  store,
  SwaggerClient,
  data: {
    themeColor: '#f5f5f5'
  },

}).$mount('#app')
