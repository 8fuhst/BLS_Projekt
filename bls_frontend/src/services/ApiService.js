import {VerdictModel} from "@/models/verdict-model";

export default class ApiService {
    async fetchVerdicts(query) {
        try {
            const res = await fetch(`api/search?query=` + query)
            let data = await res.json()
            data = data.content.map((verdict) => new VerdictModel(verdict))
            return data
        } catch (e) {
            console.log('Error requesting verdicts!')
        }
    }

    async fetchVerdict() {
        try {
            const res = await fetch(`api/verdict`)
            return await res.json()
        } catch (e) {
            console.log('Error requesting verdicts!')
        }
    }
}