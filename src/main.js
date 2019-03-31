import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import './stylus/main.styl'
import VueLazyload from 'vue-lazyload'
// import gradient from 'random-gradient'


Vue.use(VueLazyload);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')


// Vue.directive('random-gradient', {
//     inserted: function (el) {
//         // Using the element's "title" attribute, e.g.
//         el.style.backgroundImage = gradient(el.title);
//     }
// });