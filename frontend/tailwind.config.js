/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {}
  },
  daisyui: {
    themes: ['bumblebee']
  },
  plugins: [
    require('daisyui'),
    require('@tailwindcss/forms')
  ]
}
