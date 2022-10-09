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
export default {
  components: {
      Logobar
    }, 
  layout: 'login_banner',
  auth: false,
  data() {
    return {
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
          (v && v.length >= 4 && v.length <= 15) ||
          'Username must contain between 4 and 15 characters.',
      ],
      passwordRules: [
        (v) =>
          (v && v.length >= 4 && v.length <= 60) ||
          'Your password must contain between 4 and 60 characters.',
      ],
      my_authorize: [
        // { icon: 'mdi-apps', title: 'Welcome', to: '/' },
        // { icon: 'mdi-chart-bubble', title: 'Inspire', to: '/inspire' },
            {id:1000, name:"หน้าแรก", title: 'หน้าแรก',icon: 'mdi-apps', to: '/sss',isAuthen:true,
             pages: []  
            },
            {id:2000, name:"บทความ", title: 'บทความ',icon: 'mdi-chart-bubble',to: '/',isAuthen:true, 
            pages: [ {title: 'บทความ1', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                     {title: 'บทความ2', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                    ]  
            },    
            {id:3000, name:"ผู้เขียน", title: 'ผู้เขียน',icon: 'mdi-database',to: '/',isAuthen:true, 
            pages: [ {title: 'ผู้เขียน1', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                     {title: 'ผู้เขียน2', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                    ]  
            },
            {id:4000, name:"ข้อมูลลูกค้า", title: 'ข้อมูลลูกค้า',icon: 'mdi-database',to: '/',isAuthen:true, 
            pages: [ {title: 'เพิ่มประวัติ', icon: 'mdi-format-list-checks', to: '/registers',isAuthen:true},
                     {title: 'แก้ไขประวัติ', icon: 'mdi-format-list-checks', to: '/registers/customer_info',isAuthen:true},
                     {title: 'แก้ไขประวัติ2', icon: 'mdi-format-list-checks', to: '/registers/customer_info2',isAuthen:true},
                    ]  
            }, 
            {id:5000, name:"ตารางนัดหมาย", title: 'ตารางนัดหมาย',icon: 'mdi-database',to: '/',isAuthen:true, 
            pages: [ {title: 'ดูนัดหมาย', icon: 'mdi-format-list-checks', to: '/appointments',isAuthen:true}, 
                   ]  
            },     
            {id:6000, name:"กิจกรรม", title: 'กิจกรรม',icon: 'mdi-database',to: '/',isAuthen:true, 
            pages: [ {title: 'ดูกิจกรรม', icon: 'mdi-format-list-checks', to: '/activitys',isAuthen:true}, 
                   ]  
            },                     
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
      this.authorize = this.my_authorize//กำหนดสิทธิ์การเข้า Menu

      await this.$auth
        .loginWith('local', { data: this.login })
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



      console.log("userLogin : " +  this.login.username +'/' + this.login.password)
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
    authorize: {
        get() {
          console.log('get_authorize' + this.$store.state.authorize)  
          return this.$store.state.authorize
        },
        set(newVal) {
          console.log('set_authorize' + newVal) 
          this.$store.commit('set_authorize', newVal)
        }
      },
    } 
}
</script>
