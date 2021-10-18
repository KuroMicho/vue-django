<template>
  <div class="container">
    <Navbar />
    <h1>{{ user }}</h1>
    <p>{{ user.is_vendor }}</p>
  </div>
</template>
<script>
import { mapState } from "vuex";
import Navbar from "../components/Navbar.vue";

export default {
  name: "Profile",
  computed: mapState(["user"]),
  components: { Navbar },
};
</script>
<style scoped>
.container {
  background-color: gray;
  color: white;
}
</style>
