<template>
  <div class="modal">
    <div class="moda-content">
      <div class="product" v-if="product">
        <router-link to="/products">
          <i class="fa fa-times" />
        </router-link>
        <form>
          <h2>details: {{ product?.name }}</h2>
          <input type="text" name="barcode" :value="product?.barcode" />
          <input type="text" name="name" :value="product?.name" />
          <input type="text" name="image" :value="product.image" />
          <input
            type="textarea"
            name="description"
            :value="product.description"
          />
          <!-- <Field as="select" name="color" @change="handleColorOption">
        <option :value="null" disabled>-- Please select an color --</option>
        <option value="azul">azul</option>
        <option value="negro">negro</option>
        <option value="blanco">blanco</option>
        <option value="rosado">rosado</option>
      </Field> -->
          <!-- <span class="color" v-for="(color, index) in product.color" :key="index">
        {{ color }}
        <i class="fas fa-times" @click="removeColor({ colorId: index })"></i>
      </span> -->
          <input type="text" name="size" :value="product.size" />
          <input type="text" name="material" :value="product.material" />
          <input type="number" name="price" :value="product.price" />
          <input
            type="number"
            name="minimum_required"
            :value="product.minimum_required"
          />

          <button type="submit" class="btn-update">Update</button>
          <span class="error-feedback">{{ content }}</span>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
// import { getApi } from "../utils/axios";
// import userService from "../services/user.service";
import { mapState, mapActions } from "vuex";
// import { Field, Form } from "vee-validate";
export default {
  name: "Product",
  data() {
    return {
      loading: false,
      content: "",
    };
  },
  // components: { Field, Form },
  props: ["id"],
  computed: { ...mapState("products", ["product"]) },
  mounted() {
    this.loading = true;
    this.getProduct(this.id);
  },
  methods: {
    ...mapActions("products", ["getProduct"]),
  },
  // methods: {
  //   async removeColor({ colorId }) {
  //     const colorPatched = {
  //       color: delete this.product.color[colorId]
  //         ? { ...this.product.color }
  //         : false,
  //     };
  //     this.$store
  //       .dispatch("products/patchProduct", colorPatched, this.id)
  //       .then((res) => {
  //         console.log(res.data);
  //       });
  //     this.product.id == this.id
  //       ? delete this.product.color[colorId]
  //       : this.product;
  //   },
  //   async handleColorOption(opt) {
  //     let colorObj = {};
  //     if (Object.keys(this.product.color).length == 0) {
  //       colorObj = Object.assign({ 0: opt.target.value });
  //       return (this.product.color = colorObj);
  //     }
  //     if (Object.values(this.product.color).includes(opt.target.value))
  //       return alert("Color already choosed!");
  //     const colors = Object.keys(this.product.color);
  //     const size = colors.length - 1;
  //     colorObj = {
  //       ...this.product.color,
  //       [Number(colors[size]) + 1]: opt.target.value,
  //     };
  //     this.product.color = colorObj;
  //   },
  //   async handleSubmit(product) {
  //     const { color, ...others } = product;
  //     console.warn(color);
  //     const data = { color: this.product.color, ...others };

  //     this.$store
  //       .dispatch("products/putProduct", { data: data, id: this.id })
  //       .catch((error) => {
  //         this.content = error.message;
  //       });
  //   },
  // },
};
</script>
<style scoped>
.modal {
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

.product form {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.product form input {
  margin-top: 20px;
  width: 100%;
}
</style>
