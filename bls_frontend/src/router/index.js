import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Verdict from "@/views/VerdictView";
import Search from "@/views/Search";

Vue.use(VueRouter)

const routes = [
  {
    path: process.env.VUE_APP_PATH_BASE + '/',
    name: 'Home',
    component: Home
  },
  {
    path: process.env.VUE_APP_PATH_BASE + '/suche',
    name: 'Search',
    component: Search
  },
  {
    path: process.env.VUE_APP_PATH_BASE + '/urteil',
    name: 'Verdict',
    meta: {
      hidden: true
    },
    component: Verdict
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
