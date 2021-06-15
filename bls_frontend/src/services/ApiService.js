import {VerdictModel} from "@/models/verdict-model";

export default class ApiService {

    async fetchVerdicts(query, page) {
        try {
            const res = await fetch(process.env.VUE_APP_BASE_API_URL + `/search?query=` + query + `&page=` + page)
            let data = await res.json()
            data = data.content.map((verdict) => new VerdictModel(verdict))
            return data
        } catch (e) {
            console.log('Error requesting verdicts by query: ' + e)
        }
    }

    async fetchVerdict(documentnumber) {
        try {
            const res = await fetch(process.env.VUE_APP_BASE_API_URL + `/verdict?documentnumber=` + documentnumber)
            let data = await res.json()
            data = new VerdictModel(data).withModelledOffenseAndReasons()
            return data
        } catch (e) {
            console.log('Error requesting verdict by documentnumber: ' + e)
        }
    }

    async fetchNewest(page) {
        try {
            const res = await fetch(process.env.VUE_APP_BASE_API_URL + `/newest?page=` + page)
            let data = await res.json()
            data = data.content.map((verdict) => new VerdictModel(verdict))
            return data
        } catch (e) {
            console.log('Error requesting newest verdicts: ' + e)
        }
    }
}