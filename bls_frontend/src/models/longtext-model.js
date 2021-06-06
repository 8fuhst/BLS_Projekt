export class LongtextModel {
    constructor(prefix, text) {
        if (prefix) {
            this.prefix = prefix
        } else {
            this.prefix = null
        }

        if (text) {
            this.text = text
        } else {
            this.text = null
        }
    }
}