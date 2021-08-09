package com.bls_tool.controller;

import com.bls_tool.repositories.VerdictRepository;
import com.bls_tool.model.type.Verdict;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;


import java.util.List;

@Controller
public class SearchController {
    private Page<Verdict> searchResult;
    // private String filenumberRegex = "(((VGS|RiZ\\s?s?\\(R\\)|KZR|VRG|RiZ|EnRB|StbSt\\s?\\(B\\)|AnwZ\\s?\\(Brfg\\)|RiSt|PatAnwSt\\s?\\(R\\)|AnwZ\\s?\\(B\\)|PatAnwZ|EnVZ|AnwSt\\s?\\(B\\)|NotSt\\s?\\(Brfg\\)|KVZ|KZB|AR\\s?\\(Ri\\)|NotZ\\s?\\(Brfg\\)|RiSt\\s?\\(B\\)|AnwZ\\s?\\(P\\)|EnZB|RiSt\\s?\\(R\\)|NotSt\\s?\\(B\\)|AnwSt|WpSt\\s?\\(R\\)|KVR|AR\\s?\\(Kart\\)|EnZR|StbSt\\s?\\(R\\)|WpSt\\s?\\(B\\)|KZA|AR\\s?\\(Enw\\)|AnwSt\\s?\\(R\\)|KRB|RiZ\\s?\\(B\\)|PatAnwSt\\s?\\(B\\)|EnVR|AnwZ|NotZ|EnZA|AR)\\s\\d+/\\d+)|((GSZ|LwZB|WpSt\\s?\\(B\\)|AnwZ|LwZR|KVZ|EnRB|PatAnwSt\\s?\\(B\\)|ARP|VGS|WpSt\\s?\\(R\\)|RiSt\\s?\\(B\\)|EnZA|KRB|AnwSt\\s?\\(R\\)|NotSt\\s?\\(Brfg\\)|EnVR|LwZA|ZB|AR\\s?\\(Vollz\\)|StB|ZR|AR\\s?\\(VS\\)|BJs|BLw|NotZ\\s?\\(Brfg\\)|RiZ\\s?\\(B\\)|PatAnwSt\\s?\\(R\\)|AK|RiZ|PatAnwZ|ARs|StbSt\\s?\\(R\\)|VRG|NotSt\\s?\\(B\\)|AR\\s?\\(Enw\\)|AR\\s?\\(VZ\\)|StE|KVR|AR\\s?\\(Ri\\)|AR|AnwSt|NotZ|StbSt\\s?\\(B\\)|StR|ZA|AnwZ\\s?\\(B\\)|EnZR|AR\\s?\\(Kart\\)|GSSt|AnwZ\\s?\\(P\\)|ZR\\s?\\(Ü\\)|AnwZ\\s?\\(Brfg\\)|KZB|BGns|KZR|RiSt|KZA|BAusl|AnwSt\\s?\\(B\\)|BGs|RiZ\\s?\\(R\\)|EnZB|RiSt\\s?\\(R\\)|ARZ|EnVZ)\\s\\d+/\\d+)|([I+|IV|V|VI|VII|VIII|IX|X|XI|XII|1-6]+[a-z]?\\s[A-Za-z()]{2,20}\\s\\d+/\\d\\d))";
    private String filenumberRegex =  "(((VGS|RiZ\\s?s?\\(R\\)|KZR|VRG|RiZ|EnRB|StbSt\\s?\\(B\\)|AnwZ\\\\s?\\(Brfg\\)|RiSt|PatAnwSt\\s?\\(R\\)|AnwZ\\s?\\(B\\)|PatAnwZ|EnVZ|AnwSt\\s?\\(B\\)|NotSt\\s?\\(Brfg\\)|KVZ|KZB|AR\\s?\\(Ri\\)|NotZ\\s?\\(Brfg\\)|RiSt\\s?\\(B\\)|AnwZ\\s?\\(P\\)|EnZB|RiSt\\s?\\(R\\)|NotSt\\s?\\(B\\)|AnwSt|WpSt\\s?\\(R\\)|KVR|AR\\s?\\(Kart\\)|EnZR|StbSt\\s?\\(R\\)|WpSt\\s?\\(B\\)|KZA|AR\\s?\\(Enw\\)|AnwSt\\s?\\(R\\)|KRB|RiZ\\s?\\(B\\)|PatAnwSt\\s?\\(B\\)|EnVR|AnwZ|NotZ|EnZA|AR)\\s\\d+/\\d+)|((GSZ|LwZB|WpSt\\s?\\(B\\)|AnwZ|LwZR|KVZ|EnRB|PatAnwSt\\s?\\(B\\)|ARP|VGS|WpSt\\s?\\(R\\)|RiSt\\s?\\(B\\)|EnZA|KRB|AnwSt\\s?\\(R\\)|NotSt\\s?\\(Brfg\\)|EnVR|LwZA|ZB|AR\\s?\\(Vollz\\)|StB|ZR|AR\\s?\\(VS\\)|BJs|BLw|NotZ\\s?\\(Brfg\\)|RiZ\\s?\\(B\\)|PatAnwSt\\s?\\(R\\)|AK|RiZ|PatAnwZ|ARs|StbSt\\s?\\(R\\)|VRG|NotSt\\s?\\(B\\)|AR\\s?\\(Enw\\)|AR\\s?\\(VZ\\)|StE|KVR|AR\\s?\\(Ri\\)|AR|AnwSt|NotZ|StbSt\\s?\\(B\\)|StR|ZA|AnwZ\\s?\\(B\\)|EnZR|AR\\s?\\(Kart\\)|GSSt|AnwZ\\s?\\(P\\)|ZR\\s?\\(Ü\\)|AnwZ\\s?\\(Brfg\\)|KZB|BGns|KZR|RiSt|KZA|BAusl|AnwSt\\s?\\(B\\)|BGs|RiZ\\s?\\(R\\)|EnZB|RiSt\\s?\\(R\\)|ARZ|EnVZ)\\s\\d+/\\d+)|((I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|\\d\\d?)[a-z]?\\s[A-Z][A-Za-z()]{0,20}\\s\\d+/\\d\\d))";

