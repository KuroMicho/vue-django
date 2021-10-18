import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/Home.vue";
import Products from "../views/Products.vue";
import Product from "../views/Product.vue";
import Login from "../views/Login.vue";
import Logout from "../views/Logout.vue";
import Profile from "../views/Profile.vue";
import Users from "../views/Users.vue";
import User from "../views/User.vue";

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
    // meta: {
    //   requiresLogin: true,
    // },
    // children: [
    //   {
    //     path: ":id",
    //     component: Product,
    //     props: true,
    //     meta: {
    //       showModal: true,
    //     },
    //   },
    // ],
  },
  {
    path: "/products/:id",
    name: "Product",
    component: Product,
    props: true,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/user",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/users",
    name: "Users",
    component: Users,
    children: [
      {
        path: ":id",
        component: User,
        props: true,
        meta: {
          showModal: true,
        },
      },
    ],
  },
  {
    path: "/logout",
    name: "Logout",
    component: Logout,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
