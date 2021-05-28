package com.bls_tool.controller;

import com.bls_tool.repositories.VerdictRepository;
import com.bls_tool.model.type.Verdict;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
// @RequestMapping("/search")
public class SearchController {

    @Autowired
    private VerdictRepository verdictRepository;

    @GetMapping("/search")
    @ResponseBody
    public Page<Verdict> search(@RequestParam(required = false) String query) {
        // JSONArray result = new JSONArray();

        Page<Verdict> verdictByQuery
                = verdictRepository.findVerdictBy(query, PageRequest.of(0, 10)); // todo alle ergebnisse? Page request?

        // Verdict verdict1 = new Verdict();
        // JSONObject verdict_json = verdict1.toJsonMetadata();
        // result.add(verdict_json);

        return verdictByQuery;
    }

    @GetMapping("/newest")
    @ResponseBody
    public Page<Verdict> newest() {
        // JSONArray result = new JSONArray();

        Page<Verdict> verdictByQuery =
                verdictRepository.findVerdictBy("",
                        PageRequest.of(0, 10, Sort.by(Sort.Direction.DESC, "date")));

        return verdictByQuery;
    }
}
