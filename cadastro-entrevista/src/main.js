import { createApp, h } from 'vue'
import routes from './routes'
import axios from 'axios'
import VueAxios from 'vue-axios'

const SimpleRouterApp = {
  data: () => ({
    currentRoute: window.location.pathname
  }),

  computed: {
    ViewComponent () {
      const matchingPage = routes[this.currentRoute] || '404'
      return require(`./pages/${matchingPage}.vue`).default
    }
  },

  render () {
    return h(this.ViewComponent)
  },

  created () {
    window.addEventListener('popstate', () => {
      this.currentRoute = window.location.pathname
    })
  }
}

let app = createApp(SimpleRouterApp)
app.use(VueAxios, axios).mount('#app')