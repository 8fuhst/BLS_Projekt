export class VerdictNodeModel {
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