<template>   
  <v-app  :style="{ background: '#e5e7e9' }">
    <v-main>
        <header>
            <v-row
                class="fill-height ma-0"
                align="center"
                justify="center"
            >  
                <v-img
                    max-width="80%" 
                    max-height="45%"
                    src="./assets/img/banner.png">
                </v-img> 
            </v-row>

        </header>
        <v-container>
           <nuxt />
        </v-container>
    </v-main>
   
  </v-app> 
</template>

<script>
</script>
