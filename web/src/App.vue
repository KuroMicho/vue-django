<template>
  <div class="app">
    <router-view @pull_color="pullColor" :products="products"></router-view>
  </div>
</template>

<script>
import { getApi } from "./utils/axios";
export default {
  name: "App",
  data() {
    return {
      products: [],
    };
  },
  methods: {
    pullColor({ productId, colorId }) {
      const product = this.products.find((product) => product.id == productId);

      const colorPatch = {
        ...product,
        color: delete product.color[colorId] ? { ...product.color } : false,
      };
      getApi
        .patch("/product/", colorPatch)
        .then((res) => console.log(res.data));

      this.products.map((product) =>
        product.id == productId ? delete product.color[colorId] : product
      );
    },
  },
  // created() {
  //   getApi
  //     .get("/products/")
  //     .then((res) => (this.products = res.data))
  //     .catch((err) => console.log(err));
  // },
};
</script>

<style>
*,
*::before,
*::after {
  box-sizing: inherit;
  padding: 0;
  margin: 0;
}

html {
  box-sizing: border-box;
}

body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}
</style>
