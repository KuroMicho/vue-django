const { getApi } = require("../utils/axios");

export default function authHeader() {
  let user = JSON.parse(localStorage.getItem("user"));
  if (!user) return {};

  const isTokenExpired = (token) =>
    Date.now() >= JSON.parse(atob(token.split(".")[1])).exp * 1000;

  if (user && user.access_token && !isTokenExpired(user.access_token)) {
    return { Authorization: "Bearer " + user.access_token };
  }

  if (isTokenExpired(user.access_token)) {
    getApi
      .post("login/refresh/", {
        refresh: user.refresh_token,
      })
      .then((res) => {
        if (res.data.access && res.data.refresh) {
          const pick = (obj, ...props) => {
            return props.reduce(function(result, prop) {
              result[prop] = obj[prop];
              return result;
            }, {});
          };
          const user_payload = pick(
            JSON.parse(localStorage.getItem("user")),
            "user",
            "msg"
          );
          const data = {
            ...user_payload,
            refresh_token: res.data.refresh,
            access_token: res.data.access,
          };
          localStorage.removeItem("user");
          localStorage.setItem("user", JSON.stringify(data));

          return { Authorization: "Bearer " + res.data.access_token };
        }
      });
  }
}
