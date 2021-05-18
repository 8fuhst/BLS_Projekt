import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Verdict from "@/views/Verdict";
import Search from "@/views/Search";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/suche',
    name: 'Search',
    component: Search
  },
  {
    path: '/urteil',
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
