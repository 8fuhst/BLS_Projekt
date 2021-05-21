package com.bls_tool.controller;

import com.bls_tool.repositories.VerdictRepository;
import com.bls_tool.model.type.Verdict;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
// @RequestMapping("/search")
public class SearchController {

    @Autowired
    private VerdictRepository verdictRepository;

    @GetMapping("/search")
    @ResponseBody
    public Page<Verdict> search(@RequestParam(required = false) String query) {
        // JSONArray result = new JSONArray();

        // TODO: Suche in DB
        Verdict verdict1 = new Verdict();
        JSONObject verdict_json = verdict1.toJsonMetadata();

        result.add(verdict_json);

        return verdictByQuery;
    }
}
