package com.bls_tool.model.type;

import net.minidev.json.JSONArray;
import net.minidev.json.JSONObject;
import org.springframework.data.annotation.Id;
import org.springframework.data.elasticsearch.annotations.Document;
import org.springframework.data.elasticsearch.annotations.Field;
import org.springframework.data.elasticsearch.annotations.FieldType;


@Document(indexName = "verdicts3") //
public class Verdict {
    @Id
    private String _id;
    @Field(type = FieldType.Keyword, name = "court")
    private Court court; // Gericht
    @Field(type = FieldType.Integer, name = "date")
    private int date; // Entscheidungsdatum
    @Field(type = FieldType.Keyword, name = "filenumber")
    private String[] filenumber; // Aktenzeichen
    @Field(type = FieldType.Keyword, name = "ecli")
    private String ecli; // ECLI
    @Field(type = FieldType.Keyword, name = "documenttype")
    private String documenttype; // Dokumenttyp
    @Field(type = FieldType.Keyword, name = "norms")
    private String[] norms; // Normen
    @Field(type = FieldType.Text, name = "reasons")
    private String[] reasons; // Gründe
    @Field(type = FieldType.Keyword, name = "documentnumber")
    private String documentnumber; // Dokumentennummer
    @Field(type = FieldType.Text, name = "courtlocation")
    private String courtlocation; // Gerichts-Ort todo
    @Field(type = FieldType.Text, name = "spruchkoerper")
    private String spruchkoerper; // Spruchkörper
    @Field(type = FieldType.Text, name = "previouscourt")
    private String[] previouscourt; // Vorinstanzen
    @Field(type = FieldType.Text, name = "region")
    private String region;
    @Field(type = FieldType.Text, name = "mitwirkung")
    private String mitwirkung;
    @Field(type = FieldType.Text, name = "title")
    private String title; // Titelzeile
    @Field(type = FieldType.Text, name = "keysentence")
    private String[] keysentence; // Leitsatz
    @Field(type = FieldType.Text, name = "miscsentence")
    private String miscsentence; // Sonstosatz
    @Field(type = FieldType.Text, name = "tenor")
    private String[] tenor;
    @Field(type = FieldType.Text, name = "offense")
    private String[] offense; // Tatbestand
    @Field(type = FieldType.Text, name = "reasonfordecision")
    private String[] reasonfordecision; // Entscheidungsgründe
    @Field(type = FieldType.Text, name = "abwmeinung")
    private String abwmeinung; // abwmeinung todo was ist das?
    @Field(type = FieldType.Text, name = "other")
    private String other; // sonstlt
    @Field(type = FieldType.Keyword, name = "identifier")
    private String identifier; //Juris Link
    @Field(type = FieldType.Keyword, name = "successful")
    private String successful; // Ob das Verfahren erfolgreich war

    public String[] getKeywords() {
        return keywords;
    }

    @Field(type = FieldType.Text, name = "keywords")
    private String[] keywords;
    //private String plaintext; // Text ohne Formatierungen

    public String getDocumentnumber() {
        return documentnumber;
    }

    public Court getCourt(){
        return court;
    }

    public int getDate(){
        return date;
    }

    public String[] getFilenumber(){
        return filenumber;
    }

    public String getEcli(){
        return ecli;
    }

    public String getDocumenttype(){
        return documenttype;
    }

    public String[] getNorms(){
        return norms;
    }

    public String getAbwmeinung() {return abwmeinung; }

    public String getOther() { return other; }

    public String getIdentifier() { return identifier; }

    public String getCourtlocation() {
        return courtlocation;
    }

    public String getSpruchkoerper() {
        return spruchkoerper;
    }

    public String getRegion() {
        return region;
    }

    public String getMitwirkung() {
        return mitwirkung;
    }

    public String getTitle() {
        return title;
    }

    public String[] getReasons() {
        return reasons;
    }

    public String[] getReasonsForDecision() {
        return reasonfordecision;
    }

    public String[] getKeysentence() {
        return keysentence;
    }

    public String getMiscsentence() {
        return miscsentence;
    }

    public String[] getTenor() {
        return tenor;
    }

    public String[] getOffense() {
        return offense;
    }

    public String[] getPreviouscourt() {
        return previouscourt;
    }

    public String getSuccessful() {
        return successful;
    }

    public JSONObject toJSON() {
        JSONObject result = toJsonMetadata();

        result.put("offense",offense);
        result.put("reasons", reasons);
        result.put("reasonfordecision", reasonfordecision);
        result.put("abwmeinung", abwmeinung);
        result.put("other", other);
        result.put("identifier", identifier);
        return result;
    }

    public JSONObject toJsonMetadata() {
        JSONObject result = new JSONObject();
        result.put("court", court);
        result.put("date", date);
        result.put("courtlocation", courtlocation);
        result.put("spruchkoerper", spruchkoerper);
        result.put("region", region);
        result.put("mitwirkung", mitwirkung);
        JSONArray previouscourts_json = new JSONArray();
        for(String s : previouscourt) {
            previouscourts_json.add(s);
        }
        result.put("previouscourts", previouscourts_json);
        JSONArray filenumber_json = new JSONArray();
        for(String s : filenumber) {
            filenumber_json.add(s);
        }
        result.put("filenumber", filenumber_json);
        result.put("ecli", ecli);
        result.put("documenttype", documenttype);
        JSONArray norms_json = new JSONArray();
        for(String n: norms){
            norms_json.add(n);
        }
        result.put("norms", norms_json);
        result.put("tenor",tenor);
        result.put("keysentence", keysentence);
        result.put("documentnumber", documentnumber);
        result.put("title", title);
        return result;
    }
}