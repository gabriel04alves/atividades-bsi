const app = Vue.createApp({
    data() {
        return {
            product: 'Socks',
            description: 'This is a description.',
            image: './assets/images/socks_blue.jpg',
            url: 'https://github.com/gabriel04alves',
            inventory: 8,
            onSale: true
        }
    }
})