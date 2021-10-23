<template>
  <div class="modal">
    <div class="modal__content">
      <EditForm class="form" @submit="handleSubmit">
        <div class="form__header">
          <h3>Edit Product:</h3>
          <router-link to="/products">
            <i class="fa fa-times" />
          </router-link>
        </div>
        <div class="form__body">
          <Field type="text" name="barcode" v-model="product.barcode" />
          <Field v-model="product.name" name="name" type="text" />
          <Field type="text" name="image" v-model="product.image" />
          <Field
            type="textarea"
            name="description"
            v-model="product.description"
          />
          <Field as="select" name="color" @change="handleColorOption">
            <option :value="null" selected>-- Please select an color --</option>
            <option value="azul">azul</option>
            <option value="negro">negro</option>
            <option value="blanco">blanco</option>
            <option value="rosado">rosado</option>
          </Field>
          <span
            class="color"
            v-for="(color, index) in product.color"
            :key="index"
          >
            {{ color }}
            <i
              class="fas fa-times"
              @click="removeColor({ colorId: index })"
            ></i>
          </span>
          <Field type="text" name="size" v-model="product.size" />
          <Field type="text" name="material" v-model="product.material" />
          <Field type="number" name="price" v-model="product.price" />
          <Field
            type="text"
            name="minimum_required"
            v-model="product.minimum_required"
          />
          <ErrorMessage name="minimum_required" />

          <button type="submit" class="btn btn--update">Update</button>
          <span class="error-feedback">{{ content }}</span>
        </div>
      </EditForm>
    </div>
  </div>
</template>
<script>
// import { getApi } from "../utils/axios";
// import userService from "../services/user.service";
import { Form as EditForm, Field, ErrorMessage } from "vee-validate";
import { mapState, mapActions } from "vuex";
// import * as yup from "yup";
export default {
  name: "Product",
  data() {
    return {
      loading: false,
      content: "",
    };
  },
  components: { EditForm, Field, ErrorMessage },
  props: ["id"],
  computed: { ...mapState("products", ["product"]) },
  mounted() {
    this.loading = true;
    // this.getProduct(this.id);
    this.$store.dispatch("products/getProduct", this.id);
  },
  methods: {
    ...mapActions("products", ["getProduct"]),
    async removeColor({ colorId }) {
      const colorPatched = {
        color: delete this.product.color[colorId]
          ? { ...this.product.color }
          : false,
      };
      this.$store
        .dispatch("products/patchProduct", { data: colorPatched, id: this.id })
        .then(() => {
          alert("color deleted");
        });
      this.product.id == this.id
        ? delete this.product.color[colorId]
        : this.product;
    },
    async handleColorOption(opt) {
      let colorObj = {};
      if (Object.keys(this.product.color).length == 0) {
        colorObj = Object.assign({ 0: opt.target.value });
        return (this.product.color = colorObj);
      }
      if (Object.values(this.product.color).includes(opt.target.value))
        return alert("Color already choosed!");
      const colors = Object.keys(this.product.color);
      const size = colors.length - 1;
      colorObj = {
        ...this.product.color,
        [Number(colors[size]) + 1]: opt.target.value,
      };
      this.product.color = colorObj;
    },
    async handleSubmit(product) {
      const { color, ...others } = product;
      console.info(color);
      const data = { color: this.product.color, ...others };

      this.$store
        .dispatch("products/putProduct", { data: data, id: this.id })
        .then(() => this.$router.push("/products/"))
        .catch((error) => {
          console.error(error.body);
        });
    },
  },
};
</script>
<style scoped>
.modal {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background: rgba(189, 93, 93, 0.5);
  z-index: 1000;
}

.modal__content {
  width: 80vw;
  max-width: 600px;
  position: absolute;
  background-color: #fff;
  top: 50%;
  left: 50%;
  border-radius: 8px;
  transform: translate(-50%, -50%);
}

.form__header {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
}

.form__header > i {
  cursor: pointer;
}

.form {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: column;
  padding: 15px 20px;
}

.form__body {
  margin-top: 20px;
  width: 60%;
  min-width: 300px;
  display: flex;
  flex-direction: column;
}
</style>
