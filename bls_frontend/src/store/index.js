import Vue from 'vue'
import Vuex from 'vuex'
import ApiService from "../services/ApiService.js";
import {VerdictModel} from "@/models/verdict-model";

const apiService = new ApiService()
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    query: '',
    verdicts: [],
    currentVerdict: new VerdictModel(null),
  },
  mutations: {
    setVerdicts(state, payload) {
      state.verdicts = payload
    },
    setQuery(state, payload) {
      state.query = payload
    },
    setVerdict(state, payload) {
      state.currentVerdict = payload
    }
  },
  actions: {
    async setQuery(state, newQuery) {
      state.commit('setQuery', newQuery)
      const verdicts = await apiService.fetchVerdicts(newQuery)
      state.commit('setVerdicts', verdicts)
    },
    async getNewest(state) {
      const verdicts = await apiService.fetchNewest()
      state.commit('setVerdicts', verdicts)
    },
    async setCurrent(state, documentnumber) {
      const verdict = await apiService.fetchVerdict(documentnumber)
      state.commit('setVerdict', verdict)
    }
  },
  modules: {
  },
  getters: {
    getVerdicts: state => state.verdicts,
    getQuery: state => state.query,
    getCurrentVerdict: state => state.currentVerdict,
  }
})
