import axios from "axios";

const getApi = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 8000,
  withCredentials: true,
  xsrfHeaderName: "x-csrftoken",
  xsrfCookieName: "csrftoken",
});

export { getApi };
