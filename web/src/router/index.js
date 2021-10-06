import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/Home.vue";
import Products from "../views/Products.vue";
import Product from "../views/Product.vue";
import Login from "../views/Login.vue";
import Logout from "../views/Logout.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/products",
    name: "Products",
    component: Products,
    meta: {
      requiresLogin: true,
    },

    children: [
      {
        path: ":id",
        component: Product,
        props: true,
        meta: {
          showModal: true,
        },
      },
    ],
  },
  // {
  //   path: "/products/:id",
  //   name: "Product",
  //   component: Product,
  //   props: true,
  // },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/logout",
    name: "Logout",
    component: Logout,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
