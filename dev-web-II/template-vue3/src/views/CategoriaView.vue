<script setup>
import { ref, reactive, onMounted } from "vue";
import CategoriasApi from "@/api/categorias";
const categoriasApi = new CategoriasApi();

const defaultCategoria = { id: null, descricao: "" };
const categorias = ref([]);
const categoria = reactive({ ...defaultCategoria });

onMounted(async () => {
  categorias.value = await categoriasApi.buscarTodasAsCategorias();
});

function limpar() {
  Object.assign(categoria, { ...defaultCategoria });
}

async function salvar() {
  if (categoria.id) {
    await categoriasApi.atualizarCategoria(categoria);
  } else {
    await categoriasApi.adicionarCategoria(categoria);
  }
  categorias.value = await categoriasApi.buscarTodasAsCategorias();
  limpar();
}

function editar(categoria_para_editar) {
  Object.assign(categoria, categoria_para_editar);
}

async function excluir(id) {
  await categoriasApi.excluirCategoria(id);
  categorias.value = await categoriasApi.buscarTodasAsCategorias();
  limpar();
}
</script>

<template>
  <div class="container">
    <h1>Categorias</h1>
    <div class="form">
      <input type="text" v-model="categoria.descricao" placeholder="Descrição" />
      <button @click="salvar">Salvar</button>
      <button @click="limpar">Limpar</button>
    </div>
    <ul class="categoria-list">
      <li v-for="categoria in categorias" :key="categoria.id">
        <span @click="editar(categoria)">
          ({{ categoria.id }}) - {{ categoria.descricao }}
        </span>
        <button @click="excluir(categoria.id)">Excluir</button>
      </li>
    </ul>
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

.form {
  display: flex;
  gap: 10px;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
}

input[type="text"] {
  padding: 12px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 250px;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: border-color 0.3s;
}

input[type="text"]:focus {
  border-color: #343a40;
  outline: none;
}

button {
  padding: 12px 25px;
  font-size: 1rem;
  background-color: #343a40;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #000;
}

.categoria-list {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 100%;
  max-width: 500px;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}

li span {
  cursor: pointer;
  font-size: 1.1rem;
}

li span:hover {
  color: #343a40;
}

li button {
  padding: 8px 12px;
  font-size: 0.9rem;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  transition: background-color 0.3s;
}

li button:hover {
  background-color: #c0392b;
}

@media (max-width: 600px) {
  .form {
    flex-direction: column;
    gap: 10px;
  }

  input[type="text"] {
    width: 100%;
  }

  ul {
    padding: 0;
  }
}
</style>
