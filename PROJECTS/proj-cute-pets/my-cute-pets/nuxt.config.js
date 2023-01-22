import colors from 'vuetify/es5/util/colors'

const config = require('./config')

export default {
  env: {
    config
  },
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - my-cute-pets',
    title: 'my-cute-pets2',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  //plugins: [{src: '~/plugins/import-validate.js'}],
   // {src: '~/plugins/import-validate.js', mode: 'client'}
   plugins: [  
      //"~/plugins/vee-validate"
    ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth', 
  ],

  router: {
    //base: '/tooleasy/web/',
    middleware: ['auth']
  },
  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  /*vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },*/
  vuetify: {
    // customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        light: {
          primary: '#8dc63f',
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  axios: {
    baseURL: 'http://localhost:8000/api/v1',
    credentials: true
  },
  
  auth: {
    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: 'access_token',
          // type: 'JWT',
          maxAge: 60// * 60,
        },
        refreshToken: {
          property: 'refresh_token',
          data: 'refresh_token',
          maxAge: 60// * 60 * 24 * 30
        },
        endpoints: {
          login: { 
                  url: '/auth/login', 
                  method: 'post', 
                  propertyName: 'access_token' 
                 },
          user:  { 
                  url: '/users/me', 
                  method: 'get',
                  propertyName: 'data.user' 
                 }, 
          logout: { 
                    url: '/auth/logout', 
                    method: 'post'  
          },
          //logout: false
          //logout: { url: 'logout', method: 'delete', propertyName: 'data.user' },
        }  
      }
    },
    redirect: {
      login: '/login' 
    }
  },
  
  

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
