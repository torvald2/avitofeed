<template lang="pug">
b-container
  b-row 
    b-col
      b-button(variant="primary" @click="showTableCreateModal") Создать
  b-row
    b-col
      b-tabs(pills card vertical nav-wrapper-class="w-30")
        b-tab(v-for="(table, index) in tables" :key="'admin-tab'+index"  @activate-tab="getCels(table.id)")
          template(#title)
            span {{table.name}} 
            b-button(size="sm"  variant="link" @click="showDeleteTableModal(table.id)")
              b-icon(icon="x-octagon-fill" variant="danger")
          b-button(variant="primary" @click="createField(table.id)") Создать поле
          b-table(:items="items" :fields="fields" striped responsive)
            template(#cell(show_details)="row")
              b-button(size="sm" @click="row.toggleDetails" class="mr-2")
                | {{ row.detailsShowing ? 'Скрыть детали' : 'Показать детали'}}
            template(#row-details="row")
              b-form
                b-row
                  b-col
                    b-form-group(label="Имя")
                      b-form-input(v-model="row.item.cellName")
                  b-col
                    b-form-group(label="Поле XML")
                      b-form-input(v-model="row.item.xmlValues")
                b-row
                  b-col
                    b-form-group(label="Тип данных")
                      b-form-select(v-model="row.item.dataType" :options="dataTypeOpts")
                  b-col
                    b-form-group(label="Максимальная длина")
                      b-form-input(v-model="row.item.max_len")
                b-row 
                  b-col 
                    b-form-group(label="Подсказка")
                      b-form-textarea(v-model="row.item.info" rows=4)
                  b-col 
                    b-form-group(label="Значения")
                      b-form-textarea(v-model="row.item.values" rows=4)
                b-row
                  b-col 
                    b-form-group(label="Отображается если в поле:")
                      b-form-select(v-model="row.item.fieldForDisplay" :options="fieldListOptions" rows=4)
                  b-col 
                    b-form-group(label="Значения при выборе которых отображается")
                      b-form-textarea(v-model="row.item.valueForDisplay" rows=4)
                b-row
                  b-col
                    b-button(variant="primary", @click="saveItem(row.item)") Сохранить
                    
                    


  b-modal(ref="table_input_modal" title="Добавить таблицу" @ok="saveTable")
      label(for="table-name-input") Введите имя
      b-form-input(v-model="nameInput")
  b-modal(ref="table_delete_modal" title="Удалить" @ok="delTable")
      | Вы действительно хотите удалить таблицу

      
  
</template>

<script>
import { NewTable, DeleteTable, GetCells, NewCel, SaveCell} from "../services/api"
import {mapActions} from "vuex"
export default {
  name: "tableTab",
  props:["platform","tables"],
  data(){
    return {
        fields:[
            { key: 'cellName', label: 'Название'},
            {key:"xmlValue", label:"Значение XML"},
            {key:"dataType", label:"Тип данных"},
            {key:"show_details", label:"Редактировать"},
        ],
        items:[],
        nameInput:"",
        tableForDelete:0,
        dataTypeOpts:[
         { value: 1, text: 'Число' },
          { value: 2, text: 'Текст' },
          { value: 3, text: 'Выбор из списка' },
          { value: 4, text: 'Дата' },
          { value: 5, text: 'Булево' },
        ]
   
    }
  },
  methods:{
      ...mapActions(["GetTables"]),
      async getCels(tableId){
          const cels = await GetCells(tableId)
          this.items  = cels
      },
      showTableCreateModal(){
          this.$refs["table_input_modal"].show()
      },
      showDeleteTableModal(pk){
           this.tableForDelete = pk
           this.$refs["table_delete_modal"].show()
      },
      async saveTable(){
        const res = await NewTable(this.nameInput, this.platform);
        if (res){
            this.GetTables()
        } else {
            alert("Не удалось создать таблицу")

        }
        this.$refs["table_input_modal"].close()

      },
      async delTable(){
         const res = await DeleteTable(this.tableForDelete)
         if (res){
             this.GetTables()
         } else {
             alert("Не удалось удалить таблицу")
         }
         this.$refs["table_delete_modal"].close()

      },
      async createField(tableId){
          const res = await NewCel(tableId)
          if (res){
              await this.GetCells(tableId)
          } else {
              alert("Не удалось создать таблицу")
          }


      },
      async saveItem(data){
          data.values=[]
          const res = await SaveCell(data)
          if (res){
              alert("Успешно сохранено")
          } else {
              alert("Ошибка")
          }
          

      }
    
  },
  computed:{
      fieldListOptions(){
          let opts = []
          for (let i of this.items){
              opts.push({value: i.id, text: i.cellName})
          }
          return opts
      }
  },

  async beforeMount(){
      await this.getCels(this.tables[0].id)
      
    
  }

};
</script>

<style scoped>

</style>
