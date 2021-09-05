import Vue from "vue";
import Vuex from "vuex";
import  {GetAllPlatforms} from "../services/api"
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    platforms: [],
  },
  mutations: {
    SetPlatform(state, data) {
      state.platforms = data;
    },
    AppendPlatform(state, data) {
      state.platforms.push(data)
    },
  },
  actions: {
    async getPlatforms(context) {
      context.commit("SetPlatform", await GetAllPlatforms(context.state.token));
    },
  },
  modules: {},
});
