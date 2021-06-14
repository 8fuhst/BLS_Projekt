import {VerdictModel} from "@/models/verdict-model";

export default class ApiService {
    constructor() {
        this.urlBase = 'http://basecamp-demos.informatik.uni-hamburg.de:8080/bls_backend-0.0.1-SNAPSHOT'
    }

    async fetchVerdicts(query, page) {
        try {
            const res = await fetch(`api/search?query=` + query + `&page=` + page)
            let data = await res.json()
            data = data.content.map((verdict) => new VerdictModel(verdict))
            return data
        } catch (e) {
            console.log('Error requesting verdicts by query: ' + e)
        }
    }

    async fetchVerdict(documentnumber) {
        try {
            const res = await fetch(`api/verdict?documentnumber=` + documentnumber)
            let data = await res.json()
            data = new VerdictModel(data).withModelledOffenseAndReasons()
            return data
        } catch (e) {
            console.log('Error requesting verdict by documentnumber: ' + e)
        }
    }

    async fetchNewest(page) {
        try {
            const res = await fetch(`api/newest?page=` + page)
            let data = await res.json()
            data = data.content.map((verdict) => new VerdictModel(verdict))
            return data
        } catch (e) {
            console.log('Error requesting newest verdicts: ' + e)
        }
    }
}