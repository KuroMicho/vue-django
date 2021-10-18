<template>
  <div class="container">
    <Navbar />
    <ul v-for="user in users" :key="user">
      <table>
        <th>username</th>
        <th>name</th>
        <th>last name</th>
        <th>email</th>
        <th>vendor</th>
        <th>staff</th>
        <th><i class="fa fa-search"></i></th>
        <tbody>
          <td>
            {{ user.username }}
          </td>
          <td>
            {{ user.name }}
          </td>
          <td>
            {{ user.last_name }}
          </td>
          <td>
            {{ user.email }}
          </td>
          <td>
            {{ user.is_vendor }}
          </td>
          <td>
            {{ user.is_staff }}
          </td>
          <td class="edit" v-if="user && user.username">
            <router-link :to="`/users/${user.username}`">Editar</router-link>
            <div v-show="showModal" class="modal-route">
              <div class="modal-content">
                <router-view></router-view>
              </div>
            </div>
          </td>
        </tbody>
      </table>
    </ul>
    <span v-if="content">{{ content }}</span>
  </div>
</template>
<script>
// import { mapState } from "vuex";
import userService from "../services/user.service";
import Navbar from "../components/Navbar.vue";
export default {
  name: "Users",
  data() {
    return {
      users: [],
      content: "",
      showModal: false,
    };
  },
  components: { Navbar },
  watch: {
    $route: {
      immediate: true,
      handler: function(newVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      },
    },
  },
  created() {
    return userService
      .getUsers()
      .then((res) => {
        if (res.data.status == "success") {
          this.users = res.data.data;
        }
      })
      .catch((error) => {
        this.content = error.message;
      });
  },
};
</script>
<style scoped>
.container table {
  background-color: rgba(98, 59, 134, 0.459);
  padding: 10px 5px;
}

.container table th {
  background-color: rgba(102, 189, 160, 0.486);
  padding: 0px 20px;
}

.modal-route {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
}

.modal-content {
  width: 50%;
  position: absolute;
  background-color: #fff;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
