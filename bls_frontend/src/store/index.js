import Vue from 'vue'
import Vuex from 'vuex'
import ApiService from "../services/ApiService.js";
import {VerdictModel} from "@/models/verdict-model";
import {VerdictNodeModel} from "@/models/verdict-node-model";

const apiService = new ApiService()
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    verdicts: [],
    currentVerdict: new VerdictModel(null),
    fetching: false,
    page: 0,
    verdictNode: new VerdictNodeModel(null),
    verdictCache: [],
    verdictNodeCache: [],
  },
  mutations: {
    setVerdicts(state, payload) {
      state.verdicts = payload
    },
    appendVerdicts(state, payload) {
      state.verdicts = state.verdicts.concat(payload)
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
    cacheVerdicts(state, payload) {
      payload.forEach( (verdict) => {
        const index = state.verdictCache.findIndex( (cachedVerdict) => {
          return cachedVerdict.documentnumber === verdict.documentnumber
        })

        if (index === -1) {
          state.verdictCache.push(verdict)
        }
      })
    },
    cacheVerdictNodes(state, payload) {
      payload.forEach( (node) => {
        const index = this.state.verdictNodeCache.findIndex( (cachedNode) => {
          return cachedNode.documentnumber === node.documentnumber
        })

        if (index === -1) {
          this.state.verdictNodeCache.push(node)
        }
      })
    }
  },
  actions: {
    async setQuery(state, newQuery) {
      state.commit('setFetching', true)
      const verdicts = await apiService.fetchVerdicts(newQuery, this.state.page)
      state.commit('setFetching', false)
      if (this.state.page === 0) {
        state.commit('setVerdicts', verdicts)
      } else {
        state.commit('appendVerdicts', verdicts)
      }
      state.commit('cacheVerdicts', verdicts)
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
      state.commit('cacheVerdicts', verdicts)
    },
    async setCurrent(state, documentnumber) {
      const index = this.state.verdictCache.findIndex( (verdict) => {
        return verdict.documentnumber === documentnumber
      })

      if (index !== -1) {
        state.commit('setVerdict', this.state.verdictCache[index])
      } else {
        const verdict = await apiService.fetchVerdict(documentnumber)
        state.commit('cacheVerdicts', [verdict])
        state.commit('setVerdict', verdict)
      }
    },
    async getVerdictByFilenumber(state, filenumber) {
      const index = this.state.verdictCache.findIndex( (verdict) => {
        return verdict.filenumber === filenumber
      })

      if (index === -1) {
        // TODO: Request by filenumber richtig machen sobald es geht
        state.commit('setPage', 0)
        await state.dispatch('setQuery', filenumber)
        const verdict = this.state.verdicts[0]
        state.commit('cacheVerdicts', [verdict])
        return verdict
      }

      return this.state.verdictCache.find( (verdict) => {
        return verdict.filenumber === filenumber
      })
    },
    async setVerdictNode(state, filenumber) {
      const index = this.state.verdictNodeCache.findIndex( (node) => {
        return node.filenumber === filenumber
      })

      if (index !== -1) {
        state.commit('setVerdictNode', this.state.verdictNodeCache[index])
      } else {
        const verdictNode = await apiService.fetchVerdictNode(filenumber)
        state.commit('cacheVerdicts', [verdictNode])
        state.commit('setVerdictNode', verdictNode)
      }
    }
  },
  modules: {
  },
  getters: {
    getVerdicts: state => state.verdicts,
    getCurrentVerdict: state => state.currentVerdict,
    getFetching: state => state.fetching,
    getPage: state => state.page,
    getVerdictNode: state => state.verdictNode,
    getCachedVerdicts: state => state.verdictCache,
    getCachedVerdictNodes: state => state.verdictNodeCache,
  }
})
