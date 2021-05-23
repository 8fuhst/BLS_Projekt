export class VerdictModel {
    constructor(verdict) {
        this.date = verdict.date;
        this.mitwirkung = verdict.mitwirkung;
        this.identifier = verdict.identifier;
        this.reasonfordecision = verdict.reasonfordecision;
        this.other = verdict.other;
        this.reasons = verdict.reasons;
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
    }
}