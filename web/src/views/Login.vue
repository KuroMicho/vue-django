<template>
  <div class="login">
    <div>
      <h1>please sign in</h1>
      <p v-if="incorrectAuth">
        Incorrect username or password entered - please try again
      </p>
    </div>
    <form @submit="login">
      <div class="form-group">
        <input type="text" placeholder="Input username..." v-model="username" />
      </div>
      <div class="form-group">
        <input
          type="password"
          placeholder="Input password..."
          v-model="password"
        />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      incorrectAuth: false,
    };
  },
  methods: {
    login(e) {
      e.preventDefault();
      this.$store
        .dispatch("userLogin", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.$router.push({ name: "Products" });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
    },
  },
};
</script>
<style scoped>
.login {
  background-color: #f4f4f4;
  margin-top: 10%;
}

.form-group input {
  padding: 25px 10px;
}
</style>
