<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawerComputed"
      :clipped="true"
      :mini-variant="!$vuetify.breakpoint.mobile && !drawer"
      :expand-on-hover="!$vuetify.breakpoint.mobile && !drawer"
      app
      class="grey lighten-5"
    >
      <v-list nav>
        <v-list-group
          v-for="menu in menus"
          :key="menu.title"
          :prepend-icon="`${menu.icon + menuClass(menu)}`"
          no-action
          :value="menu.active"
          active-class="grey--text text--darken-2"
        >
          <template v-slot:activator>
            <v-list-item-content :class="menuClass(menu)">
              <v-list-item-title
                v-text="menu.title"
                class="font-weight-medium"
              ></v-list-item-title>
            </v-list-item-content>
          </template>
          <v-list-item
            v-for="(item, i) in menu.pages"
            v-model="item.active"
            :key="i"
            :value="item.title"
            :to="item.to"
            :disabled="item.disabled"
            router
            dense
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon" small></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.title" />
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar :clipped-left="true" app dense flat dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <!--div class="mx-5">
        <app-logo />
      </!--div-->
      <v-spacer />
      <!--v-toolbar-items>
        <div v-if="$auth.loggedIn && $auth.user">
          <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <v-avatar
                :color="stringToColor($auth.user.name)"
                v-on="on"
                size="40"
                style="margin-top: 2px"
              >
                <span class="white--text headline">{{
                  $auth.user.name.substr(0, 1).toUpperCase()
                }}</span>
              </v-avatar>
            </template>

            <v-card>
              <v-list>
                <v-list-item>
                  <v-list-item-avatar>
                    <v-avatar
                      :color="stringToColor($auth.user.name)"
                      style="min-width: 0px"
                    >
                      <span class="white--text headline">{{
                        $auth.user.name.substr(0, 1).toUpperCase()
                      }}</span>
                    </v-avatar>
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <v-list-item-title>{{ $auth.user.name }}</v-list-item-title>
                    <v-list-item-subtitle>{{
                      $auth.user.email
                    }}</v-list-item-subtitle>
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
          >Sign in</v-btn
        >
      </v-toolbar-items-->
    </v-app-bar>

    <!--v-main>
      <v-container fluid>
        <v-breadcrumbs :items="path" class="pa-2">
          <template v-slot:item="{ item }">
            <v-breadcrumbs-item :to="item.to" nuxt exact>
              {{ item.page }}
            </v-breadcrumbs-item>
          </template>
        </v-breadcrumbs>
        <v-divider class="ma-2" />
        <app-alert />
        <nuxt />
      </v-container>
    </v-main-->

    <!--app-footer /-->
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'DefaultLayout',
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      menus: [
       // { icon: 'mdi-apps', title: 'Welcome', to: '/' },
       // { icon: 'mdi-chart-bubble', title: 'Inspire', to: '/inspire' },

        {id:1000, name:"หน้าแรก", title: 'หน้าแรก',icon: 'mdi-apps',isAuthen:true,
                  pages: [ {title: 'หน้าแรก1', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                           {title: 'หน้าแรก2', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                         ]  
        },
        {id:2000, name:"บทความ", title: 'บทความ',icon: 'mdi-chart-bubble',isAuthen:true, 
          pages: [ {title: 'บทความ1', icon: 'mdi-format-list-checks', to: '/post',isAuthen:true},
                    {title: 'บทความ2', icon: 'mdi-format-list-checks', to: '/post',isAuthen:true},
                  ]  
        },    
        {id:3000, name:"ผู้เขียน", title: 'ผู้เขียน',icon: 'mdi-database',isAuthen:true, 
          pages: [ {title: 'ผู้เขียน1', icon: 'mdi-format-list-checks', to: '/admin',isAuthen:true},
                    {title: 'ผู้เขียน2', icon: 'mdi-format-list-checks', to: '/admin',isAuthen:true},
                  ]  
        },

      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  },
  methods: {
    ...mapActions({ clearAlert: 'alert/clear' }),
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
  computed: {
    drawerComputed: {
      get() {
        return (
          !this.$vuetify.breakpoint.mobile ||
          (this.$vuetify.breakpoint.mobile && this.drawer)
        )
      },
      set(value) {
        this.drawer = value
      },
    },
    path: function () {
      let arrPath = this.$route.path.split('/').filter((it) => it)
      return arrPath.map((page, index) => {
        let path = '/' + arrPath.slice(0, index + 1).join('/')
        return {
          page,
          to:
            path == this.$route.path ||
            this.menus.some(
              (menu) => menu.pages && menu.pages.some((page) => page.to == path)
            )
              ? path
              : null,
        }
      })
    },
  },
}
</script>
