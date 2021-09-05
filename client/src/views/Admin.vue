<template lang="pug">
  div
    b-card
      b-tabs(pills card)
        b-tab(v-for="(platform, index) in platforms" :key="index")
          template(#title)
            span {{platform.Name}}  
          h3 {{platform.Name}}
        b-tab(@click="addNew")
          template(#title)
            span Добавить  
            b-icon(icon="plus-circle").ml-2

    b-modal(ref="platform_input_modal" title="Добавить площадку" @ok="save")
      label(for="platform-name-input") Введите имя
      b-form-input(v-model="nameInput")

</template>

<script>
import { mapState, mapMutations,mapActions } from "vuex"
import {NewPlatform} from "../services/api"
export default {
  name: "Admin",

  data(){
    return{
      nameInput: ""
    }
  },
  computed: {
    ...mapState(["platforms"])
  },
  methods: {
    ...mapMutations(["AppendPlatform"]),
    ...mapActions(["getPlatforms"]),
    addNew() {
      this.$refs["platform_input_modal"].show()

    },
    async save() {
      const res = await NewPlatform({ Name: this.nameInput });
      this.AppendPlatform(res)
      this.$refs["platform_input_modal"].close()


    }
  },
  created(){
    this.getPlatforms()

  }

};
</script>

<style scoped>

</style>