import Vue from 'vue'
import Vuex from 'vuex'
import ApiService from "../services/ApiService.js";
import {VerdictModel} from "@/models/verdict-model";
import {VerdictNodeModel} from "@/models/verdict-node-model";

const apiService = new ApiService()
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    query: '',
    verdicts: [],
    currentVerdict: new VerdictModel(null),
    fetching: false,
    page: 0,
    verdictNode: new VerdictNodeModel(null),
  },
  mutations: {
    setVerdicts(state, payload) {
      state.verdicts = payload
    },
    appendVerdicts(state, payload) {
      state.verdicts = state.verdicts.concat(payload)
    },
    setQuery(state, payload) {
      state.query = payload
    },
    setVerdict(state, payload) {
      state.currentVerdict = payload
    },
    setFetching(state, payload) {
      state.fetching = payload
    },
    setPage(state, payload) {
      state.page = payload
    },
    setVerdictNode(state, payload) {
      state.verdictNode = payload
    },
  },
  actions: {
    async setQuery(state, newQuery) {
      state.commit('setQuery', newQuery)
      state.commit('setFetching', true)
      const verdicts = await apiService.fetchVerdicts(newQuery, this.state.page)
      state.commit('setFetching', false)
      if (this.state.page === 0) {
        state.commit('setVerdicts', verdicts)
      } else {
        state.commit('appendVerdicts', verdicts)
      }
    },
    async getNewest(state) {
      state.commit('setFetching', true)
      const verdicts = await apiService.fetchNewest(this.state.page)
      state.commit('setFetching', false)
      if (this.state.page === 0) {
        state.commit('setVerdicts', verdicts)
      } else {
        state.commit('appendVerdicts', verdicts)
      }
    },
    async setCurrent(state, documentnumber) {
      const verdict = await apiService.fetchVerdict(documentnumber)
      state.commit('setVerdict', verdict)
    },
    async setVerdictNode(state, filenumber) {
      const verdictNode = await apiService.fetchVerdictNode(filenumber)
      state.commit('setVerdictNode', verdictNode)
    }
  },
  modules: {
  },
  getters: {
    getVerdicts: state => state.verdicts,
    getQuery: state => state.query,
    getCurrentVerdict: state => state.currentVerdict,
    getFetching: state => state.fetching,
    getPage: state => state.page,
    getVerdictNode: state => state.verdictNode,
  }
})
