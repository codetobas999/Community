<template>
  <v-app dark>
  <!--Side Bar Menu -->
  <v-navigation-drawer
    v-model="drawer"
    :clipped="true" 
    :mini-variant="!$vuetify.breakpoint.mobile && !drawer"
    :expand-on-hover="!$vuetify.breakpoint.mobile && !drawer"
    app
    class="grey lighten-4"
  >
  <v-list nav>
    <v-list-group  
      v-for="menu in my_menus"
      :key="menu.page.menu_name_th"
      :prepend-icon="`${menu.page.icon + menuClass(menu)}`"
      no-action
      :value="menu.active" 
      active-class="grey--text text--darken-2"
    >
      <template v-slot:activator>
        <v-list-item-content :class="menuClass(menu)" >
          <v-list-item-title
            v-text="menu.page.menu_name_th"
            class="font-weight-medium" 
          ></v-list-item-title>
        </v-list-item-content>
      </template>

      <v-list-item
        v-for="(item, i) in menu.page_subs"
        v-model="item.active"
        :key="i"
        :value="item.menu_sub_name_th"
        :to="item.to"
        :disabled="item.disabled"
        router
        dense
      >
        <v-list-item-icon>
          <v-icon v-text="item.icon" small></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title v-text="item.menu_sub_name_th" />
        </v-list-item-content>
      </v-list-item>
    </v-list-group>
  </v-list>
</v-navigation-drawer>
<!--Side Bar Menu -->

     <!--Top Bar Menu-->
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <!--
      <v-btn icon @click.stop="miniVariant = !miniVariant">
        <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
      </v-btn>
      
      <v-btn icon @click.stop="clipped = !clipped">
        <v-icon>mdi-application</v-icon>
      </v-btn> 
      <v-btn icon @click.stop="fixed = !fixed">
        <v-icon>mdi-minus</v-icon>
      </v-btn>      
      -->
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <!--
      <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
      -->
      <v-list-item-avatar @click.stop="rightDrawer = !rightDrawer">
                  <v-avatar
                    :color="stringToColor($auth.user.first_name)"
                    style="min-width: 0px"
                  >
                    <!--span class="white--text headline">{{$auth.user.name.substr(0, 1).toUpperCase()}}</span-->
                    <span class="white--text headline">{{$auth.user.first_name.substr(0, 1)}}</span>
                  </v-avatar>
       </v-list-item-avatar>

    </v-app-bar>
    <!--Top Bar Menu-->
    <!--Content -->
    
    <v-main>
      <v-container fluid >          
        <nuxt />
      </v-container>
    </v-main>
   
    <!--  
    <v-content>
      <v-container>
        <nuxt></nuxt>
      </v-container>
    </v-content>
    -->
    <!--Content -->
    <!--TOP Right Bar Menu-->
    <v-navigation-drawer v-model="rightDrawer" :right="right" temporary fixed>
      <v-list>
        <v-list-item @click.stop="$auth.logout()">
          <v-list-item-action>
            <v-icon light>mdi-logout-variant</v-icon>
          </v-list-item-action>
          <v-list-item-title >Sign out</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <!--TOP Right Bar Menu-->
    <!---->
    
    <!-- 
    <v-footer :fixed="fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
    -->
   <!--Foot Bar Menu-->    
    <v-footer padless>
    <v-col class="text-center pa-0 overline" cols="12">
      <span style="font-size: 0.6rem">&copy; {{ year }} - Version {{ version }}</span>
    </v-col>
  </v-footer> 
   <!--Foot Bar Menu-->
  </v-app>
</template>

<script>
import { version } from '~/package.json'
import * as Common from '@/utils/common'
export default { 
  data() {
    return {  
      my_menus: [],
      clipped: true,
      miniVariant: true,
      right: true,
      rightDrawer: false,
      title: 'Demo รักษาสัตว์'
    }
  },
  /*mounted() {
    console.log('state', this.$nuxt.$store.state)
    this.getmenu()
  },*/
  mounted() {
    //console.log('state', this.$nuxt.$store.state)
    this.getmenu()
    this.my_menus.forEach((menu, mindex) => {
      let active = false
      menu.pages &&
        menu.pages.forEach((item, pindex) => {
          this.menus[mindex].pages[pindex].active = this.$route.path.includes(
            item.to
          )
          active = active || item.active
        })
      this.menus[mindex].active = active
    })
  },
  methods: {  
      async getmenu(){
        const data = await Common.getMenus()
        //console.log("typeof data");
        //console.log(typeof data);
        //console.log(data);
        this.my_menus = data
        //console.log('menu', data)
      },
      menuClass(menu) {
       return menu.page_subs &&
         menu.page_subs.some((item) => this.$route.path.includes(item.to)) 
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
    version: () => version,
    year: () => new Date().getFullYear(), 
    /*my_menus() { 
          console.log('my_menus :' + this.$nuxt.$store.state.menus) 
          return this.$nuxt.$store.state.menus
        },  */
    drawer: {
      get() {
        //console.log('GET DRAWER :', this.$nuxt.$store.state.drawer) 
        return this.$nuxt.$store.state.drawer
      },
      set(val) {
        //Common.writelog('SET DRAWER(OLD VAL) :' +  this.$nuxt.$store.state.drawer , 9)
        //console.log('SET DRAWER(OLD VAL) :', this.$nuxt.$store.state.drawer)
        //console.log('SET DRAWER(NEW VAL) :', val)
        this.$store.commit('set_drawer', val)
        //console.log('SET DRAWER(IN STATE) :', this.$nuxt.$store.state.drawer)
      }
    },
    fixed: {
      get() {
        return this.$nuxt.$store.state.fixed
      },
      set(val) {
        //console.log('OLD VAL', this.$nuxt.$store.state.fixed)
        //console.log('NEW VAL', val)
        this.$store.commit('set_fixed', val)
        //console.log('NEW DRAWER STATE', this.$nuxt.$store.state.fixed)
      }
    },
   
  }
}
</script>