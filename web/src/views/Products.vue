<template>
  <div>
    <Navbar />
    <div class="products">
      <div v-for="product in products" :key="product.id">
        <table>
          <th>id</th>
          <th>Nombre</th>
          <th>Descripcion</th>
          <th>Proveedor</th>
          <th><i class="fa fa-search"></i></th>
          <tbody>
            <td>
              {{ product.id }}
            </td>
            <td>
              {{ product.name }}
            </td>
            <td>
              {{ product.description }}
            </td>
            <td>SamsanTech</td>
            <router-link :to="`/products/${product.id}`">Editar</router-link>
          </tbody>
        </table>
      </div>
      <!-- <div class="edit">
        <div v-show="showModal" class="modal-route">
          <div class="modal-content">
            <router-view></router-view>
          </div>
        </div>
      </div> -->
    </div>
  </div>
</template>
<script>
import { mapState, mapActions } from "vuex";
import Navbar from "../components/Navbar.vue";
export default {
  name: "Products",
  data() {
    return {
      loading: false,
      showModal: false,
    };
  },
  components: { Navbar },
  // computed: {
  //   products() {
  //     return this.$store.state.products.products;
  //   },
  // },
  computed: { ...mapState("products", ["products"]) },
  watch: {
    $route: {
      immediate: true,
      handler: function(newVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      },
    },
  },
  mounted() {
    this.loading = true;
    // this.$store.dispatch("products/getProducts");
  },
  methods: {
    ...mapActions("products", ["getProducts"]),
  },
};
</script>
<style scoped>
.product {
  padding: 20px;
}

.product table {
  background-color: rgba(98, 59, 134, 0.459);
  padding: 10px 5px;
}

.product table th {
  background-color: rgba(102, 189, 160, 0.486);
  padding: 0px 20px;
}

.color {
  background-color: rgba(160, 46, 46, 0.63);
  color: white;
}

.color i {
  color: #444;
  cursor: pointer;
}

.edit {
  cursor: pointer;
}
</style>
