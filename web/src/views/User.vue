<template>
  <div class="container">
    <router-link to="/users">
      <i class="fa fa-times" />
    </router-link>
    <h2>
      {{ id }}
    </h2>
  </div>
</template>
<script>
export default {
  name: "User",
  props: {
    id: String,
  },
};
</script>
<style scoped></style>
