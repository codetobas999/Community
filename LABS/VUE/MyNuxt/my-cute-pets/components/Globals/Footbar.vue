<template> 
  <v-footer padless>
    <v-col class="text-center pa-0 overline" cols="12">
      <span style="font-size: 0.6rem">&copy; {{ year }} - Version {{ version }}</span>
    </v-col>
  </v-footer>  
</template>
  
<script>
 import { version } from '~/package.json'
export default {
    computed: {
      version: () => version,
      year: () => new Date().getFullYear(),
    },
  }
</script>