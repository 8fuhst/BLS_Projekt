import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Verdict from "@/views/VerdictView";
import Search from "@/views/Search";

Vue.use(VueRouter)

const routes = [
  {
    path: '/BLS_Tool/',
    name: 'Home',
    component: Home
  },
  {
    path: '/BLS_Tool/suche',
    name: 'Search',
    component: Search
  },
  {
    path: '/BLS_Tool/urteil',
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
