const defaultTheme = require('tailwindcss/defaultTheme')
const colors = require('tailwindcss/colors')

const primary = colors.blue
const secondary = colors.pink
const info = colors.sky
const warning = colors.amber
const success = colors.emerald
const error = colors.red

module.exports = {
  mode:'jit',
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./app.vue",
  ],
  theme: {
    extend: {
      colors: {
        primary,
        secondary,
        info,
        warning,
        success,
        error
      },
      textColor: {
        skin: {
          base: 'var(--color-text-base)',
          muted: 'var(--color-text-muted)',
          active: 'var(--color-text-active)',
          hover: 'var(--color-text-hover)',
          icon: 'var(--color-text-icon)',
        },
      },
      backgroundColor: {
        skin: {
          'fill': 'var(--color-fill)',
          'fill-active': 'var(--color-fill-active)',
          'fill-hover': 'var(--color-fill-hover)',
          'icon-fill': 'var(--color-icon-fill)',
        },
      },
      fontFamily: {
        sans: ['Poppins', ...defaultTheme.fontFamily.sans]
      }
    },
  },
  plugins: [],
}
