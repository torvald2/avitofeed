<template lang="pug">
  div
    b-card
      b-tabs(pills card)
        b-tab(v-for="(platform, index) in platforms" :key="'admin-tab'+index"  )
          template(#title)
            span {{platform.Name}} 
            b-button(size="sm"  variant="link" @click="showDeletePlatfornModal(platform.id)")
              b-icon(icon="x-octagon-fill" variant="danger") 
          h3 {{platform.Name}}
          HierTab(:hier="getCurrentPlatformHier(platform.id)" :platform="platform.id")
        b-tab(@click="addNew")
          template(#title)
            span Добавить  
            b-icon(icon="plus-circle").ml-2

    b-modal(ref="platform_input_modal" title="Добавить площадку" @ok="save")
      label(for="platform-name-input") Введите имя
      b-form-input(v-model="nameInput")
    
    b-modal(ref="platform_delete_modal" title="Удалить" @ok="delPlatform")
      | Вы действительно хотите удалить площадку

</template>

<script>
import { mapState, mapMutations,mapActions } from "vuex"

import {NewPlatform, DeletePlatform} from "../services/api"
import HierTab from "../components/HierTab.vue"
export default {
  name: "Admin",
  components:{
    HierTab
  },

  data(){
    return{
      nameInput: "",
      platformForDelete:0
      
    }
  },
  computed: {
    ...mapState(["platforms","hier"]),
   
  },
  methods: {
    ...mapMutations(["AppendPlatform"]),
    ...mapActions(["getPlatforms","getHier"]),
    addNew() {
      this.$refs["platform_input_modal"].show()

    },
    getCurrentPlatformHier(platform){
      return this.hier.filter(x => x.Platform === platform)
    }
    ,
    async save() {
      const res = await NewPlatform({ Name: this.nameInput });
      this.AppendPlatform(res)
      this.$refs["platform_input_modal"].close()

    },
    async delPlatform() {
      const res = await DeletePlatform(this.platformForDelete)
      if (res) {
        await this.getPlatforms()
        this.$refs["platform_delete_modal"].close()

      }
      
    },
    showDeletePlatfornModal(pk){
      this.platformForDelete = pk
      this.$refs["platform_delete_modal"].show()
    }


  },
  created(){
    this.getPlatforms()
    this.getHier()

  }

};
</script>

<style scoped>

</style>