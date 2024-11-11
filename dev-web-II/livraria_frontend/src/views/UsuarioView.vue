<script setup>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();
const usuario = computed(() => authStore.user);

const formatDate = (dateString) => {
  if (!dateString) return null;
  const date = new Date(dateString);
  return date.toLocaleString('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  });
};
</script>

<template>
  <div class="container" v-if="usuario">
    <h1>Informações do Usuário</h1>
    <div class="user-info">
      <img v-if="usuario.foto && usuario.foto.url" :src="usuario.foto.url" alt="Foto do usuário" class="user-photo" />
      <img v-else src="https://via.placeholder.com/150" alt="Sem foto" class="user-photo" />

      <p>Nome: <strong>{{ usuario.name }} </strong></p>
      <p>Email: <strong>{{ usuario.email }}</strong></p>
      <p>ID: <strong>{{ usuario.id }}</strong></p>
      <p>Superuser: <strong> {{ usuario.is_superuser ? 'Sim' : 'Não' }}</strong></p>
      <p>Ativo:<strong>  {{ usuario.is_active ? 'Sim' : 'Não' }}</strong></p>
      <p>Staff: <strong> {{ usuario.is_staff ? 'Sim' : 'Não' }}</strong></p>
      <p>Último Login: <strong> {{ formatDate(usuario.last_login) || 'Nunca logado' }}</strong></p>
      <!-- <p>Grupos: <strong> {{ usuario.groups.join(', ') }}</strong></p> -->
      <p>Grupos: <strong>{{ usuario.groups.map(group => group.name).join(', ') }}</strong></p>

    </div>
  </div>
  <div class="container" v-else>
    <p>Carregando informações do usuário...</p>
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
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
}

h1 {
  font-size: 1.5rem;
  color: #343a40;
  margin-bottom: 30px;
  text-align: center;
}

.user-info {
  background-color: #fff;
  padding: 30px;
  border-radius: 10px;
  max-width: 500px;
  margin: 0 auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.user-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  display: block;
  margin: 0 auto 20px;
}

p {
  font-size: 1.1rem;
  margin-bottom: 10px;
  color: #555;
}

strong {
  color: #333;
}

@media (max-width: 600px) {
  .user-info {
    padding: 20px;
  }

  h1 {
    font-size: 2rem;
  }

  p {
    font-size: 1rem;
  }
}
</style>
