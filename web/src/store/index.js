import { createStore } from "vuex";
import { getApi } from "../utils/axios.js";

const store = createStore({
  state: {
    accessToken: null,
    refreshToken: null,
    APIData: "",
  },
  getters: {
    loggedIn(state) {
      return state.accessToken != null;
    },
  },
  mutations: {
    updateStorage(state, { access, refresh }) {
      (state.accessToken = access), (state.refreshToken = refresh);
    },
    destroyToken(state) {
      state.accessToken = null;
      state.refreshToken = null;
    },
  },
  actions: {
    userLogin(context, usercredentials) {
      return new Promise((resolve, reject) => {
        getApi
          .post("/api-token/", {
            username: usercredentials.username,
            password: usercredentials.password,
          })
          .then((response) => {
            context.commit("updateStorage", {
              access: response.data.access,
              refresh: response.data.refresh,
            });
            resolve();
          })
          .catch((err) => {
            console.log(err);
            reject();
          });
      });
    },
    userLogout(context) {
      if (context.getters.loggedIn) {
        context.commit("destroyToken");
      }
    },
  },
});

export default store;
