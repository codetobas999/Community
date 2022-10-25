<template> 
  <v-app> 
    <Sidebar></Sidebar>
    <Topbar></Topbar>
    <v-main class="grey lighten-8">
      <v-container fluid >
        <v-divider class="ma-2" />        
        <app-alert />          
        <nuxt />
      </v-container>
    </v-main>  
    <Footbar></Footbar>
  </v-app>

</template>

<script>
import Sidebar from '@/components/Globals/Sidebar'
import Topbar from '@/components/Globals/Topbar'
import Footbar from '@/components/Globals/Footbar'  
export default {
  name: 'MainLayout',
  components: {
    Sidebar,
    Topbar,
    Footbar 
  },  
}
</script>