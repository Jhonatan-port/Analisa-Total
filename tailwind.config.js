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
        '96vh' : '96vh',
        
      },
      minHeight: {
        '86vh' : '86vh'
      }
    },
  },
  plugins: [],
}
