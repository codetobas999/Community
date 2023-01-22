// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    app: {
      head: {
        htmlAttrs: {
          lang: 'en'
        },
        bodyAttrs: {
          class: 'demo'
        },
        charset: 'utf-8',
        titleTemplate: '%s | IT Genius Engineering',
        meta: [
          {
            name: 'author',
            content: 'IT Genius Engineering Ltd., Thailand'
          },
          {
            name: 'viewport',
            content: 'width=device-width, initial-scale=1, maximum-scale=5'
          }
        ]
      }
    },
    modules: [
      'nuxt-icon'
    ],
    css: ['~/assets/css/main.css'],
    postcss: {
        plugins: {
          tailwindcss: {},
          autoprefixer: {},
        },
    },
    // modules: [
    //   [
    //     '@nuxtjs/robots',
    //     {
    //       UserAgent: "*",
    //       Disallow: "",
    //     }
    //   ],
    // ]
})
