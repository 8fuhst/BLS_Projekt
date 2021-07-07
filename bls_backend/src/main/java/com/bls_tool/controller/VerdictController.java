package com.bls_tool.controller;

import com.bls_tool.model.type.Verdict;
import com.bls_tool.repositories.VerdictRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
public class VerdictController {
    @Autowired
    VerdictRepository verdictRepository;
    
    @GetMapping("/verdict")
    @ResponseBody
    public Verdict getSpecificVerdict(@RequestParam String documentnumber) {
        Verdict verdict = verdictRepository.findByDocumentnumber(documentnumber);
        return verdict;
    }

    @GetMapping("/verdictFN")
    @ResponseBody
    public Verdict getSpecificVerdictByFilenumber(@RequestParam String filenumber) {
        // todo only gebe exact matches zurück und bedenke aktenzeichen arrays
        // sowie mehrere urteile dverdict = verdictRepository.findByFilenumber(filenumber);ie dasselbe aktenzeichen haben
        Verdict verdict = verdictRepository.findByFilenumber(filenumber);
        return verdict;
    }
}
