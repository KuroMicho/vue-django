<template>
  <div class="logout"></div>
</template>
<script>
export default {
  created() {
    this.$store.dispatch("auth/logout").then(() => {
      this.$router.push({ name: "Login" });
    });
  },
};
</script>
