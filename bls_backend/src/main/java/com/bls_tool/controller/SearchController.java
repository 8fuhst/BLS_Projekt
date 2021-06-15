package com.bls_tool.controller;

import com.bls_tool.repositories.VerdictRepository;
import com.bls_tool.model.type.Verdict;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.regex.Pattern;
import java.util.regex.Matcher;


import java.util.List;

@Controller
// @RequestMapping("/search")
public class SearchController {
    private Page<Verdict> searchResult;
    private String filenumberRegex = "(((VGS|RiZ\\s?s?\\(R\\)|KZR|VRG|RiZ|EnRB|StbSt\\s?\\(B\\)|AnwZ\\s?\\(Brfg\\)|RiSt|PatAnwSt\\s?\\(R\\)|AnwZ\\s?\\(B\\)|PatAnwZ|EnVZ|AnwSt\\s?\\(B\\)|NotSt\\s?\\(Brfg\\)|KVZ|KZB|AR\\s?\\(Ri\\)|NotZ\\s?\\(Brfg\\)|RiSt\\s?\\(B\\)|AnwZ\\s?\\(P\\)|EnZB|RiSt\\s?\\(R\\)|NotSt\\s?\\(B\\)|AnwSt|WpSt\\s?\\(R\\)|KVR|AR\\s?\\(Kart\\)|EnZR|StbSt\\s?\\(R\\)|WpSt\\s?\\(B\\)|KZA|AR\\s?\\(Enw\\)|AnwSt\\s?\\(R\\)|KRB|RiZ\\s?\\(B\\)|PatAnwSt\\s?\\(B\\)|EnVR|AnwZ|NotZ|EnZA|AR)\\s\\d+/\\d+)|((GSZ|LwZB|WpSt\\s?\\(B\\)|AnwZ|LwZR|KVZ|EnRB|PatAnwSt\\s?\\(B\\)|ARP|VGS|WpSt\\s?\\(R\\)|RiSt\\s?\\(B\\)|EnZA|KRB|AnwSt\\s?\\(R\\)|NotSt\\s?\\(Brfg\\)|EnVR|LwZA|ZB|AR\\s?\\(Vollz\\)|StB|ZR|AR\\s?\\(VS\\)|BJs|BLw|NotZ\\s?\\(Brfg\\)|RiZ\\s?\\(B\\)|PatAnwSt\\s?\\(R\\)|AK|RiZ|PatAnwZ|ARs|StbSt\\s?\\(R\\)|VRG|NotSt\\s?\\(B\\)|AR\\s?\\(Enw\\)|AR\\s?\\(VZ\\)|StE|KVR|AR\\s?\\(Ri\\)|AR|AnwSt|NotZ|StbSt\\s?\\(B\\)|StR|ZA|AnwZ\\s?\\(B\\)|EnZR|AR\\s?\\(Kart\\)|GSSt|AnwZ\\s?\\(P\\)|ZR\\s?\\(Ü\\)|AnwZ\\s?\\(Brfg\\)|KZB|BGns|KZR|RiSt|KZA|BAusl|AnwSt\\s?\\(B\\)|BGs|RiZ\\s?\\(R\\)|EnZB|RiSt\\s?\\(R\\)|ARZ|EnVZ)\\s\\d+/\\d+)|([I+|IV|V|VI|VII|VIII|IX|X|XI|XII|1-6]+[a-z]?\\s[A-Za-z()]{2,20}\\s\\d+/\\d\\d))";

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
        if(matcher.matches()) {// Aktenzeichen
            String encoded = query;
            try {
                encoded = URLEncoder.encode(query, StandardCharsets.UTF_8.toString());
            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            }
            searchResult = verdictRepository.findAllByFilenumberLike(encoded, PageRequest.of(page, 9));
        }
        else {
            System.out.println(query);
            System.out.println("matching Date");
            matcher = datePattern.matcher(query);
            if (matcher.matches()) { // Datum
                String[] date = query.split("\\.");
                String encoded = "";
                for (String s : date) {
                    encoded = s + encoded;
                }
                searchResult = verdictRepository.findAllByDate(encoded, PageRequest.of(page, 9));
            }
            else {
                searchResult = verdictRepository.findAllByTitleLike(query, PageRequest.of(page, 9)); // todo alle ergebnisse? Page request?
                if(page > searchResult.getTotalPages()) { //TODO Übergabe falls letzte Page nicht voll
                    searchResult = verdictRepository.findAllByTenorOrOffenseOrReasonsOrReasonfordecision(query, query, query, query, PageRequest.of(page, 9));
                }
                //second_list.removeAll(verdictByQuery);
                //verdictByQuery.addAll(second_list);
            }
        }
        return searchResult;
    }

    @GetMapping("/newest")
    @ResponseBody
    public Page<Verdict> newest(@RequestParam(required = false) Integer page) {
        if(page == null) {
            page = 0;
        }
        Page<Verdict> verdictByQuery =
                verdictRepository.findVerdictBy("",
                        PageRequest.of(page, 9, Sort.by(Sort.Direction.DESC, "date")));

        return verdictByQuery;
    }
//
//
//
//    public class date {
//        public static boolean isValidDate(String inDate) {
//            SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss:ms");
//            dateFormat.setLenient(false);
//            try {
//                dateFormat.parse(inDate.trim());
//            } catch (ParseException pe) {
//                return false;
//            }
//            return true;
//        }
}