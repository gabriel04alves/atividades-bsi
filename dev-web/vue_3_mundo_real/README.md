# **2. Real World Vue.JS3 (API de Composição)**

## **Este repositório possui um curso sobre a construção de uma _app_ Vue.JS 3**

Neste curso, criaremos um aplicativo de nível de produção usando Vue.JS versão 3. Começaremos criando o projeto usando o comando ``create-vue``. Em seguida, aprenderemos sobre componentes ``.vue`` e como eles podem ser usados para criar um aplicativo de página única (**Single Page Application**). Depois abordaremos os fundamentos do "**Vue Router**" para que possamos navegar entre as diferentes visualizações de nosso aplicativo e até mesmo buscar dados externos reais usando chamadas de API com o "**Axios**". Terminaremos aprendendo sobre o processo de construção e como implantar nosso aplicativo em produção.

## **IDE recomendado**

Vai-se utilizar o VSCode. Caso você ainda não o tenha [baixe-o](https://code.visualstudio.com/download), e depois instale-o.

Instale, também uma extensão do VSCode chamada [es6-string.html](https://marketplace.visualstudio.com/items?itemName=Tobermory.es6-string-html)


## **Tutorial 4. Vue Router Essentials (Fundamentos do Vue Router)**

Neste tutorial, veremos as ferramentas que o Vue usa para navegar entre as páginas (ou visualizações) em nosso aplicativo. Serão abordados:

* O que é roteamento do lado do cliente?
* O que é um aplicativo de página única (_Single Page Application - SPA_)?
* Como o **Vue Router** é configurado em um aplicativo Vue?
* E por fim, personalizaremos os roteadores em nosso aplicativo de exemplo


### **Passo 1. Server-Side vs Client-Side Routing (Roteamento do lado do servidor vs do lado do cliente)**

Quando se trata de websites, normalmente conectamos nossa página com links. Um link é clicado, chama de volta o servidor para a próxima página e essa página é carregada. Ver figura abaixo.

![server_side_routing](img_readme/server_side_routing.jpg)

Chamamos isso de “_roteamento do lado do servidor_” porque o cliente está fazendo uma solicitação ao servidor a cada alteração de um URL.

![sever_side_routing_2](img_readme/sever_side_routing_2.jpg)

> Quando se trata do Vue, muitos escolhem o roteamento do lado do cliente, o que significa que ele ocorre no próprio navegador (browser) usando JavaScript.

![client_side_routing](img_readme/client_side_routing.jpg)

> Em muitos casos, a visualização do nosso aplicativo que precisamos mostrar já foi carregada no navegador, portanto, não precisamos entrar em contato com o servidor para obtê-la. O **Vue Router** simplesmente atualiza a parte do aplicativo que está sendo exibida no momento.

> Na verdade, com um tipo de roteamento como esse, nosso aplicativo funciona como um aplicativo de página única (i.e. SPA). Ver figura abaix. Mas, o que exatamente isso significa? É o que veremos no próximo passo.

![spa_index_html](img_readme/spa_index_html.gif)


### **Passo 2. Aplicativo de Página Única (Single Page Application)**

Um SPA é um _web app_ que carrega de uma única página e a atualiza dinamicamente conforme o usuário interage com o aplicativo. No nosso caso, tudo está sendo carregado do arquivo "**index.html**" do nosso projeto. No **Tutorial 2**, examinamos esse arquivo e vimos que ele continha uma ``<div>`` com o ``id`` denominado ``#app``. Veja abaixo.


```
<div id="app"></div>
```

Também demos uma olhada no arquivo "**main.js**" e descobrimos que, quando nosso aplicativo é criado, ele é montado nessa ``<div>`` com o ``id #app``. Veja abaixo.

```
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
```

Em outras palavras, o arquivo "**index.html**" é a “_página única_” do nosso SPA, onde todo o código do aplicativo é montado. O **Vue Router** permite o roteamento do lado do cliente para que possamos navegar e exibir diferentes “visões” (i.e. ``views``) do nosso _app_.


### **Passo 3. O Arquivo "package.json"**

Todas as dependências do nosso aplicativo são rastreadas dentro do nosso arquivo ``package.json``. Se dermos uma olhada rápida dentro dele, veremos que o Vue CLI já inseriu o **Vue Router** como uma dependência porque optamos por adicioná-lo quando configuramos nosso projeto. Veja parte do conteúdo deste arquivo.

```
...
"dependencies": {
  "axios": "^1.2.1",
  "pinia": "^2.0.21",
  "vue": "^3.2.38",
  "vue-router": "^4.1.5"
},
...
```

> O conteúdo acima está dizendo ao nosso aplicativo para usar uma versão do ``vue-router`` compatível com a versão **4.0.0-0**. (Talvez o número da sua versão pode ser diferente dependendo de quando você fizer este tutorial).

Anteriormente no **Tutorial 2**, executamos o comando ``npm install``, que instalou a biblioteca ``vue-router`` dentro do diretório ``node_modules`` de nosso aplicativo.

Agora vamos dar uma olhada dentro do diretório ``router`` para ver como o **Vue Router** está funcionando.


### **Passo 4. Como o *Vue Router* É Configurado**

4.1 Abra o arquivo "**src/router/index.js**" e observe as duas primeiras linhas de código.

```javascript
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
```

> Na primeira linha estamos importando a biblioteca "**vue-router**".
> 
> Na segunda, importamos um componente que usaremos em nossas rotas

Observe também, neste mesmo arquivo o código abaixo.

```javascript
routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // pulamos esta parte, que será vista posteriormente
 	   ...
    }
  ]
```

``path`` indica a rota atual, em termos de URL, para onde o usuário será levado. Nela, existe apenas a ``/`` (barra), ou seja, esta é a raiz, a página inicial (``homepage``) do nosso aplicativo e o que as pessoas veem quando acessam nosso domínio em ``example.com``, por exemplo.

``name`` nos permite dar um nome a essa rota para que possamos usá-la em todo nosso _app_ para nos referirmos a ela (veremos sobre isso mais adiante).

``component`` nos permite especificar qual componente renderizar naquela rota. Observe que o ``HomeView`` foi importado na segunda linha do arquivo. Assim, este componente (``HomeView``) será renderizado sempre que o URL do navegador terminar com uma ``/`` (barra) sem nada depois dela.

Observando o segundo objeto de rota, podemos ver que ele tem um caminho diferente.

```javascript
{
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
```

Quando o URL do navegador terminar com ``/about``, o componente ``About` será renderizado.

Você provavelmente notou que também está importando o componente de maneira diferente. Em vez de importá-lo na parte superior do arquivo (duas primeiras linhas), como fizemos com ``HomeView``, estamos importando-o apenas quando a rota é realmente chamada. Como diz nos comentários, isso irá gerar um arquivo "**About.js**" separado, que só será carregado no navegador de alguém quando este alguém navegar para ``/about``. Esta é uma otimização de desempenho que não é necessária em nosso aplicativo pequeno e simples. Mas, à medida que um aplicativo cresce, pode ser útil dividir como ele é carregado em diferentes arquivos JavaScript, que só são carregados quando são necessários.

Usamos o método ``createRouter()`` para criar o roteador, informando-o para usar a API de histórico do browser e enviando as rotas, antes de finalmente exportá-lo desse arquivo.

```javascript
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...
  ]
})

