export class LongtextModel {
    constructor(prefix, text, indices) {
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

        if (indices) {
            this.indices = indices
        } else {
            this.indices = []
        }
    }
}