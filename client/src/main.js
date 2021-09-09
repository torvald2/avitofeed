import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
import BootstrapVueTreeview from 'bootstrap-vue-treeview'
Vue.use(BootstrapVueTreeview)
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
