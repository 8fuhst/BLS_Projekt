package com.bls_tool.controller;

import com.bls_tool.model.type.Verdict;
import com.bls_tool.repositories.VerdictRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/verdict")
public class VerdictController {

    @Autowired
    VerdictRepository verdictRepository;
    /*@GetMapping("/verdict")
    public JSONObject verdict() {
        Verdict verdict1 = new Verdict();
        return verdict1.toJSON();
    }

    @GetMapping("/verdict/" + docnr)
    public JSONObject getSpecificVerdict() {

    }
*/
    @GetMapping
    @ResponseBody
    public Verdict getSpecificVerdict(@RequestParam String documentnumber) {
        Verdict verdict = verdictRepository.findByDocumentnumber(documentnumber);
        return verdict;
    }
}
