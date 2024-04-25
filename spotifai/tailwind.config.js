/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage:{
        "college-drop:": "url(https://i.scdn.co/image/ab67616d0000b27325b055377757b3cdd6f26b78)"
      }
    },
  },
  plugins: [],
}