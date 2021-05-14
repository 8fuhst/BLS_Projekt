
export default class ApiService {
    async fetchVerdicts(query) {
        try {
            const res = await fetch(`api/search?query=` + query)
            return await res.json()
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