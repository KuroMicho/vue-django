import { getApi } from "../utils/axios";

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
            localStorage.setItem("user", JSON.stringify(res.data));
            return res.data;
          } else {
            throw new Error("You are not allowed login with this role");
          }
        }
      });
  }

  logout() {
    localStorage.removeItem("user");
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
