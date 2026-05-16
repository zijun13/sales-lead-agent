import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LeadsView from '../views/LeadsView.vue'
import CustomersView from '../views/CustomersView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/leads',
    name: 'leads',
    component: LeadsView
  },
  {
    path: '/customers',
    name: 'customers',
    component: CustomersView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router