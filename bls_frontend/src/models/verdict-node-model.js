/**
 * Model for the verdictnodes
 */
export class VerdictNodeModel {
    /**
     * Constructor
     * @param verdictNode The data of the verdictnode
     */
    constructor(verdictNode) {
        if (verdictNode) {
            this.filenumber = verdictNode.filenumber;
            this.outgoingReferenceList = verdictNode.outgoingReferenceList;
            this.outgoingReferenceSet = verdictNode.outgoingReferenceSet;
            this.incomingReferenceSet = verdictNode.incomingReferenceSet;
            this.incomingCount = verdictNode.incomingCount;
        } else {
            this.filenumber = '';
            this.outgoingReferenceList = [];
            this.outgoingReferenceSet = [];
            this.incomingReferenceSet = [];
            this.incomingCount = 0;
        }

    }
}