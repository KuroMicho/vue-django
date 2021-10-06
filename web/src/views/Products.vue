<template>
  <div>
    <Navbar />
    <div class="products">
      <div v-for="product in APIData" :key="product.id">
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
            <!-- <td
              class="color"
              v-for="(color, index) in product.color"
              :key="index"
            >
              {{ color }}
              <i
                class="fas fa-times"
                @click="
                  $emit('pull_color', { productId: product.id, colorId: index })
                "
              ></i>
            </td> -->
            <td class="edit" v-if="product && product.id">
              <router-link :to="`/products/${product.id}`">Editar</router-link>
              <div v-show="showModal" class="modal-route">
                <div class="modal-content">
                  <router-view></router-view>
                </div>
              </div>
              <!-- <p @click="this.$route.push({})">editar</p> -->
              <!-- <router-link
                :to="{
                  name: 'Product',
                  params: { id: product.id, product: product },
                }"
                >Edit</router-link
              > -->
            </td>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
import Navbar from "../components/Navbar.vue";
import { getApi } from "../utils/axios";
import { mapState } from "vuex";
export default {
  name: "Products",
  props: {
    products: Array,
  },
  data() {
    return {
      showModal: false,
    };
  },
  components: { Navbar },
  computed: mapState(["APIData"]),
  // onidle() {
  //   this.$store.dispatch("userLogout").then(() => {
  //     this.$router.push({ name: "Login" });
  //   });
  // },
  watch: {
    $route: {
      immediate: true,
      handler: function(newVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      },
    },
  },
  created() {
    getApi
      .get("/products/", {
        headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
      })
      .then((res) => {
        this.$store.state.APIData = res.data;
      })
      .catch((err) => {
        console.error(err);
        this.$router.push({ name: "Login" });
      });
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

.modal-route {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
}

.modal-content {
  width: 50%;
  position: absolute;
  background-color: #fff;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
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
