import {VerdictModel} from "@/models/verdict-model";

export default class ApiService {
    async fetchVerdicts(query) {
        try {
            const res = await fetch(`api/search?query=` + query)
            let data = await res.json()
            data = data.map((verdict) => new VerdictModel(verdict))
            return data
        } catch (e) {
            console.log('Error requesting verdicts by query: ' + e)
        }
    }

    async fetchVerdict(documentnumber) {
        try {
            const res = await fetch(`api/verdict?documentnumber=` + documentnumber)
            let data = await res.json()
            data = new VerdictModel(data)
            return data
        } catch (e) {
            console.log('Error requesting verdict by documentnumber: ' + e)
        }
    }

    async fetchNewest() {
        try {
            const res = await fetch(`api/newest`)
            let data = await res.json()
            data = data.content.map((verdict) => new VerdictModel(verdict))
            return data
        } catch (e) {
            console.log('Error requesting newest verdicts: ' + e)
        }
    }
}