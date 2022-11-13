<template lang="html">
  <div>
    NEW BLOG
    <v-text-field v-model="title" label="Title"></v-text-field>
    <v-textarea v-model="body" label="Body"></v-textarea>
    <v-btn @click="handleCreateClicked"> Create </v-btn>
  </div>
</template>

<script>
import * as Common from '@/utils/common'
export default {
  layout:"main" ,
  middleware: 'auth',
  data() {
    return {
      title: '',
      body: ''
    }
  },
  methods: {
    async handleCreateClicked() {
      console.log("handleCreateClicked")
      Common.writelog("XXXXX")
      /*if (this.title.length === 0) {
        return
      }
      const response = await BlogsApi.create(this.title, this.body)
      console.log('RESPONSE', response)
      this.$router.replace({
        name: 'blogs-id',
        params: {
          id: response.data.id
        }
      })*/
    }
  }
}
</script>

<style lang="css" scoped></style>