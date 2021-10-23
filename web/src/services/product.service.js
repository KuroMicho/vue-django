import authHeader from "./auth-header";
import { getApi } from "../utils/axios";

class ProductService {
  getProducts() {
    return getApi.get("products/", { headers: authHeader() });
  }

  getProduct(id) {
    return getApi.get(`products/${id}`, { headers: authHeader() });
  }

  postProduct(data) {
    return getApi.post(`product/`, data, { headers: authHeader() });
  }

  putProduct(data, id) {
    return getApi.put(`products/${id}`, data, {
      headers: authHeader(),
    });
  }

  patchProduct(data, id) {
    return getApi.patch(`products/${id}`, data, {
      headers: authHeader(),
      // "X-CSRFToken": getApi.get("csrf/").then((res) => console.log(res.data)),
    });
  }

  deleteProduct(id) {
    return getApi.delete(`products/${id}`, {
      headers: authHeader(),
    });
  }
}

export default new ProductService();
