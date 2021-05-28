package com.bls_tool.controller;

import com.bls_tool.model.type.Verdict;
import net.minidev.json.JSONObject;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/verdict")
public class VerdictController {

    @GetMapping
    public JSONObject verdict() {
        Verdict verdict1 = new Verdict();
        return verdict1.toJSON();
    }

}
