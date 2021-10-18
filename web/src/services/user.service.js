import { getApi } from "../utils/axios";
import authHeader from "./auth-header";
// import Cookies from "js-cookie";

class UserService {
  getPublicContent() {
    return getApi.get("/");
  }

  getProfile() {
    return getApi.get("user/", { headers: authHeader() });
  }

  getUsers() {
    return getApi.get("users/", { headers: authHeader() });
  }

  getUser() {
    return getApi.get("users/:id", { headers: authHeader() });
  }
}

export default new UserService();
