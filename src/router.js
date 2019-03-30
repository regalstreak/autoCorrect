import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import LoginTeacher from './views/Login/LoginTeacher.vue'
import Teacher from './views/Teacher/Teacher.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login/teacher',
      name: 'login-teacher',
      component: LoginTeacher
    },
    {
      path: '/teacher',
      name: 'teacher',
      component: Teacher
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
