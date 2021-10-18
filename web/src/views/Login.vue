<template>
  <div class="login">
    <div class="form-container">
      <img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWFvNll2oAoBW1Cvkpc8HkbVVxs8gA0xdij4-OKBCWwYcarQpJ9IokRiBamKXHDnVKkag&usqp=CAU"
        alt="logo gomoda"
      />
      <Form @submit="handleLogin" :validation-schema="schema">
        <div class="form-group">
          <div class="field-container">
            <i class="fa fa-user" />
            <Field
              name="username"
              placeholder=" username"
              type="text"
              class="form-control"
            />
          </div>
          <ErrorMessage name="username" class="error-feedback" />
        </div>
        <div class="form-group">
          <div class="field-container">
            <i class="fa fa-key" />
            <Field
              name="password"
              placeholder="password"
              type="password"
              class="form-control"
            />
          </div>
          <ErrorMessage name="password" class="error-feedback" />
        </div>
        <div class="form-group radio_option">
          <div v-for="role in roles" :key="role">
            <div>
              <label :for="role">{{ role }}</label>
              <Field
                type="radio"
                :value="role"
                name="role"
                class="form-control"
              />
            </div>
            <ErrorMessage name="role" class="error-feedback" />
          </div>
        </div>
        <div class="form-group">
          <button class="btn" :disabled="loading">
            <span v-show="loading"></span><span>Login</span>
          </button>
        </div>
        <div class="form-group">
          <div v-if="message" class="alert alert-danger">
            {{ message }}
          </div>
        </div>
      </Form>
    </div>
  </div>
</template>
<script>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";

export default {
  name: "Login",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
      username: yup.string().required("username is required!"),
      password: yup.string().required("password is required!"),
      role: yup.string().required("Please select your role!"),
    });
    return {
      loading: false,
      message: "",
      roles: ["is_staff", "is_vendor"],
      schema,
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/products/");
    }
  },
  methods: {
    handleLogin(user) {
      // console.log(user);
      this.loading = true;
      this.$store
        .dispatch("auth/login", user)
        .then(() => {
          this.$router.push({ name: "Products" });
        })
        .catch((error) => {
          this.loading = false;
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
        });
    },
  },
};
</script>
<style scoped>
.login {
  background-color: #6e5085;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
}

.form-container {
  background-color: white;
  padding: 10px 20px;
  width: 30vw;
  min-width: 375px;
  box-shadow: 0 2px 5px 1px rgba(0, 0, 0, 0.4);
  border-radius: 8px;
}

.form-container > img {
  height: 150px;
  width: 150px;
}
.field-container {
  width: 100%;
  position: relative;
  display: flex;
  align-items: center;
  margin-top: 30px;
  border: 1px solid gray;
}

.field-container i {
  position: absolute;
  left: 0;
  bottom: 0;
  padding: 10px 20px;
  border-right: 1px solid gray;
}

.form-group {
  width: 80%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.field-container input {
  width: 100%;
  padding: 10px 20px;
  outline: none;
  margin-left: 50px;
  border-left: none;
  border: none;
}

.field-container input::placeholder {
  color: black;
}

.field-container:focus-within {
  border: 1px solid violet;
  box-shadow: 0 0 3px 3px rgba(162, 71, 173, 0.2);
}

.radio_option {
  display: grid;
  margin-top: 20px;
  grid-template-columns: 1fr 1fr;
  grid-column-gap: 5px;
}

.radio_option > div > span {
  display: block;
  margin-top: 10px;
}

.form-group > span {
  display: block;
  margin-top: 10px;
  background-color: lightcoral;
  width: 100%;
  padding: 10px 5px;
  color: #fff;
}

button {
  background: lightcoral;
  height: 35px;
  line-height: 35px;
  width: 100%;
  border: none;
  outline: none;
  cursor: pointer;
  color: #fff;
  font-size: 1.1em;
  margin: 20px 0;
  transition: all 0.3s ease-in-out;
}

button:hover {
  background-color: rgb(224, 109, 109);
}
</style>
