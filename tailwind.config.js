/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'btn-padrao' : '#0497aa',
        'btn-padrao-hover' : '#074a53'
      },
      height: {
        'semi-screen' : '80vh'
      },
    },
  },
  plugins: [],
}
