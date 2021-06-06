export class VerdictModel {
    constructor(verdict) {
        if (verdict) {
            this.date = verdict.date;
            this.mitwirkung = verdict.mitwirkung;
            this.identifier = verdict.identifier;
            this.other = verdict.other;
            this.reasonsForDecision = verdict.reasonsForDecision;
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
        }

    }
}