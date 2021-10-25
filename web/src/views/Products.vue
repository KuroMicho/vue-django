<template>
  <div>
    <Navbar />
    <AlertCustom
      v-bind:alertIsShow="alertIsShow"
      :title="'Sucess Deleted'"
      :type="'success'"
      @close_alert="alertIsShow = false"
    />
    <ModalAdd
      v-bind:modalIsShow="modalIsShow"
      @close_modal="modalIsShow = false"
    />
    <button class="btn" @click="handleAddModal()">Add Product</button>
    <!-- <div class="products">
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
            <button @click="handleDelete(product.id)">Eliminar</button>
          </tbody>
        </table>
      </div> 
    </div> -->
    <pre>
      {{ JSON.stringify(products, null, 2) }}
    </pre>
    <el-table
      :data="
        products.filter(
          (product) =>
            !search || product.name.toLowerCase().includes(search.toLowerCase())
        )
      "
      style="width: 80%; margin: 0 auto;"
    >
      <el-table-column label="ID" prop="id" />
      <el-table-column label="Name" prop="name" />
      <el-table-column align="right">
        <template #header>
          <el-input v-model="search" size="mini" placeholder="Type to search" />
        </template>
        <template #default="scope">
          <el-button
            size="mini"
            @click="this.$router.push(`/product/${scope.row.id}/sales/`)"
          >
            Sales
          </el-button>
          <el-button
            size="mini"
            @click="this.$router.push(`/product/${scope.row.id}`)"
          >
            Editar
          </el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.row.id)"
            >Delete</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <pre>{{
      JSON.stringify(
        products
          .map((product) => {
            return { [product.name]: product.price };
          })
          .reduce(function(result, item) {
            var key = Object.keys(item)[0]; //first propertys
            result[key] = item[key];
            return result;
          }, {}),
        null,
        2
      )
    }}</pre>
    <line-chart
      :library="{ backgroundColor: '#222' }"
      ytitle="Price"
      label="Price"
      :data="
        products
          .map((product) => {
            return { [product.name]: product.price };
          })
          .reduce(function(result, item) {
            var key = Object.keys(item)[0]; //first property: a, b, c
            result[key] = item[key];
            return result;
          }, {})
      "
    ></line-chart>
  </div>
</template>
<script>
import { mapState, mapActions } from "vuex";
import Navbar from "../components/Navbar.vue";
import ModalAdd from "../components/ModalAdd.vue";
import AlertCustom from "../components/AlertCustom.vue";
import { ElTable, ElTableColumn, ElButton, ElInput } from "element-plus";
import "element-plus/es/components/table/style/css";
import "element-plus/es/components/table-column/style/css";
import "element-plus/es/components/button/style/css";
import "element-plus/es/components/input/style/css";

export default {
  name: "Products",
  data() {
    return {
      loading: false,
      modalIsShow: false,
      alertIsShow: false,
      search: "",
    };
  },
  components: {
    Navbar,
    ModalAdd,
    AlertCustom,
    ElTable,
    ElTableColumn,
    ElButton,
    ElInput,
  },
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
    this.$store.dispatch("products/getProducts");
  },
  methods: {
    ...mapActions("products", ["getProducts"]),
    async handleDelete(id) {
      this.$store
        .dispatch("products/deleteProduct", id)
        .then(() => (this.alertIsShow = true));
    },
    handleAddModal() {
      this.modalIsShow = true;
    },
  },
  emits: ["close_modal", "close_alert"],
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

.btn {
  color: white;
  cursor: pointer;
  background-color: lightcoral;
  border: none;
  border-radius: 10px;
  font-weight: bold;
  padding: 5px 15px;
  margin-top: 20px;
}
</style>
