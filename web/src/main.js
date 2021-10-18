import { FontAwesomeIcon } from "./plugins/font-awesome";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

// router.beforeEach((to, from, next) => {
//   if (to.matched.some((record) => record.meta.requiresLogin)) {
//     if (!store.getters["auth/loggedIn"]) {
//       next({ name: "Login" });
//     } else {
//       next();
//     }
//   } else {
//     next();
//   }
// });

router.beforeEach((to, from, next) => {
  const publicPages = ["/login", "/register", "/"];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem("user");

  // trying to access a restricted page + not logged in
  // redirect to login page
  if (authRequired && !loggedIn) {
    next("/login");
  } else {
    next();
  }
});

createApp(App)
  .use(store)
  .use(router)
  .component("font-awesome-icon", FontAwesomeIcon)
  .mount("#app");
