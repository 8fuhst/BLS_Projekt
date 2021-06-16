import {VerdictModel} from "@/models/verdict-model";
import {VerdictNodeModel} from "@/models/verdict-node-model";

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

    async fetchVerdictNode(filenumber) {
        try {
            console.log(filenumber)
            //const res = await fetch(process.env.VUE_APP_BASE_API_URL + `/verdictNode?filenumber=` + 'IV%20ZR%2036/09')
            //let data = await res.json()
            const hardcode = JSON.parse('{\n' +
                '  "filenumber": "IV ZR 36/09",\n' +
                '  "outgoingReferenceList": [\n' +
                '    [\n' +
                '      {\n' +
                '        "vorinstanz": [\n' +
                '          [\n' +
                '            "0",\n' +
                '            "IV ZR 36/09"\n' +
                '          ]\n' +
                '        ]\n' +
                '      },\n' +
                '      {\n' +
                '        "gruende": [\n' +
                '          [\n' +
                '            "5",\n' +
                '            "X ARZ 362/02"\n' +
                '          ]\n' +
                '        ]\n' +
                '      },\n' +
                '      {\n' +
                '        "entscheidungsgruende": [\n' +
                '          \n' +
                '        ]\n' +
                '      },\n' +
                '      {\n' +
                '        "tatbestand": [\n' +
                '          \n' +
                '        ]\n' +
                '      },\n' +
                '      {\n' +
                '        "tenor": [\n' +
                '          \n' +
                '        ]\n' +
                '      },\n' +
                '      {\n' +
                '        "leitsatz": [\n' +
                '          \n' +
                '        ]\n' +
                '      }\n' +
                '    ]\n' +
                '  ],\n' +
                '  "outgoingReferenceSet": [\n' +
                '    "IV ZR 36/09,X ARZ 362/02"\n' +
                '  ],\n' +
                '  "incomingReferenceSet": [\n' +
                '    "IV ZR 36/09"\n' +
                '  ],\n' +
                '  "incomingCount": 1\n' +
                '}')
            return new VerdictNodeModel(hardcode)
        } catch (e) {
            console.log('Error requesting verdict node: ' + e)
        }
    }
}