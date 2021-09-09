<template lang="pug">
  b-container
   
    b-row
      b-col(cols="4")
        b-overlay(:show="inProg" rounded="sm")
          b-card
            b-card-text
              b-button(@click="create"  variant="light")
                b-icon(icon="folder-plus")
                span Создать
              b-tree-view(:data="hier" nodeLabelProp="Name"  :renameNodeOnDblClick="false" :contextMenuItems="[]" @nodeSelect="onSelect" v-if="hier")
      b-col(v-if="selectedID")
        b-form
          b-form-group(
            label="Родительская категория"
            label-for="parent-select"
          )
            b-form-select(v-model="selected_parent" :options="parents" id="parent-select")
          b-form-group(
            label="Имя"
            label-for="input-1"
          )
            b-form-input(v-model="nameOfSelected")
          b-form-group(
            label="Описание"
            label-for="input-2"
           )
            b-form-textarea(v-model="descOfSelect" id="input-2" rows="4")
          b-form-group(
            label="Значение XML"
            label-for="input-3"
          )
            b-form-input(v-model="xmlOfSelect")
          b-form-group(
            label="Таблица"
            label-for="input-4"
          )
            b-form-select(id="input-4")
          b-button(type="submit" variant="primary") Сохранить
          b-button(type="reset" variant="danger" @click="deleteCat") Удалить
    b-modal(ref="create-hier-error-model" hide-footer title="Ошибка")
      h1 Ошибка создания категории
  
</template>

<script>
import { CreateEmptyCategory,DeleteCategory} from "../services/api"
import {mapActions} from "vuex"
export default {
  name: "hiertab",
  props:["hier","platform"],
  data(){
    return {
      selectedID:0,
      selected_parent:"",
      nameOfSelected:"",
      descOfSelect:"",
      xmlOfSelect:"",
      inProg:false
      
    }
  },
  methods:{
    ...mapActions(["getHier"]),
    onSelect(event, isSelected){
      if (isSelected){
        this.selectedID = event.data.id
        this.selected_parent = event.data.Parent
        this.nameOfSelected = event.data.Name
        this.descOfSelect = event.data.Description
        this.xmlOfSelect = event.data.XML_Value
      }
      

    },
    async deleteCat(){
      this.inProg = true
      const res = await !DeleteCategory(this.selectedID)
      if (res){
        this.inProg = false
        this.$refs["create-hier-error-model"].show()

      } else {
        await this.getHier()
        this.selectedID = false

        this.inProg =false

      }
      
    },

    async create(){
      this.selectedID = false
      this.inProg = true
      const res = await !CreateEmptyCategory(this.platform)
      if (res){
        this.inProg = false

      this.$refs["create-hier-error-model"].show()

      } else {
        await this.getHier()

        this.inProg =false

      }
      
    }
  },
  computed:{
    parents(){
      let data = []
        for (const el of this.hier){
            data.push({value: el.id, text: el.Name})
          
        }
      return data
      
    }
  }

};
</script>

<style scoped>

</style>
