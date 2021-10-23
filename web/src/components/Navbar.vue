<template>
  <div class="navbar">
    <router-link to="/">
      <img src="../assets/logo.png" alt="ecommerce gomoda" />
    </router-link>
    <ul>
      <li>
        <router-link v-show="!user" to="/login">Login</router-link>
        <router-link v-show="!user" to="/register">Register</router-link>

        <router-link v-if="user.is_vendor || user.is_staff" to="/products"
          >Productos</router-link
        >
        <router-link v-if="user.is_staff" to="/purchases"
          >Purchases</router-link
        >
        <router-link v-if="user.is_staff" to="/users">Users</router-link>
        <router-link v-if="user" to="/user">Profile</router-link>
        <router-link v-if="user" to="/logout">Logout</router-link>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: "Navbar",
  data() {
    return { user: 0 };
  },
  mounted() {
    this.user = this.$store.state.auth.user.user;
  },
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