    //String dateRegex = "(3[01]|[12][0-9]|0?[1-9]).(1[012]|0?[1-9]).((?:19|20)[0-9][0-9])";
    String dateRegex = "[0-3][0-9]\\.[0-1][0-9]\\.[1-2][0-9][0-9][0-9]";  //todo andere schreibweisen
    //String dateRegex = "\d{2}.\d{2}.\d{4}";
    private Pattern filenumberPattern = Pattern.compile(filenumberRegex);
    private Pattern datePattern = Pattern.compile(dateRegex);
    private Matcher matcher;

    @Autowired
    private VerdictRepository verdictRepository;

    @GetMapping("/search")
    @ResponseBody
    public Page<Verdict> search(@RequestParam(required = false) String query, @RequestParam(required = false) Integer page) {
        matcher = filenumberPattern.matcher(query);
        if(page == null) {
            page = 0;
        }
        // Unterschiedliche Suchansätze je nach Suchanfrage:
        if(matcher.matches()) { // Suche nach Aktenzeichen
            String encoded = query;
            Verdict searched = null;
            List<Verdict> searchResultList;
            // versuche die Suchanfrage zu codieren
            // damit sie der Syntax des Aktenzeichen-Feldes in der ElasticSearch Datenbank entspricht:
            try {
                encoded = URLEncoder.encode(query, StandardCharsets.UTF_8.toString());
            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            }
            // Suche im Aktenzeichen-Feld
            searchResult = verdictRepository.findAllByFilenumberLike(encoded, PageRequest.of(page, 9));
            // finde das Urteil dessen Aktenzeichen genau zu der Suchanfrage passt, sofern vorhanden
            for(Verdict verdict : searchResult) {
                for(String s : verdict.getFilenumber()) {
                    if(s.equals(query)) {
                        searched = verdict;
                        break;
                    }
                }
            }
            if(searched != null) {
                searchResultList = searchResult.toList();
                List<Verdict> modifiableSearchResults = new ArrayList<>();
                for(Verdict v : searchResultList) {
                    modifiableSearchResults.add(v);
                }
                // prüfe ob Urteil mit dem exact passenden Aktenzeichen am Anfang der Ergebnisliste ist.
                // wenn nicht, dann füge es am Anfang hinzu:
                if(!modifiableSearchResults.get(0).equals(searched)) {
                    if(modifiableSearchResults.contains(searched)) {
                        int index = modifiableSearchResults.indexOf(searched);
                        modifiableSearchResults.remove(index);
                    }
                    modifiableSearchResults.add(0, searched);
                }
                searchResult = new PageImpl<>(modifiableSearchResults, PageRequest.of(0, 9), searchResultList.size());
            }
            return searchResult;
        }
        else {
            matcher = datePattern.matcher(query);
            if (matcher.matches()) { // Suche nach Datum
                // codiere Suchanfrage in richtiges Format
                String[] date = query.split("\\.");
                String encoded = "";
                for (String s : date) {
                    encoded = s + encoded;
                }
                // suche im Datum-Feld
                searchResult = verdictRepository.findAllByDate(encoded, PageRequest.of(page, 9));
            }
            else { // normale Suche nach Suchbegriffen in den relevanten Textfeldern der Urteile
                // zuerst Suche in Titeln:
                searchResult = verdictRepository.findAllByTitleLike(query, PageRequest.of(page, 9));
                // sobald Titelsuchergebnisse erschöpft sind, suche in weiteren Textfeldern:
                if(page > searchResult.getTotalPages()) {
                    searchResult = verdictRepository.findAllByTenorOrOffenseOrReasonsOrReasonfordecision(query, query, query, query, PageRequest.of(page, 9));
                }
            }
        }
        return searchResult;
    }

    @GetMapping("/newest")
    @ResponseBody
    // gibt die neusten Urteile nach dem Datum sortiert wieder um diese auf der Startseite anzuzeigen
    public Page<Verdict> newest(@RequestParam(required = false) Integer page) {
        if(page == null) {
            page = 0;
        }
        Page<Verdict> verdictByQuery =
                verdictRepository.findVerdictBy("",
                        PageRequest.of(page, 9, Sort.by(Sort.Direction.DESC, "date")));

        return verdictByQuery;
    }
}
