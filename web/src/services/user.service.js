import { getApi } from "../utils/axios";
// import authHeader from "./auth-header";

class UserService {
  getProfile() {
    return getApi.get("user/");
  }

  getUsers() {
    return getApi.get("users/");
  }

  // getUser() {
  //   return getApi.get("users/:id", { headers: authHeader() });
  // }
}

export default new UserService();
