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
    fetching: false,
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
    },
    setFetching(state, payload) {
      state.fetching = payload
    }
  },
  actions: {
    async setQuery(state, newQuery) {
      state.commit('setQuery', newQuery)
      state.commit('setFetching', true)
      const verdicts = await apiService.fetchVerdicts(newQuery)
      state.commit('setFetching', false)
      state.commit('setVerdicts', verdicts)
    },
    async getNewest(state) {
      state.commit('setFetching', true)
      const verdicts = await apiService.fetchNewest()
      state.commit('setFetching', false)
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
    getFetching: state => state.fetching,
  }
})
