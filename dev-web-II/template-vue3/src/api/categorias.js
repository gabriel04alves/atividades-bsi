import axios from "axios";
export default class CategoriasApi {
  async buscarTodasAsCategorias() {
    const { data } = await axios.get("/categorias/");
    return data.results;
  }
  async adicionarCategoria(categoria) {
    const { data } = await axios.post("/categorias/", categoria);
    return data.results;
  }
  async atualizarCategoria(categoria) {
    const { data } = await axios.put(`/categorias/${categoria.id}/`, categoria);
    return data.results;
  }
  async excluirCategoria(id) {
    const { data } = await axios.delete(`/categorias/${id}/`);
    return data.results;
  }
}
