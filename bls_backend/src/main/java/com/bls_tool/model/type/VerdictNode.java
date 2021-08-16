package com.bls_tool.model.type;

import net.minidev.json.JSONArray;
import org.springframework.data.annotation.Id;
import org.springframework.data.elasticsearch.annotations.Document;
import org.springframework.data.elasticsearch.annotations.Field;
import org.springframework.data.elasticsearch.annotations.FieldType;

@Document(indexName = "verdict_nodes")
public class VerdictNode {
    @Id
    private String _id;
    @Field(type = FieldType.Keyword, name = "filenumber")
    private String filenumber;
    @Field(type = FieldType.Nested, name = "outgoing_reference_list")
    private JSONArray outgoingReferenceList;
    @Field(type = FieldType.Text, name = "outgoing_reference_set")
    private String[] outgoingReferenceSet;
    @Field(type = FieldType.Text, name = "incoming_reference_set")
    private String[] incomingReferenceSet;
    @Field(type = FieldType.Integer, name = "incoming_count")
    private int incomingCount;

    public String getFilenumber() {
        return filenumber;
    }

    public JSONArray getOutgoingReferenceList() {
        return outgoingReferenceList;
    }

    public String[] getOutgoingReferenceSet() {
        return outgoingReferenceSet;
    }

    public String[] getIncomingReferenceSet() {
        return incomingReferenceSet;
    }

    public int getIncomingCount() {
        return incomingCount;
    }
}
