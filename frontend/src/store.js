import Vue from 'vue'
import Vuex from 'vuex'
import api from './api.js'

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        geneInput: [],
        enrichedPathways: {}
    },
    mutations: {
        'ADD_GENE_INPUT' (state, geneInput) {
            state.geneInput = geneInput
        },
        'ADD_RESULTS' (state, enrichedPathways) {
            state.enrichedPathways = enrichedPathways
        },
        'API_FAIL' (state, error) {
            console.error(error)
        },
    },
    actions: {
        updateQueryList(store, geneListArr) {
            store.commit('ADD_GENE_INPUT', geneListArr);
            api.post(`/api/gene-enrichment`, {'genes': geneListArr})
                .then(
                    response => {
                        console.log(response.body);
                        store.commit('ADD_RESULTS', response.body)
                    }
                )
                .catch(
                    error => {
                        store.commit('API_FAIL', error);
                    }
                )
        }
    }
});

export default store;
