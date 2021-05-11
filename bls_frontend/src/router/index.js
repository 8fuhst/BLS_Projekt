import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Suche from "@/views/Suche";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/suche',
    name: 'Suche',
    component: Suche
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
