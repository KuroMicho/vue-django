<template>
  <div class="navbar">
    <router-link to="/">
      <img src="../assets/logo.png" alt="ecommerce gomoda" />
    </router-link>
    <ul>
      <li>
        <router-link to="/products">Productos</router-link>
        <router-link v-if="accessToken" to="/logout">Logout</router-link>
      </li>
    </ul>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  name: "Navbar",
  computed: mapState(["accessToken"]),
};
</script>
<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 200px;
  background-color: #ebbce2;
}

.navbar img {
  width: 50px;
  height: 50px;
  object-fit: contain;
}

.navbar ul {
  list-style: none;
}
.navbar ul li a {
  color: #333;
  text-decoration: none;
}
.navbar ul li a:not(a:last-of-type) {
  margin-right: 20px;
}
</style>
