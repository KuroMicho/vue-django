<template>
  <div v-show="modalIsShow" class="modal">
    <div class="modal__content">
      <AddForm class="form" aria-describedby="add form" @submit="handleSubmit">
        <div class="form__header">
          <h3>Add Product:</h3>
          <i class="fa fa-times" @click="$emit('close_modal')" />
        </div>
        <div class="form__body">
          <div class="form__group">
            <label for="barcode">Barcode:</label>
            <Field type="text" name="barcode" />
          </div>
          <div class="form__group">
            <label for="name">Name:</label>
            <Field type="text" name="name" />
          </div>
          <div class="form__group">
            <label for="image">Image Url:</label>
            <Field type="url" name="image" />
          </div>
          <div class="form__group">
            <label for="description">Description:</label>
            <Field type="textarea" name="description" />
          </div>
          <div class="form__group">
            <label for="color">Color:</label>
            <Field as="select" name="color" @change="handleColorOption">
              <option :value="null" selected
                >-- Please select an color --</option
              >
              <option value="azul">azul</option>
              <option value="negro">negro</option>
              <option value="blanco">blanco</option>
              <option value="rosado">rosado</option>
            </Field>
          </div>
          <span>{{ color }}</span>
          <!-- <span class="color" v-for="(color, index) in product.color" :key="index">
      {{ color }}
      <i class="fas fa-times" @click="removeColor({ colorId: index })"></i> -->
          <!-- </span> -->
          <div class="form__group">
            <label for="size">Size:</label>
            <Field as="select" name="size" @change="handleSizeOption">
              <option :value="null" selected
                >-- Please select an size --</option
              >
              <option value="XS">XS</option>
              <option value="S">S</option>
              <option value="M">M</option>
              <option value="L">L</option>
            </Field>
          </div>
          <div class="form__group">
            <label for="material">Material:</label>
            <Field as="select" name="material" @change="handleMaterialOption">
              <option :value="null" selected
                >-- Please select an material --</option
              >
              <option value="Algodon">Algodon</option>
              <option value="Cuero">Cuero</option>
              <option value="Seda">Seda</option>
              <option value="Sintetico">Sintetico</option>
            </Field>
          </div>
          <div class="form__group">
            <label for="price">Price:</label>
            <Field type="number" name="price" />
          </div>
          <div class="form__group">
            <label for="minimum_required">Minimum Required:</label>
            <Field type="text" name="minimum_required" />
            <ErrorMessage name="minimum_required" />
          </div>

          <button class="btn btn--add" type="submit">Add</button>
          <span class="error-feedback">{{ content }}</span>
        </div>
      </AddForm>
    </div>
  </div>
</template>
<script>
import { Form as AddForm, Field, ErrorMessage } from "vee-validate";

export default {
  name: "ModalAdd",
  data() {
    return { content: "", color: null, size: null, material: null };
  },
  props: {
    modalIsShow: {
      type: Boolean,
    },
  },
  components: { AddForm, Field, ErrorMessage },
  methods: {
    handleSubmit(data) {
      const { color, size, material, ...restData } = data;
      console.info(color, size, material);
      const newData = {
        color: this.color,
        size: this.size,
        material: this.material,
        ...restData,
      };
      this.$store
        .dispatch("products/postProduct", newData)
        .then(() => {
          alert("product added");
        })
        .catch((error) => {
          this.content = error;
        });
    },
    async handleColorOption(opt) {
      let colorObj = {};
      if (this.color == null) {
        colorObj = Object.assign({ 0: opt.target.value });
        return (this.color = colorObj);
      }
      if (Object.values(this.color).includes(opt.target.value))
        return alert("Color already choosed!");
      const colors = Object.keys(this.color);
      const size = colors.length - 1;
      colorObj = {
        ...this.color,
        [Number(colors[size]) + 1]: opt.target.value,
      };
      this.color = colorObj;
    },
    async handleSizeOption(opt) {
      let sizeObj = {};
      if (this.size == null) {
        sizeObj = Object.assign({ 0: opt.target.value });
        return (this.size = sizeObj);
      }
      if (Object.values(this.size).includes(opt.target.value))
        return alert("size already choosed!");
      const sizes = Object.keys(this.size);
      const size = sizes.length - 1;
      sizeObj = {
        ...this.size,
        [Number(sizes[size]) + 1]: opt.target.value,
      };
      this.size = sizeObj;
    },
    async handleMaterialOption(opt) {
      let materialObj = {};
      if (this.material == null) {
        materialObj = Object.assign({ 0: opt.target.value });
        return (this.material = materialObj);
      }
      if (Object.values(this.material).includes(opt.target.value))
        return alert("Material already choosed!");
      const materials = Object.keys(this.material);
      const size = materials.length - 1;
      materialObj = {
        ...this.material,
        [Number(materials[size]) + 1]: opt.target.value,
      };
      this.material = materialObj;
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
  background: rgba(0, 0, 0, 0.5);
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
}

.form__group {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.form__group > input,
.form__group > select {
  margin-top: 10px;
  border-radius: 8px;
  width: 50%;
  padding: 5px 15px;
  border: 1px solid gray;
  outline: none;
}

.form__group > select {
  cursor: pointer;
}

.btn {
  color: white;
  cursor: pointer;
  background-color: lightcoral;
  border: none;
  border-radius: 10px;
  font-weight: bold;
  padding: 5px 15px;
  margin-top: 20px;
}

.form__body > span {
  display: block;
  margin-top: 5px;
}
</style>
