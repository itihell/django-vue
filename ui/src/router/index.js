import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import PaginaLogin from '../views/login/index'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'login',
        component: PaginaLogin
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
]

console.log(process.env.BASE_URL)
const router = createRouter({
    history: createWebHistory("/"),
    routes
})

export default router
