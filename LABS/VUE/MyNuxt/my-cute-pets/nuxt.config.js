import colors from 'vuetify/es5/util/colors'

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - my-cute-pets',
    title: 'my-cute-pets',
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
  plugins: [
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
    '@nuxtjs/auth'
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

  /*axios: {
    //baseURL: 'http://127.0.0.1:8888/api',
    baseURL: 'http://localhost:12345/api',
    credentials: false//true
  },*/
  
  auth: {
    redirect: {
      login: '/login' //ถ้าไม่ Login ให้ Redirect มาที่หน้า Login
    },
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
          login: { url: 'http://localhost:12345/api/login', 
                   method: 'post', 
                   propertyName: 'data.token' //เป็น Structure ของ Data ที่ Return
                 },
          user:  { url: 'http://localhost:12345/api/me', 
                   method: 'get', 
                   propertyName: 'data.user' 
                 },
          logout: false  
        }
        /*
        endpoints: {
          login:  { url: 'https://sakko-demo-api.herokuapp.com/api/v1/user/sign_in ', 
                    method: 'post', 
                    propertyName: 'user.auth_jwt' //เป็น Structure ของ Data ที่ Return
                  },
          logout: { url: 'https://sakko-demo-api.herokuapp.com/api/v1/user/sign_out ', 
                    method: 'delete'   
                  },
          user:   { url: 'https://sakko-demo-api.herokuapp.com/api/v1/user/me', 
                    method: 'get', 
                    propertyName: 'user' 
                  } 
        },
        tokenName: 'auth-token' //https://auth.nuxtjs.org/schemes/local/#usage
        
        */
        /*
        sign_in={
                  "user":{
                    "email": "xxx@gmial.com",
                    "password": "12345"
                  }                  
                }
        */        

      }
    } 

  },
  
  

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
