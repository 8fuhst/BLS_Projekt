package com.bls_tool.controller;

import com.bls_tool.model.type.VerdictNode;
import com.bls_tool.repositories.VerdictNodeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/verdictNode")
public class VerdictNodeController {
    @Autowired
    VerdictNodeRepository verdictNodeRepository;

    @GetMapping
    @ResponseBody
    public VerdictNode getSpecificVerdictNode(@RequestParam String filenumber) {
        return verdictNodeRepository.findByFilenumber(filenumber);
    }
}
