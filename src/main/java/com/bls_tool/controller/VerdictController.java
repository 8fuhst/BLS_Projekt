package com.bls_tool.controller;

import com.bls_tool.model.type.Verdict;
import net.minidev.json.JSONArray;
import net.minidev.json.JSONObject;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/verdict")
public class VerdictController {

    @GetMapping
    public String verdict() {
        Verdict verdict1 = new Verdict();
        return verdict1.toJSON().toJSONString();
    }

}
