<template>
  <div>
    <div>
      <label>Email <input v-model="fields.email"/></label>
    </div>
    <br>
    <div>
      <label>Password <input v-model="fields.password"/></label>
    </div>
    <div>
      <button type="button" @click="getLogin">Entrar</button>
    </div>
  </div>
</template>

<script>
export default {

  name: 'PaginaLogin',
  components: {},
  mixins: [],
  data: () => ({
    fields: {}
  }),

  computed: {},
  watch: {},
  asyncData() {
  },
  fetch() {
    // The `fetch` method is used to fill the store before rendering the page
  },
  head() {
    return {
      bodyAttrs: {
        class: 'layout-navbar-fixed  sidebar-collapse'
      },
      title: `Detalles de transacciones`,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'Page 1 description'
        }
      ]
    }
  },
  mounted() {
  },
  created() {
  },
  methods: {
    async getLogin() {
      this.procesando = true
      const url = `/api/v1/login`
      await this.axios
          .post(url, this.fields)
          .then((resp) => {
            console.log(resp.data)
          })
          .catch((e) => {
            console.log(e)
          })
    }
  }
}
</script>
<style scoped></style>