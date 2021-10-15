<template>
  <div>
    <router-link to="/products">X</router-link>
    <h2>product {{ product.id }}</h2>
    <span class="color" v-for="(color, index) in product.color" :key="index">
      {{ color }}
      <i
        class="fas fa-times"
        @click="removeColor({ productId: product.id, colorId: index })"
      ></i>
    </span>
  </div>
</template>
<script>
import { getApi } from "../utils/axios";
import { mapState } from "vuex";
// console.log(this.$route.params.id);
export default {
  name: "Product",
  data() {
    return {
      product: {},
    };
  },
  props: ["id"],
  computed: mapState(["APIData"]),
  created() {
    this.product = this.$store.state.APIData.filter(
      (product) => product.id == this.id
    )[0];
  },
  methods: {
    async removeColor({ productId, colorId }) {
      const colorPatched = {
        ...this.product,
        color: delete this.product.color[colorId]
          ? { ...this.product.color }
          : false,
      };
      getApi
        .patch(`/product/${this.id}`, colorPatched, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((res) => console.log(res.data));

      this.product.id == productId
        ? delete this.product.color[colorId]
        : this.product;
    },
    async onSubmit() {
      getApi
        .patch(`/products/${this.id}`, {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
        })
        .then((res) => {
          this.$store.state.APIData = res.data;
        });
    },
  },
};
</script>
<style scoped></style>
