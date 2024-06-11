# **2. Real World Vue.JS3 (API de Composição)**

## **Este repositório possui um curso sobre a construção de uma _app_ Vue.JS 3**

Neste curso, criaremos um aplicativo de nível de produção usando Vue.JS versão 3. Começaremos criando o projeto usando o comando ``create-vue``. Em seguida, aprenderemos sobre componentes ``.vue`` e como eles podem ser usados para criar um aplicativo de página única (**Single Page Application**). Depois abordaremos os fundamentos do "**Vue Router**" para que possamos navegar entre as diferentes visualizações de nosso aplicativo e até mesmo buscar dados externos reais usando chamadas de API com o "**Axios**". Terminaremos aprendendo sobre o processo de construção e como implantar nosso aplicativo em produção.

## **IDE recomendado**

Vai-se utilizar o VSCode. Caso você ainda não o tenha [baixe-o](https://code.visualstudio.com/download), e depois instale-o.

Instale, também uma extensão do VSCode chamada [es6-string.html](https://marketplace.visualstudio.com/items?itemName=Tobermory.es6-string-html)


## **Tutorial 5. Chamadas de API Com Axios**

Nosso aplicativo está atualmente, funcionando assim: os eventos que estamos exibindo são simplesmente codificados dentro dos dados do componente ``EventListView.vue``. Em um _app_ do mundo real, provavelmente haveria algum tipo de banco de dados de eventos do qual estaríamos extraindo. Nosso aplicativo faria uma solicitação para os eventos, o servidor responderia com eles (em formato **JSON**), nós os pegaríamos e os definiríamos como dados de nosso componente (``ref``), que exibiríamos na nossa ``view``. A figura abaixo ilustra este processo.

![fetch_data_api_call](img_readme/fetch_data_api_call.jpg)

Portanto, nossas tarefas a serem executadas neste tutorial incluem:

* Criar um banco de dados fictício (_mock database_) para abrigar nossos eventos
* Instalar uma biblioteca (seu nome é **Axios**) para fazer as API Calls (Chamadas de API)
* Implementar uma chamada de API de nome ``getEvents()``
* Refatorar nosso código que trata da API em uma camada de serviço


### **Passo 1. Nosso Banco de Dados Fictício (Mock Data Base)**

Observe que existe um arquivo ``db.json`` no repositório do tutorial.

1.1 Abra o arquivo "**db.json**" e observe o conteúdo dele.

```javascript
{
  "events": [
    {
      "id": 123,
      "category": "animal welfare",
      "title": "Cat Adoption Day",
      "description": "Find your new feline friend at this event.",
      "location": "Meow Town",
      "date": "January 28, 2022",
      "time": "12:00",
      "organizer": "Kat Laydee"
    },
    {
      "id": 456,
      "category": "food",
      "title": "Community Gardening",
      "description": "Join us as we tend to the community edible plants.",
      "location": "Flora City",
      "date": "March 14, 2022",
      "time": "10:00",
      "organizer": "Fern Pollin"
    },
    {
      "id": 789,
      "category": "sustainability",
      "title": "Beach Cleanup",
      "description": "Help pick up trash along the shore.",
      "location": "Playa Del Carmen",
      "date": "July 22, 2022",
      "time": "11:00",
      "organizer": "Carey Wales"
    }
  ]
}
```

> Esse código deve parecer muito familiar para você, pois é uma versão **JSON** dos dados dos eventos que estão localizados em nosso componente ``EventListView.vue``. São eles que iremos buscar em breve com uma chamada de **API**.

Opcionalmente, você pode criar seu banco de dados. Para criá-lo, usaremos o website "**My JSON Server**", que é uma solução simples que não requer instalação. Só precisamos de um repositório **Github** com um arquivo ``db.json`` nele. 

Antes porém, convém fazer uma breve descrição do site "**My JSON Server**". De acordo com o Chat-GPT:

> O **My JSON Server** é um serviço online que permite criar uma **API REST** fake (i.e. simulada) usando apenas arquivos **JSON**. Com essa ferramenta, você pode criar _endpoints_ personalizados e disponibilizar dados fictícios neste formato (**JSON**). 

> O funcionamento do **My JSON Server** é bastante simples. Você faz o upload dos arquivos **JSON** contendo os dados que deseja disponibilizar através da API, e o serviço gera _endpoints_ correspondentes a esses arquivos. Estes _endpoints_ podem ser acessados por meio de URLs específicas, e você pode fazer requisições HTTP como **GET**, **POST**, **PUT**, **DELETE** para recuperar, adicionar, atualizar ou excluir dados simulados.

> Essa ferramenta é útil para desenvolvedores que desejam criar protótipos rápidos, realizar testes ou desenvolver aplicações que dependem de uma API externa. Com o **My JSON Server**, você pode simular uma API real com dados personalizados sem precisar criar um servidor completo para isso.

1.2 A fim de acessar nosso servidor fictício, digite na barra de endereço do seu browser o seguinte URL:

``my-json-server.typicode.com/{GithubUserName}/{RepoName}``

> Obviamente, se você estiver criando seu próprio arquivo **db.json** no repositório de sua própria conta do Github, preencha os espaços em branco para seu ``UserName`` e ``RepoName``. Ou seja, genericamente o URL será:

> Adicionando ``/events`` ao final do URL nos permite direcionar os dados dos eventos especificamente. Então o que usaremos em breve para fazer nossa chamada é: 

``https://my-json-server.typicode.com/Code-Pop/Real-World_Vue-3/events``


### **Passo 2. Axios Para Chamada de API**

Agora que temos nosso _mock database_ e sabemos qual URL chamar, estamos prontos para instalar uma biblioteca para nos ajudar a fazer as chamadas de API. Vamos usar a biblioteca **Axios**.

**Axios** é uma biblioteca JavaScript utilizada para fazer requisições HTTP a servidores a partir do ambiente do Vue.JS ou de qualquer outro aplicativo JavaScript. Ela é amplamente usada para realizar operações assíncronas, como recuperar dados de um servidor ou enviar dados para um servidor.

Surge a pergunta: porque estamos usando Axios? Além de ser popular, ela inclui várias características, incluindo:

* Solicitações GET, POST, PUT e DELETE
* Adiciona autenticação a cada solicitação
* Define tempos limite se as solicitações demorarem muito
* Configura padrões para cada solicitação
* Intercepta solicitações para criar _middleware_
* Lida com erros e cancela solicitações adequadamente
* Serializa e desserializa corretamente as solicitações e respostas

2.1 Digite na linha de comando para irmos à pasta raiz do nosso projeto:

```
cd vue_3_mundo_real
```

2.2 Agora digite o comando abaixo.

```
npm install axios
```

### **Passo 3. Implementando Axios Para Obter Eventos**

3.1 Para escrever nossa chamada de API, vamos para o componente ``EventListView.vue``, excluímos os dados dos eventos codificados (``events``) e vamos substituir por ``null``. Depois, importamos a biblioteca **Axios** e, em seguida, importamos/adicionamos o gancho do ciclo de vida ``onMounted`` (_lifecycle hook_). Portanto, abra o arquivo "**src/views/EventListView.vue**" e altere o seu conteúdo para o código abaixo.


```
<script setup>
import { ref, onMounted } from 'vue'
import EventCard from '@/components/EventCard.vue'
import axios from 'axios'

const events = ref(null)

onMounted(() => {
  // get events from mock db when component is created
  // obtém os eventos do banco de dados fictício quando o componente é criado
})
</script>

```

Mas, o que é _lifecycle hook_ no Vue.JS? De acordo com o Chat-GPT:

> É um método predefinido que é executado em uma determinada ordem, começando a partir da inicialização da instância do Vue até sua destruição. Cada instância do componente Vue passa por uma série de etapas de inicialização quando é criada, como configurar a observação de dados, compilar o modelo, montar a instância no DOM e atualizá-lo quando os dados mudam. Ao longo do caminho, ele também executa funções chamadas ganchos de ciclo de vida, dando aos usuários a oportunidade de adicionar seu próprio código em estágios específicos. 

> Você só precisa entender que um componente tem um ciclo de vida e diferentes ganchos (ou métodos) são executados nesses diferentes estágios de seu ciclo de vida. Por exemplo, antes de ser criado, quando for criado, antes de ser montado, quando for montado e assim por diante. Veja a figura abaixo.

![lifecycle_hooks](img_readme/lifecycle_hooks.jpg)

Observe na figura acima que existem oito (8) _lifecycle hooks_ no Vue.JS.

No nosso caso, queremos fazer nossa chamada de API e obter nossos eventos quando o componente estiver ``onMounted``, e, então vamos executar o método ``get`` disponível para nós no **Axios**, passando o URL "**my-json-server**" como argumento ( que é de onde se deseja obter).

3.2 Abra o arquivo "**src/views/EventListView.vue**" e substitua o seu código para o trecho que está abaixo.

```javascript
import { ref, onMounted } from 'vue'
import EventCard from '@/components/EventCard.vue'
import axios from 'axios'

const events = ref(null)

onMounted(() => {
  axios
    .get('https://my-json-server.typicode.com/Code-Pop/Real-World_Vue-3/events')
    .then((response) => {
      events.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
```
> Como o Axios é uma biblioteca baseada em promessa e é executado de forma assíncrona, precisamos aguardar esta tal promessa retornada da solicitação ``get`` para resolver antes de prosseguir. É por isso que adicionamos o ``.then``, que nos permite esperar pela resposta (i.e. ``response``) e definir nossa referência de eventos locais (i.e. ``local events ref``) igual a ela.

> Como queremos capturar quaisquer erros que ocorram, também adicionamos ``.catch`` e estamos apenas registrando o erro (i.e. ``error``) no console. Existem várias soluções em nível de produção para tratamento de erros, porém, esta atende às nossas necessidades para este tutorial. Veremos outras em um futuro próximo.

> Se verificarmos isso no navegador, veremos nossos eventos sendo exibidos, extraídos suavemente de nosso servidor fictício recém-implementado.



### **Passo 4. Reorganizando Nosso Código Em Uma Camada de Serviço**

Porém, existe um problema com nosso código. Atualmente, estamos importando o Axios para o componente ``EventListView.vue``. Mas no próximo tutorial vamos criar um novo componente, que exibe os detalhes do nosso evento. E ele também precisará fazer uma chamada de API. Se estivermos importando o Axios para cada componente que precisa dele, estaremos criando desnecessariamente uma nova instância do Axios cada vez que fizermos isso (ver figura abaixo). Com o código da API entrelaçado em todo o nosso aplicativo, isso fica confuso e torna nosso aplicativo mais difícil de depurar.

![problem_with_our_code](img_readme/problem_with_our_code.jpg)


4.1 Uma solução mais limpa e escalável é modularizar nosso código de API em uma camada de serviço. Para fazer isso, crie uma pasta chamada ``services`` em "**src**".

4.2 Agora crie um arquivo chamado "**src/services/EventService.js**" e coloque o conteúdo abaixo nele.

```javascript
import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'https://my-json-server.typicode.com/Code-Pop/Real-World_Vue-3',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getEvents() {
    return apiClient.get('/events')
  }
}
```

> Observe que na primeira linha do arquivo, que estamos importando o Axios. Abaixo disso, adicionamos uma constante chamada ``apiClient``, que contém uma instância do Axios. Como você pode ver, definimos um ``baseURL`` e algumas outras configurações para o Axios usar enquanto se comunica com nosso servidor.
> 
> E por fim, podemos exportar um método que obtém nossos eventos, usando nosso novo Axios ``apiClient``.

> Como você pode ver, ainda temos acesso ao método ``get`` do Axios e estamos passando ``'/events'`` como o argumento ao fazer essa chamada. Esta _string_ será adicionada ao nosso ``baseURL``, e então a requisição será feita para: ‘**https://my-json-server.typicode.com/Code-Pop/Real-World_Vue-3/events**’.

4.3 Em seguida, só precisamos fazer uso deste novo ``EventService`` em nosso componente ``EventListView.vue``, excluindo a importação do Axios, importando o ``EventService`` e executando sua chamada ``getEvents()``. Abra o arquivo "**src/views/EventListview.vue**" e substitua seu conteúdo para o que está abaixo.

```javascript
<script setup>
import { ref, onMounted } from 'vue'
import EventCard from '@/components/EventCard.vue'
~~import axios from 'axios'~~
import EventService from '@/services/EventService.js'

const events = ref(null)

onMounted(() => {
  EventService.getEvents()
    .then((response) => {
      events.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>

<template>
  <h1>Events For Good</h1>
  <div class="events">
    <EventCard v-for="event in events" :key="event.id" :event="event" />
  </div>
</template>

<style scoped>
.events {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
```

E com isso, refatoramos nosso código de API em uma camada de serviço modular. O refatoramento está ilustrado na figura abaixo.

![modular_layer_service](img_readme/modular_layer_service.jpg)


### **Passo 6. Fazendo o Fechamento**

6.1 Repita o procedimento efetuado no **Passo 3.10** do **Tutorial 3** para visualizarmos no browser o que acabamos de fazer no passo anterior. Você verá algo como a figura abaixo.

![example_app_t4](img_readme/example_app_t4.jpg)

Ao visualizar nossos eventos no browser, os ``EventCards` parecem clicáveis. Não seria legal se pudéssemos clicar neles e ver mais detalhes sobre esse evento? No próximo tutorial, aprenderemos como fazer isso usando as habilidades de roteamento dinâmico do **Vue Router**.