<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="itemTodo.title"
      :counter="10"
      :rules="titleRules"
      label="Title"
      required
    ></v-text-field>

    <v-text-field
      v-model="itemTodo.description"
      :counter="10" 
      label="Description"
      required
    ></v-text-field>
 
    <v-select
      v-model="itemTodo.select" 
      :items="status"
      :rules="[v => !!v || 'Item is required']"
      label="Status"
      required
    ></v-select>

    <!--
    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>
    -->

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="create"
    >
      Create
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Clear
    </v-btn>
    <!--
    <v-btn
      color="warning"
      @click="resetValidation"
    >
      Reset Validation
    </v-btn>
    -->
  </v-form>
</template>

<script>
import * as Todo from '@/utils/todo'
export default {
layout:"main" ,
middleware: 'auth',    
data() {
  return {
    valid: true,  
    itemTodo: {
      title: '',
      description: '',
      select: null,
      selectFlag: null
    },
    titleRules: [
      v => !!v || 'Title is required',
      v => (v && v.length <= 10) || 'Title must be less than 10 characters',
    ],
    status: [
      'True',
      'False' 
    ],
  }
} ,
methods: {
  async create () {
    //this.$refs.form.validate() 
    //const data = await Todo.create(this.title,this.description,JSON.parse(this.select.toLowerCase()))
    //this.itemTodo.selectFlag = JSON.parse(this.itemTodo.select.toLowerCase())
    const data = await Todo.create(this.itemTodo)
    console.log(data) 
  },
  reset () {
      this.$refs.form.reset()
  },
  /*resetValidation () {
    this.$refs.form.resetValidation()
  },*/

},
}
</script>