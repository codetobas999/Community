<template>
  <v-flex xs12 sm8 md6 justify-center mx-auto>
    <v-alert
      v-model="error.show"
      border="right"
      colored-border
      type="error"
      transition="scale-transition"
      elevation="2"
      dismissible
      >{{ error.message }}
    </v-alert>
    
    <v-form
      ref="form"
      v-model="valid"
      lazy-validation
      @submit.prevent="validate"
    >
      
      <v-card :loading="isLoading">
        
        <v-app-bar dense flat>
          <Logobar />
        </v-app-bar>
        
        <v-card-text class="pb-1">
          
          <v-text-field
            v-model="login.username"
            :rules="usernameRules"
            label="Username"
            required
            @keyup.enter="$refs['input-password'].focus()"
            prepend-icon="mdi-account"
          ></v-text-field>
          <v-text-field
            v-model="login.password"
            ref="input-password"
            :rules="passwordRules"
            label="Password"
            required
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showPassword ? 'text' : 'password'"
            @click:append="showPassword = !showPassword"
          ></v-text-field>
        </v-card-text>
        
        <v-card-actions>
          <v-btn
            color="primary"
            block
            class="mx-auto text-capitalize font-weight-regular"
            type="submit"
          >
            Log in
          </v-btn>
        </v-card-actions>
        
      </v-card>
      
    </v-form> 
  </v-flex>
</template>

<script>
import { mapActions } from 'vuex'
import Logobar from '@/components/Globals/Logobar' 
import * as SettingApp from '@/utils/settingApp'
export default {
  components: {
      Logobar
    }, 
  layout: 'login_banner',
  auth: false,
  data() {
    return {
      mySettingApp:{
                  language:"EN",
                  theme:"default",
                  show_page:-1,
                  token_age:60
      },
      login: {
        username: '',
        password: '',
      },
      valid: true,
      showPassword: false,
      isLoading: false,
      error: {
        show: false,
        message: '',
      },
      usernameRules: [
        (v) => !!v || 'Username is required',
        (v) =>
          (v && v.length >= 4 && v.length <= 25) ||
          'Username must contain between 4 and 15 characters.',
      ],
      passwordRules: [
        (v) =>
          (v && v.length >= 4 && v.length <= 60) ||
          'Your password must contain between 4 and 60 characters.',
      ],

    }
  },
  methods: {
    ...mapActions({ clearAlert: 'alert/clear' }),
    validate() {
      if (this.$refs.form.validate()) {
        this.userLogin()
      }
    },
    async userLogin() {
      this.$refs.form.resetValidation()
      this.clearAlert()
      this.isLoading = true
      //this.menus = this.my_menus//กำหนดสิทธิ์การเข้า Menu
 
      await this.$auth
        /*.loginWith('local', { data: this.login })*/
        .loginWith('local', {data:`username=${this.login.username}&password=${this.login.password}`})
        .then((response) => {   
          console.log(response)  
          // redirect page
          let path = this.$auth.$storage.getUniversal('redirect') || '/'
          this.$auth.$storage.setUniversal('redirect', null)
          this.$router.push(path)
        })
        /*.catch((error) => {
          console.log(error)
          this.error = {
            show: true,
            message:
              (error.response &&
                error.response.data &&
                error.response.data.description) ||
              error.statusText ||
              error,
          }
        })
        .finally(() => {
          this.isLoading = false
        })*/

      console.log("--------------")
      //this.settingApp = this.mySettingApp
      this.settingApp = await SettingApp.queryByUser()//this.mySettingApp
      console.log("--------------")  
      console.log("userLogin : " +  this.login.username +'/' + this.login.password)
      console.log("show_page1 : " +  this.settingApp.show_page)
      //console.log("show_page2 : " +  this.$store.state.setting_app.show_page)
      this.isLoading = true
      this.$router.push('/')
      //this.$router.push('redirect')
      //let path = this.$auth.$storage.getUniversal('redirect') || '/'
      //    this.$auth.$storage.setUniversal('redirect', null)
      //    this.$router.push(path)
    }
    /*
    async userLogin() {
      this.$refs.form.resetValidation()
      this.clearAlert()
      this.isLoading = true
      await this.$auth
        .loginWith('local', { data: this.login })
        .then((response) => {
          console.log(response)
          // redirect page
          let path = this.$auth.$storage.getUniversal('redirect') || '/'
          this.$auth.$storage.setUniversal('redirect', null)
          this.$router.push(path)
        })
        .catch((error) => {
          console.log(error)
          this.error = {
            show: true,
            message:
              (error.response &&
                error.response.data &&
                error.response.data.description) ||
              error.statusText ||
              error,
          }
        })
        .finally(() => {
          this.isLoading = false
        })
    },
    */
  },
  computed: {
    settingApp: {
        get() {
          //console.log('get_settingApps' + this.$store.state.setting_app)  
          return this.$store.state.setting_app
        },
        set(newVal) {
          //console.log('set_settingApp' + newVal) 
          this.$store.commit('set_settingApp', newVal)
        }
      },
    /*menus: {
        get() {
          console.log('get_menus' + this.$store.state.menus)  
          return this.$store.state.menus
        },
        set(newVal) {
          console.log('set_menus' + newVal) 
          this.$store.commit('set_menus', newVal)
        }
      },
      authorizes: {
        get() {
          console.log('get_authorizes' + this.$store.state.authorizes)  
          return this.$store.state.authorizes
        },
        set(newVal) {
          console.log('set_authorizes' + newVal) 
          this.$store.commit('set_authorizes', newVal)
        }
      }, */ 
    } 
}
</script>
