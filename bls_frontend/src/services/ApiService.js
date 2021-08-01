import {VerdictModel} from "@/models/verdict-model";
import {VerdictNodeModel} from "@/models/verdict-node-model";

export default class ApiService {

    /**
     * Fetches an array of verdicts for a specified query
     * @param query The query for the search
     * @param page The page index of the search
     * @returns {Promise<*>} Array of fetched verdicts
     */
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

    /**
     * Fetches a single verdict by its documentnumber
     * @param documentnumber The documentnumber of the verdict
     * @returns {Promise<VerdictModel>} The fetched Verdict as Verdictmodel
     */
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

    /**
     * Fetches a single verdict by its filenumber
     * @param filenumber The filenumber of the verdict
     * @returns {Promise<VerdictModel>} The fetched Verdict as Verdictmodel
     */
    async fetchVerdictByFilenumber(filenumber) {
        try {
            const res = await fetch(process.env.VUE_APP_BASE_API_URL + `/verdictFN?filenumber=` + filenumber)
            const data = await res.json()
            if (data) {
                const verdict = new VerdictModel(data).withModelledOffenseAndReasons()
                return verdict
            } else {
                return new VerdictModel(undefined).withFilenumber(filenumber)
            }
        } catch (e) {
            console.log('Error requesting verdict by filenumber: ' + e)
            return new VerdictModel(undefined).withFilenumber(filenumber)
        }
    }

    /**
     * Fetches an array of the newest verdicts
     * @param page The page index of the search
     * @returns {Promise<*>} Array of fetched verdicts
     */
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

    /**
     * Fetches a verdictnode by the filenumber of a verdict for the references
     * @param filenumber The filenumber of the verdict
     * @returns {Promise<VerdictNodeModel>} The fetched verdictnode as verdictnodemodel
     */
    async fetchVerdictNode(filenumber) {
        try {
            const res = await fetch( process.env.VUE_APP_BASE_API_URL + `/verdictNode?filenumber=` + filenumber)
            const data = await res.json()
            return new VerdictNodeModel(data)
        } catch (e) {
            console.log('Error requesting verdict node: ' + e)
            return new VerdictNodeModel(undefined)
        }
    }

    /**
     * Prepares the data of a verdict and then downloads it
     * @param documentnumber The documentnumber of the verdict
     */
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