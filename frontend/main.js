import Vue from 'vue'
import VueRouter from 'vue-router';

import store from './src/store.js';

import App from './App.vue'
import GeneInput from './assets/components/GeneInput.vue';
import Results from './assets/components/Results.vue';

Vue.use(VueRouter);


const routes = [
    { path: '/', component: GeneInput },
    { path: '/results', component: Results },
];

const router = new VueRouter({ routes });


// eslint-disable-next-line no-new
new Vue({
    el: '#app',
    router: router,
    store: store,
    render: h => h(App)
});
