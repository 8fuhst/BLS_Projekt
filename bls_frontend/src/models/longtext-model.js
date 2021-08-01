/**
 * Model for the entries in a verdict longtext
 */
export class LongtextModel {
    /**
     * Constructor
     * @param prefix The prefix/heading of the entry
     * @param text The text/body of the entry
     * @param indices The indices which are present in this entry, important for reference association
     */
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