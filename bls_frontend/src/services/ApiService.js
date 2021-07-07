import {VerdictModel} from "@/models/verdict-model";
import {VerdictNodeModel} from "@/models/verdict-node-model";

export default class ApiService {

    async fetchVerdicts(query, page) {
        try {
            const res = await fetch(process.env.VUE_APP_BASE_API_URL + `/search?query=` + query + `&page=` + page)
            let data = await res.json()
            data = data.content.map((verdict) => new VerdictModel(verdict).withModelledOffenseAndReasons())
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

    async fetchVerdictByFilenumber(filenumber) {
        try {
            const res = await fetch(process.env.VUE_APP_BASE_API_URL + `/verdictFN?filenumber=` + filenumber)
            const data = await res.json()
            if (data) {
                const verdict = new VerdictModel(data).withModelledOffenseAndReasons()
                return verdict
            } else {
                return undefined
            }
        } catch (e) {
            console.log('Error requesting verdict by filenumber: ' + e)
            return undefined
        }
    }

    async fetchNewest(page) {
        try {
            const res = await fetch(process.env.VUE_APP_BASE_API_URL + `/newest?page=` + page)
            let data = await res.json()
            data = data.content.map((verdict) => new VerdictModel(verdict).withModelledOffenseAndReasons())
            return data
        } catch (e) {
            console.log('Error requesting newest verdicts: ' + e)
        }
    }

    async fetchVerdictNode(filenumber) {
        try {
            const res = await fetch( process.env.VUE_APP_BASE_API_URL + `/verdictNode?filenumber=` + filenumber)
            let data = await res.json()
            return new VerdictNodeModel(data)
        } catch (e) {
            console.log('Error requesting verdict node: ' + e)
            return new VerdictNodeModel(null)
        }
    }

    async downloadVerdictData(documentnumber) {
        try {
            const res = await fetch(process.env.VUE_APP_BASE_API_URL + `/verdict?documentnumber=` + documentnumber)
            const verdict = await res.json()

            const txtData = JSON.stringify(verdict)
            const txtName = documentnumber + ".json"
            const blob = new Blob([txtData])
            const url = URL.createObjectURL(blob)

            const download = (path, filename) => {
                const anchor = document.createElement('a')
                anchor.href = path
                anchor.download = filename
                document.body.appendChild(anchor)
                anchor.click()
                document.body.removeChild(anchor)
            }
            download(url, txtName)
        } catch (e) {
            console.log('Error downloading verdict: ' + e)
        }
    }
}