// import authHeader from "./auth-header";
import { getApi } from "../utils/axios";

class ProductService {
  getProducts() {
    return getApi.get("products/");
  }

  getProduct(id) {
    return getApi.get(`product/${id}`);
  }

  postProduct(data) {
    return getApi.post(`product/`, data);
  }

  putProduct(data, id) {
    return getApi.put(`product/${id}`, data);
  }

  patchProduct(data, id) {
    return getApi.patch(`product/${id}`, data, {
      // "X-CSRFToken": getApi.get("csrf/").then((res) => console.log(res.data)),
    });
  }

  deleteProduct(id) {
    return getApi.delete(`product/${id}`);
  }
}

export default new ProductService();
