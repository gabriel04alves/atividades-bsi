# **2. Real World Vue.JS3 (API de Composição)**

## **Este repositório possui um curso sobre a construção de uma _app_ Vue.JS 3**

Neste curso, criaremos um aplicativo de nível de produção usando Vue.JS versão 3. Começaremos criando o projeto usando o comando ``create-vue``. Em seguida, aprenderemos sobre componentes ``.vue`` e como eles podem ser usados para criar um aplicativo de página única (**Single Page Application**). Depois abordaremos os fundamentos do "**Vue Router**" para que possamos navegar entre as diferentes visualizações de nosso aplicativo e até mesmo buscar dados externos reais usando chamadas de API com o "**Axios**". Terminaremos aprendendo sobre o processo de construção e como implantar nosso aplicativo em produção.

## **IDE recomendado**

Vai-se utilizar o VSCode. Caso você ainda não o tenha [baixe-o](https://code.visualstudio.com/download), e depois instale-o.

Instale, também uma extensão do VSCode chamada [es6-string.html](https://marketplace.visualstudio.com/items?itemName=Tobermory.es6-string-html)


## **Tutorial 6. Roteamento Dinâmico**

Neste tutorial, vamos adicionar a funcionalidade onde um usuário pode clicar em qualquer um dos ``EventCards`` exibidos em nossa página inicial (``Home``) e ser direcionado para uma exibição que mostra mais detalhes sobre esse evento. Em outras palavras: vamos implementar algum comportamento de roteamento dinâmico. Abordaremos esse novo recurso em duas partes. 

* **Parte 1**: Clicar em um evento e fazer uma chamada de API para buscá-lo com todos os seus detalhes. O evento será buscado pelo seu ``id``, porém estático.

* **Parte 2**: Tornar o comportamento do roteamento mais dinâmico. Isto é, pode-se clicar em qualquer um dos eventos e ele será buscado via chamada da API, porém o seu ``id`` muda o endereço do URL dinamicamente.


Para a **Parte 1**, portanto, nossas tarefas a serem executadas são:

* Criar um novo componente ``EventDetailsView`` para exibir os detalhes do evento

* Adicionar uma nova chamada de API para buscar um único evento pelo seu `id` (este é o evento do qual exibiremos os detalhes)

* Adicionar uma rota para o novo componente ``EventDetailsView``

* Tornar ``EventCard`` clicável para que possamos acessar esta nova rota chamada ``EventDetailsView``


##Parte 1

### **Passo 1. Criando O Componente ``EventDetailsView``**


1.1 Crie um arquivo chamado "**src/views/EventDetailsView.vue**" e adicione o conteúdo abaixo nele.

```javascript
<script setup>
import { ref, onMounted } from 'vue'

const event = ref(null)

onMounted(() => {
  // fetch event (by id) and set local event data
  // busca o evento (por id) e define os dados do evento local
  
})
</script>

<template>
  <div>
    <h1>{{ event.title }}</h1>
    <p>{{ event.time }} on {{ event.date }} @ {{ event.location }}</p>
    <p>{{ event.description }}</p>
  </div>
</template>
```


> Esse código renderiza os detalhes do evento ``ref``. Esse evento é recuperado de uma chamada de API que o busca pelo seu ``id``. Vamos revisitar nosso banco de dados simulado para ver como buscá-lo.

> Observe o que acontece quando chamamos nosso URL "**my-json-server**", desta vez com um ``id``no final dele (**…/events/123**). Isso tem como alvo um único evento, onde seu ``id`` corresponde ao final do nosso URL: ``123``. Veja a figura abaixo.

![url_api_call](img_readme/url_api_call.jpg)

> Este é o tipo de URL que usaremos ao buscar um único evento, onde termina com o ``id` do evento. Vamos entrar em nosso arquivo ``EventService`` e adicionar essa chamada de API agora.

1.2 Abra o arquivo "**src/services/EventService.js**" e adicione o conteúdo abaixo nele.

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
  },
  //Added new call
  getEvent(id) {
    return apiClient.get('/events/' + id)
  }
}
```

> A chamada ``getEvent`` é muito semelhante à chamada ``getEvents`` do último tutorial. No entanto, ela recebe um ``id`` como argumento, que é anexado ao final do URL para o qual estamos fazendo uma solicitação ``get``.

Agora que a chamada ``getEvent`` está pronta para uso, vamos usá-la em nosso novo componente ``EventDetailsView``.

1.3 Abra o arquivo "**src/views/EventDetailsView.vue**" e altere o seu conteúdo para o que está abaixo.

```javascript
import { ref, onMounted } from 'vue'
import EventService from '@/services/EventService.js'

const event = ref(null)
const id = ref(123)

onMounted(() => {
  EventService.getEvent(id.value)
    .then((response) => {
      event.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
```

> Algumas coisas a serem observadas acima:

* Estamos chamando ``getEvent`` do ``EventService``, que agora importamos para o componente
* Estamos passando ``id.value`` - Esse ``id`` é atualmente apenas um valor de dados embutido em código. (Faremos essa dinâmica na Parte 2 deste tutorial. Essa não é nossa solução final.)
* Estamos definindo nossa referência (``ref``) do ``event`` local igual à resposta de nossa solicitação ``getEvent``

Agora que este componente está fazendo uma chamada para exibir um único evento, podemos adicioná-lo às nossas rotas.


### **Passo 2. Adicionando ``EventDetailsView`` como uma rota**

2.1 Abra o arquivo "**src/router/index.js**" e altere o seu conteúdo de acordo com o que está abaixo.

```javascript
...
import EventDetailsView from '../views/EventDetailsView.vue'
import AboutView from '../views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...
    {
      path: '/event/123',
      name: 'event-details',
      component: EventDetailsView,
    },
    ...
  ],
})
```

> Por enquanto, apenas codificaremos o caminho: "**/event/123**". Eventualmente, a parte final (``123``) será dinâmica e atualizada com o ``id`` do evento que está sendo exibido no momento.
> 

> Agora que temos essa nova rota, precisamos acessá-la. Novamente, queremos acessar esta rota sempre que clicarmos em um dos ``EventCards`` em nossa página inicial (i.e. "**homepage**").


### **Passo 3. Tornando o ``EventCard`` clicável com um ``RouterLink``**

3.1 Indo para o componente ``EventCard``, vamos agrupar nosso código do _template_ em um ``RouterLink``. Portanto, abra o arquivo "**src/components/EventCard.vue**" e altere o seu conteúdo para o código abaixo.


```javascript
<template>
  <RouterLink to="event/123">
    <div class="event-card">
      <h2>{{ event.title }}</h2>
      <span>@{{ event.time }} on {{ event.date }}</span>
    </div>
  </RouterLink>
</template>

```

Agora, quando um de nossos ``EventCards`` for clicado, seremos encaminhados para o novo caminho ``event/123``.

Se verificarmos isso no browser, veremos um erro no console ao clicarmos em um evento (ver figura abaixo).

![error_click_event](img_readme/error_click_event.jpg)


> O que está acontecendo aqui é que ``EventDetailsView`` está tentando exibir os detalhes do evento antes de receber o evento de volta da chamada da API. Precisamos dizer ao nosso componente para esperar até que tenha o evento antes de tentar exibir seus detalhes. Felizmente, essa é uma solução muito simples.

3.2 Abra o arquivo "**src/views/EventDetailsView.vue**" e altere o seu conteúdo com o que está abaixo.

```javascript
<template>
  <div v-if="event">
    <h1>{{ event.title }}</h1>
    <p>{{ event.time }} on {{ event.date }} @ {{ event.location }}</p>
    <p>{{ event.description }}</p>
  </div>
</template>
```

> Ao adicionar um simples ``v-if="event"`` em nosso elemento ``<div>`` aqui, podemos garantir que ele seja renderizado apenas quando o evento existir em nossos dados.


3.3 Se verificarmos novamente no navegador, veremos que está funcionando até agora… Quando clicamos no evento "_Cat Adoption Day_" ``EventCard``, somos levados a uma visualização que exibe os detalhes desse evento. Veja a figura abaixo.

![cat_adoption_day_event](img_readme/cat_adoption_day_event.jpg)

> No entanto, se clicarmos em qualquer outro ``EventCard``, ainda estamos obtendo os mesmos detalhes do "_Cat Adoption Day_", e o ``id`` no final de nosso URL é o mesmo: **123**. Isso é esperado, já que codificamos o ``id`` que estamos passando para a chamada ``getEvent`` e no caminho da rota ``EventDetails`.

Isso nos leva ao final da **Parte 1** e ao início da **Parte 2**, onde tornamos esse comportamento de roteamento dinâmico para que possamos rotear os detalhes de qualquer ``EventCard`` em que clicarmos.


##Parte 2

Para tornar nosso comportamento de roteamento dinâmico, precisamos trocar o ``id`` codificado em nosso caminho (**/123**) e substituí-lo por um segmento dinâmico. Este é basicamente um parâmetro variável para o caminho do URL, que é atualizado com o ``id`` de qualquer evento exibido atualmente nessa rota. A figura abaixo mostra o que pretendemos fazer.

![dynamic_segment](img_readme/dynamic_segment.jpg)

> Em seguida, desejaremos prover esse segmento dinâmico no componente ``EventDetailsView`` como uma ``prop`` a ser usada ao fazer a chamada ``getEvent``.



### **Passo 4. Adicionando um segmento dinâmico à rota ``EventDetailsView``**

Vamos começar e adicionar um segmento dinâmico ao caminho da rota ``EventDetailsView`.

4.1 Abra o arquivo "**src/router/index.js**" e altere o seu conteúdo conforme abaixo.

```javascript
{
  path: '/event/:id',
  name: 'event-details',
  props: true,
  component: EventDetailsView,
},
```

> Observe como a sintaxe de um segmento dinâmico começa com dois pontos ``:`` e é seguida pelo que você quiser chamar o segmento. Nesse caso, é ``:id``, pois é substituído pelo ``id`` do nosso evento. Em outro caso de uso, pode ser algo como ``:username`` ou ``:orderNumber``.

> Também adicionamos ``props: true`` aqui para dar ao componente ``EventDetailsView`` acesso a este parâmetro de segmento dinâmico como uma ``prop``.

> Como atualizamos o caminho nesta rota, o caminho no atributo ``to`` do nosso atributo ``EventCard`` agora precisa ser atualizado. Lembre-se, atualmente está codificado como ``to="event/123"``.


4.2 Agora abra o arquivo "**src/components/EventCard.vue**" e observe a linha que contém o ``RouterLink``. Altere-a para:

```javascript
<RouterLink :to="{ name: 'event-details' }">
```

> Agora, também tornamos nosso aplicativo um pouco mais escalável. Em um aplicativo maior com vários ``RouterLinks``, torna-se desnecessariamente árduo manter os caminhos em cada ``RouterLink`` sempre que eles precisam mudar. Por outro lado, se os seus usaram rotas nomeadas e o caminho da sua rota precisar ser alterado, você pode simplesmente alterá-lo uma vez no arquivo do roteador e nenhum de seus ``RouterLinks`` precisa ser atualizado, pois não depende do próprio caminho .

### **Passo 5. Adicionando o ID do evento aos parâmetros do roteador**

Neste ponto, você deve estar se perguntando como dizemos ao nosso segmento dinâmico ``:id`` por qual valor ele precisa ser substituído. Podemos fazer isso adicionando a propriedade ``params`` ao nosso objeto no atributo ``to:``.

5.1 Abra o arquivo "**src/components/EventCard.vue**" e altere o seu conteúdo para o abaixo.

```javascript
<script setup>
defineProps({
  event: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <RouterLink :to="{ name: 'event-details', params: { id: event.id } }">
    <div class="event-card">
      <h2>{{ event.title }}</h2>
      <span>@{{ event.time }} on {{ event.date }}</span>
    </div>
  </RouterLink>
</template>
```

> Lembre-se de alguns tutoriais atrás, este componente tem o evento como uma ``prop``, e então podemos pegar ``event.id`` dele e definir o parâmetro ``id``  igual a ele. Veja a linha acima que contém o código abaixo.

```javascript
<RouterLink :to="{ name: 'event-details', params: { id: event.id } }">
```

Agora, quando clicamos neste ``RouterLink``, somos roteados para ``EventDetailsView`` e o caminho da rota é anexado com o ``id`` do evento.


5.2 Agora podemos finalmente alimentar esse parâmetro ``id`` no componente ``EventDetailsView`` como uma ``prop``. Abra o arquivo "src/views/EventDetailsView.vue" e altere o seu conteúdo como o abaixo.

```javascript
<script setup>
import { ref, onMounted } from 'vue'
import EventService from '@/services/EventService.js'

const props = defineProps({
  id: {
    required: true,
  },
})

const event = ref(null)

onMounted(() => {
  EventService.getEvent(props.id)
    .then((response) => {
      event.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>
```

> Agora, quando dizemos ``getEvent(this.id)``, estamos nos referindo à ``prop id`` recém-adicionada. Quando ``EventDetailsView`` é roteado e assim montado, ele agora faz uma solicitação para o evento com o ``id`` que se encontra no parâmetro dinâmico do caminho da rota.


5.3 Se verificarmos isso no browser, poderemos clicar com sucesso em um ``EventCard`` e exibir os detalhes apropriados para esse evento. Veja a figura abaixo.

![click_event_succesful](img_readme/click_event_succesful.jpg)

### **Passo 6. Limpando nosso Código**

Com isso, finalizamos nosso comportamento de roteamento dinâmico. Ufa! Foram muitos passos. Agora, eu só precisamos limpar algumas coisas antes de terminarmos.

Primeiro, nossos ``EventCards`` não parecem tão bonitos agora que estão envolvidos com um``RouterLink`` (ver figura abaixo).

![event_card_no_nice](img_readme/event_card_no_nice.jpg)


Vamos adicionar uma classe chamada ``event-link`` ao ``<RouterLink>`` para torná-lo mais bonito.

6.1 Abra o arquivo "**src/components/EventCard.vue**" e altere o seu conteúdo por este abaixo.

```javascript
<template>
  <RouterLink
    class="event-link"
    :to="{ name: 'event-details', params: { id: event.id } }"
  >
    <div class="event-card">
      <h2>{{ event.title }}</h2>
      <span>@{{ event.time }} on {{ event.date }}</span>
    </div>
  </RouterLink>
</template>

<style scoped>
...
.event-link {
  color: #2c3e50;
  text-decoration: none;
}
</style>
```
A figura abaixo mostra que a visualização de evento ficou mais agradável.

![event_card_nice](img_readme/event_card_nice.jpg)

Por uma questão de consistência, também podemos atualizar o arquivo ``App.vue`` para usar rotas nomeadas em vez de caminhos codificados.

6.2 Abra o arquivo "**src/App.vue**" e altere o trecho de código para:

```javascript
<div class="wrapper">
  <nav>
    <RouterLink :to="{ name: 'event-list' }">Events</RouterLink> |
    <RouterLink :to="{ name: 'about' }">About</RouterLink>
  </nav>
</div>
```

> Isso ajuda a criar escalabilidade para a manutenção das rotas de nosso aplicativo.



### **Passo 7. Fazendo o Fechamento**

No próximo tutorial, aprenderemos como pegar nosso aplicativo e implantá-lo na produção (i.e. fazer o _deploy_), usando o **Render**.