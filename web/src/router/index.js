import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/Home.vue";
import Products from "../views/Products.vue";
import Product from "../views/Product.vue";
import Login from "../views/Login.vue";
import Profile from "../views/Profile.vue";
import Users from "../views/Users.vue";
import User from "../views/User.vue";
import Sales from "../views/Sales.vue";

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
    path: "/product/:id",
    name: "Product",
    component: Product,
    props: true,
  },
  {
    path: "/product/:id/sales",
    name: "Sales",
    component: Sales,
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
    path: "/:pathMatch(.*)*", //will match everything and put it under `$route.params.pathMatch`
    name: "not-found",
    redirect: "/",
    // component: NotFound,
  },
  {
    path: "/product/:afterProduct(.*)", //will match everything and put it under `$route.params.pathMatch`
    redirect: "/",
    // component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
