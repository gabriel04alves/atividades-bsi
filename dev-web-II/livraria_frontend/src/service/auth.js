import axios from "axios";

export default class AuthService {
  async postUserToken(token) {
    const response = await axios.get("/usuarios/me/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  }
}
