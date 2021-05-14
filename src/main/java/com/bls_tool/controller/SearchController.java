package com.bls_tool.controller;

import com.bls_tool.model.type.Verdict;
import net.minidev.json.JSONArray;
import net.minidev.json.JSONObject;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
// @RequestMapping("/search")
public class SearchController {

    @GetMapping("/search")
    @ResponseBody
    public String search(@RequestParam(required = false) String query) {
        JSONArray result = new JSONArray();

        // TODO: Suche in DB
        Verdict verdict1 = new Verdict();
        JSONObject verdict_json = verdict1.toJsonMetadata();

        result.add(verdict_json);

        return result.toJSONString();
    }
}
