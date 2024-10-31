<script setup>
import { onMounted, ref } from 'vue';
import { PassageUser } from '@passageidentity/passage-elements/passage-user';
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();
const psg_auth_token = ref('');
const copyMessageVisible = ref(false);

const getUserInfo = async () => {
  try {
    const authToken = localStorage.getItem('psg_auth_token');
    const passageUser = new PassageUser(authToken);
    const user = await passageUser.userInfo(authToken);
    psg_auth_token.value = authToken;
    if (user) {
      await authStore.setToken(authToken);
    } else {
      authStore.unsetToken();
    }
  } catch (error) {
    authStore.unsetToken();
  }
};

const copyToClipboard = () => {
  navigator.clipboard.writeText(psg_auth_token.value).then(() => {
    copyMessageVisible.value = true;
    setTimeout(() => {
      copyMessageVisible.value = false;
    }, 2000);
  }).catch(err => {
    console.error('Erro ao copiar o token: ', err);
  });
};

onMounted(() => {
  getUserInfo();
});
</script>

<template>
  <div class="container">
    <button @click="copyToClipboard">Copiar token de autenticação</button>
    <p v-if="copyMessageVisible" class="copy-message">Token copiado com sucesso!</p>
    <p>{{ psg_auth_token }}</p>
  </div>
</template>

<style scoped>
body {
  font-family: 'Arial', sans-serif;
  background-color: #f4f4f9;
  margin: 0;
  padding: 0;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start; /* Alinha o conteúdo ao topo */
  min-height: 100vh;
  padding: 20px;
}

p {
  font-size: 1rem;
  color: #555;
  text-align: center;
  background-color: #fff;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  word-break: break-all;
  margin: 10px auto; /* Ajustado o margin para 10px */
}

button {
  display: block;
  margin: 0 auto 20px; /* Removido o espaço extra acima do botão */
  padding: 12px 25px;
  background-color: #343a40;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #000;
  color: #fff;
}

.copy-message {
  text-align: center;
  color: #4CAF50;
  margin-top: 10px;
  font-weight: bold;
  animation: fadeInOut 2s ease-in-out;
}

@keyframes fadeInOut {
  0% { opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { opacity: 0; }
}

@media (max-width: 600px) {
  .container {
    padding: 15px;
  }

  p {
    padding: 15px;
    max-width: 90%;
  }
}
</style>
