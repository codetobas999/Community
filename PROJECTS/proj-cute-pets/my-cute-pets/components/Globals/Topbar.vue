<template> 
  <v-app-bar :clipped-left="true" app dense flat dark>
    <v-app-bar-nav-icon @click.stop="toggle_menu" />
    <div class="mx-5"><Logobar /></div>
    <v-spacer />
    <v-toolbar-items> 
      <div v-if="$auth.loggedIn && $auth.user.first_name"> 
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-avatar
              :color="stringToColor($auth.user.first_name)"
              v-on="on"
              size="40"
              style="margin-top: 2px"
            >
              <!--span class="white--text headline">{{$auth.user.name.substr(0, 1).toUpperCase()}}</span-->
              <span class="white--text headline">{{$auth.user.first_name.substr(0, 1)}}</span>
            </v-avatar>
          </template>
          <v-card>
            <v-list>
              <v-list-item>
                <v-list-item-avatar>
                  <v-avatar
                    :color="stringToColor($auth.user.first_name)"
                    style="min-width: 0px"
                  >
                    <!--span class="white--text headline">{{$auth.user.name.substr(0, 1).toUpperCase()}}</span-->
                    <span class="white--text headline">{{$auth.user.first_name.substr(0, 1)}}</span>
                  </v-avatar>
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>{{ $auth.user.first_name }}</v-list-item-title>
                  <!--v-list-item-subtitle>{{$auth.user.email}}</!--v-list-item-subtitle-->
                </v-list-item-content>
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-list dense>
              <v-list-item @click.stop="$auth.logout()">
                <v-list-item-icon>
                  <v-icon>mdi-logout-variant</v-icon>
                </v-list-item-icon>
                <v-list-item-title>Sign out</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card>
        </v-menu>
      </div>
      <v-btn
          v-else
          text
          height="100%"
          to="/login"
          class="text-capitalize font-weight-regular"
          >Sign in</v-btn>
    </v-toolbar-items>
  </v-app-bar>  
</template>
  
<script>
import Logobar from '@/components/Globals/Logobar' 
export default {
    components: {
      Logobar
    },  
    data() {
      return {
        title: 'Vuetify.js'
      }
    },
    methods: {
      toggle_menu() {
        console.log('top-toggleDrawer :' + this.$store.state.set_toggle_menu) 
        this.$store.commit('set_toggle_menu', !this.$store.state.set_toggle_menu)
      },
      menuClass(menu) {
       return menu.pages &&
         menu.pages.some((item) => this.$route.path.includes(item.to)) 
         ? ' primary--text'
         : ' grey--text text--darken-2' 
    },
    stringToColor(str) {
      var colors = [
        '#e51c23',
        '#e91e63',
        '#9c27b0',
        '#673ab7',
        '#3f51b5',
        '#5677fc',
        '#03a9f4',
        '#00bcd4',
        '#009688',
        '#259b24',
        '#8bc34a',
        '#afb42b',
        '#ff9800',
        '#ff5722',
        '#795548',
        '#607d8b',
      ]
      var hash = 0
      if (str.length === 0) return hash
      for (var i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash)
        hash = hash & hash
      }
      hash = ((hash % colors.length) + colors.length) % colors.length
      return colors[hash] 
    }, 

  }, 
  }
  </script>
  
  <style></style>