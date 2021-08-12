import _axios from "./plugins/axios";
import {createApp} from "vue";
import aplicacion from "./App.vue";
import VueAxios from "vue-axios";
import router from './router'


const app = createApp({
    el: "#app",
    delimiters: ["[[", "]]"],
    components: {
        aplicacion,
    },
    data() {
        return {
            dato: "Componente de VueJS 3",
        };
    },
}).use(router);
app.use(VueAxios, _axios)
app.mount("#app");
