import tokenService from "../services/token.service";
import { getApi } from "./axios";

const setup = (store) => {
  getApi.interceptors.request.use(
    (config) => {
      const token = tokenService.getLocalAccessToken();
      if (token) {
        config.headers["Authorization"] = "Bearer " + token;
        // config.headers["x-access-token"] = token; // for Node.js Express back-end
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  getApi.interceptors.response.use(
    (res) => {
      return res;
    },
    async (error) => {
      const originalConfig = error.config;

      if (originalConfig.url !== "/login/" && error.response) {
        // Access Token was expired

        if (error.response.status === 401 && !originalConfig._retry) {
          originalConfig._retry = true;

          try {
            const rs = await getApi.post("login/refresh/", {
              refresh: tokenService.getLocalRefreshToken(),
            });
            console.info(rs);

            const { access } = rs.data;

            store.dispatch("auth/refreshToken", access);
            tokenService.updateLocalAccessToken(access);

            return getApi(originalConfig);
          } catch (_error) {
            return Promise.reject(_error);
          }
        }
      }
      return Promise.reject(error);
    }
  );
};

export default setup;
