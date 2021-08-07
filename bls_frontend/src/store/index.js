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
    moreResults: true,
  },
  mutations: {
    /**
     * Sets the current verdicts loaded
     */
    setVerdicts(state, payload) {
      state.verdicts = payload
      state.moreResults = payload.length !== 0
    },
    /**
     * Appends verdicts to the current verdicts loaded
     */
    appendVerdicts(state, payload) {
      state.verdicts = state.verdicts.concat(payload)
      state.moreResults = payload.length !== 0
    },
    /**
     * Sets the current verdict thats active
     */
    setVerdict(state, payload) {
      state.currentVerdict = payload
    },
    /**
     * Sets the fetching state
     */
    setFetching(state, payload) {
      state.fetching = payload
    },
    /**
     * Sets the page for search queries
     */
    setPage(state, payload) {
      state.page = payload
    },
    /**
     * Sets the current active verdictnode
     */
    setVerdictNode(state, payload) {
      state.verdictNode = payload
    },
    /**
     * Caches verdicts loaded for later use
     */
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
    /**
     * Caches verdictnodes for later use
     */
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
    /**
     * Sets a new query, then fetches and caches new verdicts
     */
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
    /**
     * Fetches and caches the newest verdicts
     */
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
    /**
     * Fetches or loads verdict from cache by its documentnumber, then sets it active
     */
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
    /**
     * Fetches or loads verdict from cache by its filenumber, then returns it
     */
    async getVerdictByFilenumber(state, filenumber) {
      const index = this.state.verdictCache.findIndex( (verdict) => {
        return verdict.filenumber === filenumber
      })

      if (index === -1) {
        const verdict = await apiService.fetchVerdictByFilenumber(filenumber)
        if (verdict) {
          state.commit('cacheVerdicts', [verdict])
          return verdict
        } else {
          return undefined
        }
      }

      return this.state.verdictCache[index]
    },
    /**
     * Fetches or loads verdictnode from cache, then sets it active
     */
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
    getMoreResults: state => state.moreResults
  }
})
