import authHeader from "./auth-header";
import { getApi } from "../utils/axios";

class ProductService {
  getProducts() {
    return getApi.get("products/", { headers: authHeader() });
  }

  getProduct(id) {
    return getApi.get(`products/${id}`, { headers: authHeader() });
  }

  putProduct(data, id) {
    return getApi.put(`products/${id}`, data, {
      headers: authHeader(),
    });
  }

  patchColor(data, id) {
    return getApi.patch(`products/${id}`, data, {
      headers: authHeader(),
      // "X-CSRFToken": getApi.get("csrf/").then((res) => console.log(res.data)),
    });
  }
}

export default new ProductService();
