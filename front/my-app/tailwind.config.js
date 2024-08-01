/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      screens: {
        'tall': {'raw': '(min-height: 1520px)'},
      },
      colors: {
        // https://coolors.co/palette/a41623-f85e00-ffb563-ffd29d-918450
        // palettes:{ 1: '#A41623', 2: '#F85E00', 3:'FFB563', 4:'#FFD29D', 5: '#918450'},

        // https://coolors.co/palette/3d348b-7678ed-f7b801-f18701-f35b04
        palettes:{ 1: '#3D348B', 2: '#7678ED', 3:'#F7B801', 4:'#F18701', 5: '#F35B04'},

        // flowbite-svelte
        primary: { 50: '#FFF5F2', 100: '#FFF1EE', 200: '#FFE4DE', 300: '#FFD5CC', 400: '#FFBCAD', 500: '#FE795D', 600: '#EF562F', 700: '#EB4F27', 800: '#CC4522', 900: '#A5371B'},
      },
      height: {
        '90': '90%'
      }
    }
  },
  plugins: []
};