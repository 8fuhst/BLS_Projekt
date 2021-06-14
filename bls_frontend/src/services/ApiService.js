import {VerdictModel} from "@/models/verdict-model";

export default class ApiService {
    async fetchVerdicts(query) {
        try {
            const res = await fetch('http://basecamp-demos.informatik.uni-hamburg.de:8080/bls_backend-0.0.1-SNAPSHOT/search?query=' + query)
            let data = await res.json()
            data = data.map((verdict) => new VerdictModel(verdict))
            return data
        } catch (e) {
            console.log('Error requesting verdicts by query: ' + e)
        }
    }

    async fetchVerdict(documentnumber) {
        try {
            const res = await fetch('http://basecamp-demos.informatik.uni-hamburg.de:8080/bls_backend-0.0.1-SNAPSHOT/verdict?documentnumber=' + documentnumber)
            let data = await res.json()
            data = new VerdictModel(data).withModelledOffenseAndReasons()
            return data
        } catch (e) {
            console.log('Error requesting verdict by documentnumber: ' + e)
        }
    }

    async fetchNewest() {
        try {
            const res = await fetch('http://basecamp-demos.informatik.uni-hamburg.de:8080/bls_backend-0.0.1-SNAPSHOT/newest')
            let data = await res.json()
            data = data.content.map((verdict) => new VerdictModel(verdict))
            return data
        } catch (e) {
            console.log('Error requesting newest verdicts: ' + e)
        }
    }
}