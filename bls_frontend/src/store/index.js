import Vue from 'vue'
import Vuex from 'vuex'
import ApiService from "../services/ApiService.js";

const apiService = new ApiService()


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    query: '',
    verdicts: [],
  },
  mutations: {
    setVerdicts(state, payload) {
      state.verdicts = payload
    },
    setQuery(state, payload) {
      state.query = payload
    }
  },
  actions: {
    async setQuery(state, newQuery) {
      state.commit('setQuery', newQuery)
      const verdicts = await apiService.fetchVerdicts(newQuery)
      state.commit('setVerdicts', verdicts)
    }
  },
  modules: {
  },
  getters: {
    getVerdicts: state => state.verdicts,
    getQuery: state => state.query,
  }
})
