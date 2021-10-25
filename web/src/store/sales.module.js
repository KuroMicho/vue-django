import SaleService from "../services/sales.service";

const initialState = {
  sales: [],
  sale: {},
};

export const sales = {
  namespaced: true,
  state: initialState,
  actions: {
    getSalesByProduct({ commit }, id) {
      return SaleService.getSalesByProduct(id)
        .then((res) => {
          commit("getSalesSuccess", res.data.data);
          return Promise.resolve();
        })
        .catch((error) => {
          commit("getSalesFailure");
          return Promise.reject(error);
        });
    },
  },
  mutations: {
    getSalesSuccess(state, sales) {
      state.sales = sales;
    },
    getSalesFailure(state) {
      state.sales = null;
    },
  },
};
