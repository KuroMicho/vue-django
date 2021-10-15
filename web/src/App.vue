<template>
  <div class="app">
    <!-- <router-view @pull_color="pullColor" :products="products"></router-view> -->
    <router-view></router-view>
  </div>
</template>

<script>
// import { getApi } from "./utils/axios";
// import { mapState } from "vuex";
export default {
  name: "App",
  // data() {
  //   return {
  //     products: [],
  //   };
  // },
  // computed: mapState(["APIData"]),
  // methods: {
  //   pullColor({ productId, colorId }) {
  //     const product = this.APIData.find((product) => product.id == productId);

  //     const colorPatch = {
  //       ...product,
  //       color: delete product.color[colorId] ? { ...product.color } : false,
  //     };
  //     getApi
  //       .patch("/product/", colorPatch)
  //       .then((res) => console.log(res.data));

  //     this.APIData.map((product) =>
  //       product.id == productId ? delete product.color[colorId] : product
  //     );
  //   },
  // },
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
