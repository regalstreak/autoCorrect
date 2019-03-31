import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'
// import Home from './views/HomePage/index.vue'
import LoginTeacher from './views/Login/LoginTeacher.vue'
import Teacher from './views/Teacher/Teacher.vue'

// import OurHomePage from './views/HomePage/index.html'

import LoginExaminer from './views/Login/LoginExaminer.vue'
import Examiner from './views/Examiner/Examiner.vue'
import FileUpload from './views/Examiner/FileUpload.vue'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: Home
    // },
    // {
    //   path: '/destination',
    //   mode: history,
    //   name: 'home',
    //   component: { template: OurHomePage }
    // },
    {
      path: '/login/teacher',
      name: 'login-teacher',
      component: LoginTeacher
    },
    {
      path: '/login/examiner',
      name: 'login-examiner',
      component: LoginExaminer
    },
    {
      path: '/teacher',
      name: 'teacher',
      component: Teacher
    },
    {
      path: '/examiner',
      name: 'examiner',
      component: Examiner
    },
    {
      path: '/file-upload',
      name: 'file-upload',
      component: FileUpload
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
