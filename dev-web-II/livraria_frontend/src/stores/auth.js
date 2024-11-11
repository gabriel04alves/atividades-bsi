import { ref } from 'vue';
import { defineStore } from 'pinia';

import AuthService from '@/service/auth';
const authService = new AuthService();

export const useAuthStore = defineStore('auth', () => {
  const user = ref({});
  const loggedIn = ref(false);

  async function setToken(token) {
    user.value = await authService.postUserToken(token);
    loggedIn.value = true;
  }

  function unsetToken() {
    user.value = {};
    loggedIn.value = false;
  }

  return { user, loggedIn, setToken, unsetToken };
});
