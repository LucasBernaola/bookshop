import { createApp } from 'vue'
import axios from 'axios'
import App from './App.vue'
import store from './store'
import { registerPlugins } from '@/plugins'
import 'vuetify/dist/vuetify.css';

const app = createApp(App)

registerPlugins(app)

app.config.globalProperties.$axios = axios;

app.use(store);

app.mount('#app')