export default router
```

> Portanto, definimos as duas visualizações diferentes entre as quais nosso aplicativo poderá navegar, mas na verdade ainda não carregamos esse roteador em nossa instância do Vue. Lembre-se, todo o nosso aplicativo é carregado de nosso arquivo "**main.js**" e, se olharmos dentro desse arquivo, podemos ver que estamos importando nosso arquivo em ``./router/index.js``, que está trazendo o que exportamos de "**router.js**". Veja o trecho de código do arquivo "**main.js**".


```javascript
import router from './router'  
```

> A linha acima indica queremos importar "**index.js**" do diretório ``/router``.


Você também notará neste arquivo que dizemos à nossa instância Vue para usar o roteador que importamos. Veja a linha abaixo.

```javascript
app.use(router)
```

**Até agora tudo bem. Nosso roteador está configurado. Mas onde é adicionada a funcionalidade para permitir que o usuário navegue para diferentes partes do aplicativo? É o que veremos no próximo passo.**  


### **Passo 4. Componentes embutidos do Vue Router**

Procurando dentro do arquivo "**App.vue**", encontraremos um elemento ``<nav>``. Dentro dele existem alguns links de roteadores (``RouterLink``), que são componentes globais específicos do "**Vue Router**" aos quais temos acesso.


4.1 Abra o arquivo "**src/App.vue**" e observe o conteúdo abaixo:

```
<header>
  <div class="wrapper">
    <nav>
      <RouterLink to="/">Home</RouterLink> |
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </div>
</header>
```


4.2 E um pouco mais abaixo deles está este outro componente do "**Vue Router**":

```
<RouterView />
```

**Surge a pergunta: o que está acontecendo aqui?**

``<RouterLink>`` é um componente (da biblioteca ``vue-router``) cujo trabalho é vincular a uma rota específica. Você pode pensar nele como uma "etiqueta de âncora embelezada" (_anchor tag_).

``<RouterView/>`` é essencialmente um espaço reservado (i.e. _placeholder_) onde o conteúdo do nosso componente ``view` será renderizado na página.

