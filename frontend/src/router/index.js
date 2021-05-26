import Vue from 'vue'
import VueRouter from 'vue-router'
import About from  '../components/views/About.vue'
import Dashboard from  '../components/views/Dashboard.vue'
import Swagger from  '../components/Swagger/Swagger.vue'
import Login from  '../components/views/Login.vue'
import Error from  '../components/views/Error.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      allowAnonymous: true
    }
  },
  {
    path: '/',
    name: 'Main',
    component: Dashboard
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About
  },
  {
    path: '/swagger',
    name: 'Swagger',
    component: Swagger
  },
  {
    path: '/request',
    name: 'Request',
    component: Dashboard
  },
  {
    path: '/other1',
    name: 'Other1',
    component: Dashboard
  },
  {
    path: '/other2',
    name: 'Other2',
    component: Dashboard
  },
  {
    path: '/other3',
    name: 'Other3',
    component: Dashboard
  },
  // {
  //   path: '/login',
  //   name: 'Login',
  //   //component: Login,
  //   meta: {
  //     allowAnonymous: true
  //   }
  // },
  {
    path: '/error',
    name: 'Error',
    component: Error,
    meta: {
      allowAnonymous: true
    }
  },
  {
    path: '*',
    component: Error,
    meta: {
      allowAnonymous: true
    }
  }
]

const router = new VueRouter({
  routes
})

export default router
