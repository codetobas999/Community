<template>
    <v-data-table
      :headers="headers"
      :items="desserts"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar
          flat
        >
          <v-toolbar-title>User Group All</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
            v-model="dialog"
            max-width="500px"
          > 
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
              >
                New Item
              </v-btn>
            </template>  

            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>
  
              <v-card-text>
                <v-container>
                 
                  <v-row>
                    <v-col cols="12" sm="6" md="4" >
                      <v-text-field
                        v-model="editedItem.user_code"
                        label="Email"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12" sm="6" md="4" > 
                      <v-select
                        v-model="editedItem.group_code"
                        :items="groups"
                        label="Group Code"
                    ></v-select>
                    </v-col>

                    <v-col cols="12" sm="6" md="4" > 
                      <v-switch
                         v-model="editedItem.status"
                         inset
                         :label="`Status : ${editedItem.status.toString()}`"
                      ></v-switch>
                    </v-col>
                   
                  </v-row>
                  
                </v-container>
              </v-card-text>
  
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="save"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn
          color="primary"
          @click="initialize"
        >
          Reset
        </v-btn>
      </template>
    </v-data-table>
  </template>
      
    <script> 
    import * as AuthUserGroup from '@/utils/authUserGroup'
    export default {
      layout:"main" ,
      middleware: 'auth',
      data: () => ({
           dialog: false,
           dialogDelete: false, 
 
        headers: [ 
          { text: 'Email', value: 'user_code' },
          { text: 'Group Code', value: 'group_code' }, 
          { text: 'Status', value: 'status' },
          { text: 'Actions', value: 'actions', sortable: false },
        ],
        desserts: [],
        editedIndex: -1,
        editedItem: {
          user_code: '', 
          group_code: '', 
          status: false, 
        },
        defaultItem: {
          user_code: '',
          group_code: '', 
          status: false, 
        },
        groups: [
          'G0001',
          'G0002',
          'G0003',
          'G0004',
        ],
     }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      }, 
    },  
    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.initialize()
    },

    methods: {
      async initialize () {
        //this.$refs.form.validate() 
        //const data = await Todo.create(this.title,this.description,JSON.parse(this.select.toLowerCase()))
        //this.itemTodo.selectFlag = JSON.parse(this.itemTodo.select.toLowerCase())
        this.desserts  = await AuthUserGroup.queryAll()
        //console.log(desserts) 
      }, 
      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      }, 
      deleteItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      }, 
      async deleteItemConfirm () {
        console.log("Delete")
        const data = await AuthUserGroup.destroy(this.editedItem.auth_user_id) 
        console.log(data)
        this.desserts.splice(this.editedIndex, 1)
        this.closeDelete()
      }, 
      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      }, 
      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      }, 
      async save () {
        console.log("Save") 
        if (this.editedIndex > -1) {
          console.log("Update")
          Object.assign(this.desserts[this.editedIndex], this.editedItem)           
          const data = await AuthUserGroup.update(this.editedItem) 
          console.log(data) 
        } else {
          console.log("Create") 
          console.log(this.editedItem)
          const data = await AuthUserGroup.create(this.editedItem)   
          this.editedItem.user_id = data.data.user_id
          this.desserts.push(this.editedItem)
          
        }
        this.close()
      },
    },  
    
}
</script>
      
<style> 
</style>
      