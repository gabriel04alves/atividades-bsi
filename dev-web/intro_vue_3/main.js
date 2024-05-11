const app = Vue.createApp({
    data() {
        return {
            cart: [],
            premium: true
        }
    },
    methods: {
        updateCart(id) {
            this.cart.push(id)
        },
        removeItemCart(id) {
            this.cart.pop(id)
            // console.log(this.cart)
        },
    }
})