Quando um usuário clica no link ``Home``, para onde ele será direcionado? Essa resposta está dentro do atributo ``to``: ``<RouterLink to="/">``.

Ou seja, ele será levados para ``/``, o que significa que de acordo com a rota configurada em "**router.js**", o componente ``Home`` será carregado.


 4.3 Agora abra o arquivo "src/router/index.js" e observe o trecho de código.

```javascript
{
  path: '/',
  name: 'home',
  component: HomeView
},
```

Mas onde, exatamente, ele será carregado? A resposta é: no ``<RouterView/>``.

Novamente, isso é apenas um _placeholder_ que é substituído pelo componente ``view`` para o qual roteamos, como ``HomeView`` ou ``AboutView``. A figura abaixo ilustra este processo.

![placeholder_component](img_readme/placeholder_component.jpg)


### **Passo 5. Customizando (Personalizando) nosso aplicativo de exemplo**

Agora que entendemos os fundamentos do "**Vue Router**", estamos prontos para começar a personalizar as rotas em nosso aplicativo de exemplo. Nossa lista de tarefas inclui:

1. Renomear ``HomeView.vue`` para ``EventListView.vue``
2. Personalizar a rota para ``EventListView``
3. Atualizar ``AboutView.vue``
4. Reconfigurar a rota ``About``




5.1 Renomeie o arquivo "**src/views/HomeView.vue**" para "**src/views/EventListView.vue**".

5.2 Agora que o arquivo foi renomeado, precisaremos alterar nossa declaração de importação (comando ``import``) em nosso arquivo  roteador e corrigir o próprio objeto de rota (i.e. o nome do componente). Abra o arquivo "**src/route/index.js**" e altere a segunda e a décima linha de código conforme o trecho abaixo.

```
import { createRouter, createWebHistory } from 'vue-router'
import EventListView from '../views/EventListView.vue' 
const routes = [
  {
    path: '/',
    name: 'event-list',
    component: EventListView
  },
  ...
]
```

5.3 Agora vamos adicionar alguma personalização à nossa página ``About`` para ajustar nosso aplicativo de exemplo, adicionando uma descrição de texto. Para isto, abra o arquivo "**src/views/About.vue**" e altere o seu conteúdo conforme o trecho de código abaixo.

```
<template>
  <div class="about">
    <h1>A site for events to better the world.</h1>
  </div>
</template>
```

5.4 Como não precisamos usar a divisão de código em nível de rota para nosso aplicativo, vamos simplificar o objeto de rota ``About``. Abra o arquivo "**src/router/index.js**" e substitua seu conteúdo de acordo com o trecho de código abaixo.

```javascript
{
  path: '/about',
  name: 'about',
  component: AboutView
}
```

> Não podemos nos esquecer de importar o arquivo "**About.vue**".

5.5 Para nos certificarmos de que todas as alterações no arquivo "**src/router/index.js**" foram efetuadas, o seu conteúdo deve estar como o código abaixo.

```javascript
import { createRouter, createWebHistory } from 'vue-router'
import EventListView from '../views/EventListView.vue'
import AboutView from '../views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'event-list',
      component: EventListView,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
  ],
})

export default router
```

5.6 Como agora estamos exibindo uma lista de eventos no que costumava ser nossa página “**Home page**”, vamos atualizar o HTML interno do ``RouterLink`` para essa visualização. Abra o arquivo "src/App.vue" e atualize seu conteúdo para:

```javascript
<template>
  <div id="layout">
    <header>
      <div class="wrapper">
        <nav>
          <RouterLink to="/">Events</RouterLink> |
          <RouterLink to="/about">About</RouterLink>
        </nav>
      </div>
    </header>
    <RouterView />
  </div>
</template>
```


5.7 Repita o procedimento efetuado no **Passo 3.10** do **Tutorial 3** para visualizarmos no browser o que acabamos de fazer no passo anterior. Você verá algo como a figura abaixo.


![example_app_t4](img_readme/example_app_t4.jpg)


### **Passo 7. Fazendo o Fechamento**

Neste tutorial aprendemos os conceitos básicos do **Vue Router**. No próximo tutorial, aprenderemos como buscar nossos eventos como dados externos que extraímos por meio de uma chamada de API usando o Axios.