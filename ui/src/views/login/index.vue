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
      <label>Password <input v-model="fields.password"/></label>
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
  methods: {}
}
</script>
<style scoped></style>