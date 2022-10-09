<template> 
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
      v-for="menu in my_authorize"
      :key="menu.title"
      :prepend-icon="`${menu.icon + menuClass(menu)}`"
      no-action
      :value="menu.active" 
      active-class="grey--text text--darken-2"
    >
      <template v-slot:activator>
        <v-list-item-content :class="menuClass(menu)" >
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
</template>
  
<script>
  export default {
    data () {
        return {  
          loading: true,
          //drawer: false,
          page: 'Request',
          menus :[]
        }
    },
    methods: {  
      menuClass(menu) {
       return menu.pages &&
         menu.pages.some((item) => this.$route.path.includes(item.to)) 
         ? ' primary--text'
         : ' grey--text text--darken-2' 
      },
    },
    computed: {
      drawer: {
        get() {
          console.log('side-drawer' + this.$store.state.drawer)  
          return this.$store.state.drawer
        },
        set(newVal) {
          this.$store.commit('set_drawer', newVal)
        }
      }, 
      my_authorize: {
        get() {
          console.log('my_authorize :' + this.$store.state.authorize) 
          return this.$store.state.authorize
        }, 
      },

    },
    mounted() {
    this.my_authorize.forEach((menu, mindex) => {
      let active = false
      menu.pages &&
        menu.pages.forEach((item, pindex) => { 
          this.my_authorize[mindex].pages[pindex].active = this.$route.path.includes(
            item.to
          )
          active = active || item.active 
        })
      this.my_authorize[mindex].active = active 
    })
  }, 
  }
  </script>
  
  <style></style>