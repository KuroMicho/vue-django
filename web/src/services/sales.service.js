import { getApi } from "../utils/axios";
// import authHeader from "./auth-header";

class SaleService {
  //   getAllSales

  postSale(id) {
    return getApi.post(`product/${id}/sale/`);
  }

  getSalesByProduct(id) {
    return getApi.get(`product/${id}/sales/`);
  }
}

export default new SaleService();
