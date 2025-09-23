import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

// Lazy load de vistas
const Home = () => import('../views/home/Home.vue');
const PetScreen = () => import('../views/pet/PetScreen.vue');
const PetSelect = () => import('../views/pet/PetSelect.vue');
const Login = () => import('../views/Auth/Login.vue');

// Definición de rutas
const routes: Array<RouteRecordRaw> = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/pet',
    name: 'PetScreen',
    component: PetScreen
  },
  {
    path: '/pet/select',
    name: 'PetSelect',
    component: PetSelect
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  // Ruta comodín para redirigir a home si no existe
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
];

// Crear router
const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
