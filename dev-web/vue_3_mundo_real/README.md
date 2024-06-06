# **2. Real World Vue.JS3 (API de Composição)**

## **Este repositório possui um curso sobre a construção de uma _app_ Vue.JS 3**

Neste curso, criaremos um aplicativo de nível de produção usando Vue.JS versão 3. Começaremos criando o projeto usando o comando ``create-vue``. Em seguida, aprenderemos sobre componentes ``.vue`` e como eles podem ser usados para criar um aplicativo de página única (**Single Page Application**). Depois abordaremos os fundamentos do "**Vue Router**" para que possamos navegar entre as diferentes visualizações de nosso aplicativo e até mesmo buscar dados externos reais usando chamadas de API com o "**Axios**". Terminaremos aprendendo sobre o processo de construção e como implantar nosso aplicativo em produção.

## **IDE recomendado**

Vai-se utilizar o VSCode. Caso você ainda não o tenha [baixe-o](https://code.visualstudio.com/download), e depois instale-o.

Instale, também uma extensão do VSCode chamada [es6-string.html](https://marketplace.visualstudio.com/items?itemName=Tobermory.es6-string-html)


## **Tutorial 3. Single File Components (Componentes de Arquivo Único)**

No tutorial anterior criamos nosso projeto com o comando ``create-vue``, e agora estamos prontos para começar a customizá-lo para construir nosso próprio aplicativo.

### **Passo 1. O Que São Esses Arquivos ``.vue``?**

Para começar a construir nosso _app_, precisamos obter uma compreensão básica de como as coisas estão funcionando no aplicativo de demonstração que a CLI criou para nós no tutorial anterior. Vamos analisar o diretório ``src/views``, que possui dois arquivos com a extensão ``.vue``: **HomeView.vue** e **AboutView.vue**. Na verdade, eles são os componentes que o "**Vue Router**" (Roteador Vue) carrega quando navegamos para as rotas ``Home`` e ``About``, respectivamente. A figura abaixo ilustra o que acabamos de dizer.

![links_home_about](img_readme/links_home_about.jpg)

No próximo tutorial, vamos explorar os fundamentos do **Vue Router**, mas por enquanto você só precisa entender que esses componentes de “_visualização_” são diferentes e que podem ser vistos (ou navegados) em nosso aplicativo. Eles podem conter componentes filhos que estão aninhados dentro deles, e seus filhos também serão exibidos. Por exemplo, o componente ``HomeView.vue`` tem um filho: ``TheWelcome.vue``, que tem vários códigos de _template_ que estão sendo exibidos quando estamos na rota ``Home``. O trecho de código do arquivo ``HomeView.vue`` abaixo mostra como o componente pai "chama" o componente filho.

```javascript
<script setup>
   import TheWelcome from '../components/TheWelcome.vue'
</script>
```

Cada um desses arquivos ``.vue`` são componentes de arquivo único, e é isso que estamos explorando: do que são compostos e como você os usa para criar um aplicativo Vue?

### **Passo 2. Anatomia de Um Componente de Arquivo Único (Single File Component)**

Quando falamos de aplicativos Vue, na verdade estamos falando de uma coleção de componentes Vue. A figura abaixo mostra esta coleção.

![anatomia_componente](img_readme/anatomia_componente.gif)

Surge uma pergunta: como funcionam esses componentes de arquivo único? Observe a figura abaixo.

![anatomia_componente_2](img_readme/anatomia_componente_2.jpg)

Um componente ``.vue`` típico possui três seções: ``<script>``, ``<template>`` e ``<style>``.

Usando a analogia de um corpo humano, você pode pensar no ``<template>`` como o esqueleto de seu componente, uma vez que ele dá a estrutura. A seção de ``<script>`` é o cérebro, fornecendo a inteligência e o comportamento. E a seção ``<style>`` é exatamente o que parece: roupas, maquiagem, penteado, enfim, a perfumaria.

Tradicionalmente, essas seções são escritas em HTML, JavaScript e CSS. No entanto, com a configuração adequada, você também pode usar alternativas como Pug, TypeScript e SCSS.

Agora que pudemos entender os componentes de arquivo único, podemos começar a criar os nossos. Mas primeiro, o que vamos construir, exatamente? O próximo passo descreverá isto.


### **Passo 3. O _app_ Que Vamos Construir**

No final deste curso, teremos feito um _app_ que mostra eventos. Veja a figura abaixo.

![display_events_app](img_readme/display_events_app.jpg)

Os eventos serão extraídos de uma chamada a uma API externa e serão exibidos na página inicial. Poderemos clicar no evento para ver os seus detalhes, como mostra a figura abaixo.

![display_events_app_2](img_readme/display_events_app_2.jpg)

3.1 Abra o Terminal no VS Code. Primeiro digite (CTRL+Shift+P) e use a opção “Ver: Toggle Terminal” ou “Ver: Alternar Terminal”.

3.2 Caso ainda não esteja no diretório, digite na linha de comando do Terminal: 

```
cd vue_3_mundo_real
```

3.3 Renomeie o arquivo "**src/components/HelloWorld.vue**" para "**src/components/EventCard.vue**".

3.4 Agora abra o arquivo "**src/components/EventCard.vue**" e altere o seu conteúdo para o trecho de código abaixo.

```html
<script setup>
// defineProps({
//   msg: {
//     type: String,
//     required: true,
//   },
// })
</script>

<template>
  <div class="greetings"></div>
</template>

<style scoped></style>
```

3.5 Abra o arquivo "**src/App.vue**" e altere o seu conteúdo para o trecho de código abaixo.

```
<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div id="layout">
    <header>
      <div class="wrapper">
        <nav>
          <RouterLink to="/">Home</RouterLink> |
          <RouterLink to="/about">About</RouterLink>
        </nav>
      </div>
    </header>
    <RouterView />
  </div>
</template>

<style>
#layout {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
nav {
  padding: 30px;
}
nav a {
  font-weight: bold;
  color: #2c3e50;
}
nav a.router-link-exact-active {
  color: #42b983;
}
</style>
```

3.6 Abra o arquivo "**src/main.js**" e altere o conteúdo abaixo

```javascript
import './assets/main.css'
```

Para este conteúdo (apenas aplique um comentário na linha):

```javascript
// import './assets/main.css'
```

O que fizemos foi "remover" o arquivo CSS porque nós implementamos o estilo no passo 3.5.

3.7 Remova a pasta "**src/components/icons**"

3.8 Remova os arquivos "**src/components/TheWelcome.vue**" e "**src/components/WelcomeItem.vue**".

3.9 Abra o arquivo "**src/views/HomeView.vue**" e altere o seu conteúdo para:

```javascript
<script setup></script>

<template>
  <div class="home"></div>
</template>
```

3.10 Digite na linha de comando:

```
npm run dev
```

Após a execução do comando acima, ele disponibiliza ao vivo um host local (``http://localhost:5173``), você verá a seguinte página no browser:

![vue_initial_app_updated](img_readme/vue_initial_app_updated.jpg)


### **Passo 4. Trabalhando no ``EventCard``**

4.1 Abra o arquivo "**src/components/EventCard.vue**" e altere o conteúdo abaixo:

```
<template>
  <div class="greetings"></div>
</template>
```

Para:

```
<template>
  <div class="event-card"></div>
</template>
```

4.2 Agora vamos adicionar alguns estilos para classe ``event-card``. Substitua o trecho de código abaixo

```
<style scoped></style>
```

Para:

```
<style scoped>
.event-card {
  padding: 20px;
  width: 250px;
  cursor: pointer;
  border: 1px solid #39495c;
  margin-bottom: 18px;
}
.event-card:hover {
  transform: scale(1.01);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2);
}
</style>
```

> Você deve estar se perguntando o que esse atributo ``scoped`` significa? A resposta é: ele nos permite definir e isolar estilos apenas para esse componente. Ou seja, eles são específico e não afetarão nenhuma outra parte de nossa aplicação.

4.3 Como queremos exibir informações sobre o evento neste "**EventCard**", precisamos fornecer a ele um evento para exibição. Vamos, então, adicionar isso usando uma referência em nossa seção ``<script>``. Para isto, abra o arquivo "**src/components/EventCard.vue**" e altere o conteúdo da secão ``<script>`` com o trecho de código abaixo.

```javascript
<script setup>
import { ref } from 'vue'

// defineProps({
//   msg: {
//     type: String,
//     required: true,
//   },
// })

const event = ref({
  id: 5928101,
  category: 'animal welfare',
  title: 'Cat Adoption Day',
  description: 'Find your new feline friend at this event.',
  location: 'Meow Town',
  date: 'January 28, 2022',
  time: '12:00',
  petsAllowed: true,
  organizer: 'Kat Laydee',
})
</script>
```

4.4 Agora, na seção ``<template>`` podemos exibir alguns desses dados de evento usando o código abaixo. No mesmo arquivo do passo anterior (**passo 4.3**), altere a seção ``<template>``:

```javascript
<template>
  <div class="event-card">
    <h2>{{ event.title }}</h2>
    <span>@{{ event.time }} on {{ event.date }}</span>
  </div>
</template>
```

4.5 Para que o evento "**EventCard**" seja exibido, ele precisa ser colocado em algum lugar para o qual ele possa ser roteado, como o arquivo "**HomeView.vue**" em nosso diretório ``views``. Precisamos importar ``EventCard.vue``, e então podemos usá-lo no ``<template>``. Para isto, abra o arquivo "**src/views/HomeView.vue**" e altere o seu conteúdo para:

```javascript
<script setup>
import EventCard from '@/components/EventCard.vue'
</script>

<template>
  <div class="home">
    <EventCard />
  </div>
</template>
```

4.6 Agora, devemos ver nosso "**EventCard**" aparecendo no browser quando estamos na página inicial (``Home``). Ver figura abaixo.

![event_card_showing_up](img_readme/event_card_showing_up.jpg)


### **Passo 5. Fazendo Um Refatoramento No Código**

Estamos fazendo um grande progresso, mas lembre-se de que queremos que o ``EventCard`` seja exibido no meio da página inicial ("**Home Page**"). E, como eventualmente teremos uma coleção de eventos que extraímos de uma chamada à uma API, precisamos refatorar um pouco para tornar esse caso de uso mais pronto para produção.

As etapas de refatoração incluem:

* Mover os dados dos eventos para o evento pai (i.e. "**HomeView.vue**")
* O evento pai cria o componente ``EventCard`` para cada evento em seus dados
* O evento pai alimenta cada ``EventCard`` com seu próprio evento para exibir
* O evento pai exibe os ``EventCards`` em um contêiner Flexbox.


5.1 Nosso primeiro passo será excluir os dados do evento em ``EventCard``. Em seguida, adicionaremos uma ``prop``para este evento, para que o componente pai possa alimentar o componente filho com um objeto de evento para exibição. Para isto, abra o arquivo "**src/components/EventCard.vue**" e substitua o seu conteúdo pelo abaixo.

```
<script setup>
import { ref } from 'vue'

defineProps({
  event: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <div class="event-card">
    <h2>{{ event.title }}</h2>
    <span>@{{ event.time }} on {{ event.date }}</span>
  </div>
</template>

<style scoped>
.event-card {
  padding: 20px;
  width: 250px;
  cursor: pointer;
  border: 1px solid #39495c;
  margin-bottom: 18px;
}
.event-card:hover {
  transform: scale(1.01);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2);
}
</style>
```
5.2 Agora que o ``EventCard`` está configurado para receber um evento, podemos adicionar os dados dele no seu componente pai, que é ``HomeView.vue``. Abra o arquivo "**src/views/HomeView.vue"**, e substitua conteúdo dele pelo que está abaixo:

```
<script setup>
import EventCard from '@/components/EventCard.vue'
import { ref } from 'vue'

const events = ref([
  {
    id: 5928101,
    category: 'animal welfare',
    title: 'Cat Adoption Day',
    description: 'Find your new feline friend at this event.',
    location: 'Meow Town',
    date: 'January 28, 2022',
    time: '12:00',
    petsAllowed: true,
    organizer: 'Kat Laydee',
  },
  {
    id: 4582797,
    category: 'food',
    title: 'Community Gardening',
    description: 'Join us as we tend to the community edible plants.',
    location: 'Flora City',
    date: 'March 14, 2022',
    time: '10:00',
    petsAllowed: true,
    organizer: 'Fern Pollin',
  },
  {
    id: 8419988,
    category: 'sustainability',
    title: 'Beach Cleanup',
    description: 'Help pick up trash along the shore.',
    location: 'Playa Del Carmen',
    date: 'July 22, 2022',
    time: '11:00',
    petsAllowed: false,
    organizer: 'Carey Wales',
  },
])
</script>

<template>
  <div class="home">
    <EventCard />
  </div>
</template>
```

5.3 Agora que ``HomeView.vue`` tem os dados dos eventos, podemos usá-los para criar um novo ``EventCard`` para cada um dos objetos de evento que estão nesses dados, usando a diretiva ``v-for``. Para isto, abra o arquivo "src/views/HomeView.vue" e altere o conteúdo que trata da seção ``<template>``para o código abaixo.

```
<template>
  <div class="home">
    <EventCard v-for="event in events" :key="event.id" :event="event" />
  </div>
</template>
```

> Observe como estamos vinculando o ``id`` do evento ao atributo ``:key``. Isso dá ao "**Vue.JS**" uma maneira de identificar e acompanhar cada ``EventCard`` exclusivo.

5.4 Repita o procedimento efetuado no **Passo 3.10** para visualizarmos no browser o que acabamos de fazer no passo anterior. Ou seja, criamos um ``EventCard``para cada um dos eventos que são dados do arquivo "**HomeView.vue**". Você verá algo como a figura abaixo.

![all_events_homeview](img_readme/all_events_homeview.jpg)

5.5 Por fim, só precisamos colocar esses eventos em um contêiner Flexbox para que as coisas fiquem como queremos. Abra o arquivo "**src/views/HomeView.vue**" e altere o nome da classe do elemento ``<div>`` em que nosso ``EventCard`` está aninhado e adicionar alguns estilos Flexbox. Altere o conteúdo das seções ``<template>``e ``<style scoped>`` pelo seguinte trecho abaixo.

```
...

<template>
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

5.6 Repita o procedimento efetuado no **Passo 3.10** para visualizarmos no browser o que acabamos de fazer no passo anterior. Você verá algo como a figura abaixo.

####INSERIR FIGURA

> Agora nossos ``EventCards`` serão exibidos em uma coluna centralizada.


### **Passo 6. E os Estilos Globais?**

6.1 Até agora, discutimos estilos com escopo e como o atributo ``scoped`` nos permite adicionar estilos direcionados ao componente específico com o qual estamos preocupados. Mas e os estilos globais que queremos aplicar a todo o nosso aplicativo? Embora existam diferentes maneiras de fazer isso, a mais simples é abrindo o arquivo "**src/App.vue**". Lembre-se: este é o componente raiz do nosso aplicativo. Agora remova o atributo ``scoped`` da seção ``<style>``. Ela ficará então assim:

```
<style>
...
</style>
```

6.2 Agora todos os estilos no ``App.vue`` são aplicados a todo o aplicativo. Aqui, poderíamos adicionar uma nova regra (um novo elemento ``<h2>``). Abra novamente o arquivo ``**src/App.vue**" e adicione a regra do CSS.

```
<style>
...
h2 {
  font-size: 20px;
}
</style>
```

6.3 Agora, qualquer elemento ``<h2>`` em nosso aplicativo terá um tamanho de fonte de 20px. Como o template do nosso ``EventCard`` possui um ``<h2>``, ele receberá esse novo estilo global. Abra o arquivo "src/components/EventCard.vue" e altere o conteúdo da seção ``<template>``para o trecho de código abaixo.

```
<template>
  <div class="event-card">
    <h2>{{ event.title }}</h2>
    <span>@{{ event.time }} on {{ event.date }}</span>
  </div>
</template>
```

6.4 Falando em itens globais em nosso _app_ Vue, o que aconteceria se adicionássemos algo como um elemento ``<h1>`` à seção ``<template>`` do arquivo ``src/App.vue``? Abra-o e altere a seção com o conteúdo abaixo.

```
<template>
  <div id="layout">
    <header>
      <div class="wrapper">
        <nav>
          <RouterLink to="/">Home</RouterLink> |
          <RouterLink to="/about">About</RouterLink>
        </nav>
      </div>
    </header>
    <h1>Events For Good</h1> <!-- new element -->
    <RouterView />
  </div>
</template>
``` 

6.5 Repita o procedimento efetuado no **Passo 3.10** para visualizarmos no browser o que acabamos de fazer no passo anterior. Você verá algo como a figura abaixo.

![all_events_homeview_2](img_readme/all_events_homeview_2.jpg)

> Estamos vendo algumas coisas. Primeiro, nosso contêiner Flexbox está funcionando e os títulos dos eventos agora são um pouco maiores (**20px**) devido à nova regra global de estilo que adicionamos. 

6.6 Observe o que acontece quando navegamos para a rota ``About``. Ver figura abaixo.

![route_about](img_readme/route_about.jpg)

> Observe que o conteúdo desta página "_This is an about page_" aparece no canto inferior esquerdo. Portanto, precisamos corrigir esse posicionamento um pouco mais adiante.

> Observe também que estamos vendo aquele header ``<h1>`` exibindo “_Events For Good_”. Isso nos diz que podemos colocar o conteúdo no template do nosso ``App.vue`` que queremos que seja exibido globalmente em todas as visualizações do nosso aplicativo. Isso pode ser útil para coisas como barra de pesquisa, cabeçalho ou uma barra de navegação, como já temos aqui.

6.7 Mas, para o nosso caso de uso, não precisamos que o título apareça em todas as visualizações. Vamos então colocá-lo no arquivo "**src/views/HomeView.vue**". Abra-o e altere-o com o código abaixo.

```
...
<template>
  <h1>Events For Good</h1>
  <div class="events">
    <EventCard v-for="event in events" :key="event.id" :event="event" />
  </div>
</template>
...
```

> Agora, esse título aparecerá apenas em uma rota ``Home``.

6.8 Por fim, para corrigir este problema de posicionamento da página ``About``, precisamos apenas remover alguns estilos padrão. Abra o arquivo "**src/views/AboutView.vue**" e altere o seu conteúdo pelo que está abaixo.


```
<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<style>
/* @media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
} */
```

Você verá algo como a figura abaixo.

![route_about_2](img_readme/route_about_2.jpg)


### **Passo 7. Fazendo o Fechamento**

Vimos muita coisa. Aprendemos o que é um componente de arquivo único ``.vue``, como ele é composto (com estilos com atributo ``scoped`` versus estilos globais) e como começar a usar esses componentes para criar um aplicativo Vue.