import Vue from "vue";
import Vuex from "vuex";
import  {GetAllPlatforms, GetHierarcty, GetTables} from "../services/api"
Vue.use(Vuex);

function flatToHierarchy (flat) {

  var roots = [] 

  var all = {}

  flat.forEach(function(item) {
    all[item.id] = item
  })

  for (const key in all) {
    if (!all[key].Parent){
      roots.push(all[key])
    } else {
      if(!all[all[key].Parent].children){
        all[all[key].Parent].children = []

      }
      all[all[key].Parent].children.push(all[key])
      
    }
  }

  return roots
}

export default new Vuex.Store({
  state: {
    platforms: [],
    hier:[],
    tables:[]
  },
  mutations: {
    SetPlatform(state, data) {
      state.platforms = data;
    },
    AppendPlatform(state, data) {
      state.platforms.push(data)
    },
    SetHier(state, data){
      state.hier = data
    },
    SetTables(state,data){
      state.tables = data
    }
  },
  actions: {
    async getPlatforms(context) {
      context.commit("SetPlatform", await GetAllPlatforms());
    },
    async getHier(context){
      const hier = await GetHierarcty()

      context.commit("SetHier", flatToHierarchy(hier));
    },
    async GetTables(context){
      context.commit("SetTables", await GetTables())
    }
  },
  modules: {},
});
