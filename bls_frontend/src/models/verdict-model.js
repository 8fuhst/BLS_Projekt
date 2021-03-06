import {LongtextModel} from "@/models/longtext-model";

/**
 * Model for the verdicts
 */
export class VerdictModel {
    /**
     * Constructor
     * @param verdict The data of a verdict
     */
    constructor(verdict) {
        if (verdict) {
            this.date = verdict.date;
            this.mitwirkung = verdict.mitwirkung;
            this.identifier = verdict.identifier;
            this.other = verdict.other;
            if (verdict.reasons.length > 0) {
                this.reasonsForDecision = verdict.reasons;
            } else {
                this.reasonsForDecision = verdict.reasonsForDecision;
            }
            this.filenumber = verdict.filenumber;
            this.offense = verdict.offense;
            this.documenttype = verdict.documenttype;
            this.court = verdict.court;
            this.keysentence = verdict.keysentence;
            this.spruchkoerper = verdict.spruchkoerper;
            this.tenor = verdict.tenor
            this.ecli = verdict.ecli;
            this.norms = verdict.norms;
            this.abwmeinung = verdict.abwmeinung;
            this.previouscourts = verdict.previouscourts;
            this.documentnumber = verdict.documentnumber;
            this.region = verdict.region;
            this.courtlocation = verdict.courtlocation;
            this.title = verdict.title;
            this.modelledReasonsForDecision = [];
            this.modelledOffense = [];
            if (verdict.keywords) {
                this.keywords = verdict.keywords;
            } else {
                this.keywords = []
            }
        } else {
            this.date = '';
            this.mitwirkung = '';
            this.identifier = '';
            this.other = '';
            this.reasonsForDecision = [];
            this.filenumber = [];
            this.offense = [];
            this.documenttype = '';
            this.court = '';
            this.keysentence = '';
            this.spruchkoerper = '';
            this.tenor = [];
            this.ecli = '';
            this.norms = [];
            this.abwmeinung = '';
            this.previouscourts = '';
            this.documentnumber = '';
            this.region = '';
            this.courtlocation = '';
            this.title = '';
            this.modelledReasonsForDecision = [];
            this.modelledOffense = [];
            this.keywords = [];
        }

    }

    /**
     * Sets the filenumber and returns the verdict
     * @param filenumber New filenumber
     * @returns {VerdictModel} The new verdictmodel
     */
    withFilenumber(filenumber) {
        this.filenumber = filenumber
        return this
    }

    /**
     * Creates models for the verdict longtext entries for the Offense and Reasons section
     * @returns {VerdictModel} The new verdictmodel
     */
    withModelledOffenseAndReasons() {
        let i
        if (this.reasonsForDecision) {
            for (i = 0; i < this.reasonsForDecision.length; i++) {
                if (!this.reasonsForDecision[i].replace(/\s/g, '').length) {
                    continue
                }
                if (isNaN(this.reasonsForDecision[i])) {
                    this.modelledReasonsForDecision.push(new LongtextModel(this.reasonsForDecision[i], null, [i]))
                } else {
                    this.modelledReasonsForDecision.push(new LongtextModel(this.reasonsForDecision[i], this.reasonsForDecision[i + 1], [i, i+1]))
                    i++
                }
            }
        }

        if (this.offense) {
            for (i = 0; i < this.offense.length; i++) {
                if (!this.offense[i].replace(/\s/g, '').length) {
                    continue
                }
                if (isNaN(this.offense[i])) {
                    this.modelledOffense.push(new LongtextModel(this.offense[i], null, [i]))
                } else {
                    this.modelledOffense.push(new LongtextModel(this.offense[i], this.offense[i + 1], [i, i+1]))
                    i++
                }
            }
        }
        return this
    }
}