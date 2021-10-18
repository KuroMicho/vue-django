import ProductService from "../services/product.service";

export const products = {
  namespaced: true,
  state: {
    products: [],
    product: null,
    retrieved: false,
  },
  actions: {
    async getProducts({ commit }) {
      return ProductService.getProducts()
        .then((res) => {
          commit("getProductsSuccess", res.data.data);
          return Promise.resolve();
        })
        .catch((error) => {
          commit("getProductsFailure");
          return Promise.reject(error);
        });
    },
    async getProduct({ commit }, id) {
      return ProductService.getProduct(id)
        .then((res) => {
          commit("getProductSuccess", res.data.data);
          return Promise.resolve();
        })
        .catch((error) => {
          commit("getProductFailure");
          return Promise.reject(error);
        });
    },
    // async patchProduct({ commit }, data, id) {
    //   return ProductService.patchProduct(data, id)
    //     .then((res) => {
    //       commit("patchProductSuccess", res.data.data);
    //       return Promise.resolve();
    //     })
    //     .catch((error) => {
    //       commit("patchProductFailure");
    //       return Promise.reject(error);
    //     });
    // },
    async putProduct({ commit }, { data, id }) {
      return ProductService.putProduct(data, id)
        .then((res) => {
          commit("putProductSuccess", res.data.data);
          return Promise.resolve();
        })
        .catch((error) => {
          commit("putProductFailure");
          return Promise.reject(error);
        });
    },
  },
  mutations: {
    getProductsSuccess(state, products) {
      state.products = products;
      state.retrieved = true;
    },
    getProductSuccess(state, product) {
      state.product = product;
      state.retrieved = true;
    },
    putProductSuccess(state, product) {
      state.product = product;
    },
    patchProductSuccess(state, product) {
      state.product = product;
    },
    getProductsFailure(state) {
      state.products = null;
      state.retrieved = false;
    },
    getProductFailure(state) {
      state.product = null;
      state.retrieved = false;
    },
    putProductFailure(state) {
      state.retrieved = false;
    },
    patchProductFailure(state) {
      state.retrieved = false;
    },
  },
};
