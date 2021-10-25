import { getApi } from "../utils/axios";
import tokenService from "./token.service";

class AuthService {
  login(user) {
    return getApi
      .post("login/", {
        username: user.username,
        password: user.password,
      })
      .then((res) => {
        if (res.data.access_token) {
          if (res.data.user[user.role]) {
            // localStorage.setItem("user", JSON.stringify(res.data));
            tokenService.setUser(res.data);
            return res.data;
          } else {
            throw new Error("You are not allowed login with this role");
          }
        }
      });
  }

  logout() {
    // localStorage.removeItem("user");
    return getApi
      .post("logout/", {
        refresh_token: tokenService.getLocalRefreshToken(),
      })
      .then(() => {
        // console.log("here");
        tokenService.removeUser();
      });
  }

  register(user) {
    return getApi.post("register/", {
      username: user.username,
      email: user.email,
      password: user.password,
    });
  }
}

export default new AuthService();
