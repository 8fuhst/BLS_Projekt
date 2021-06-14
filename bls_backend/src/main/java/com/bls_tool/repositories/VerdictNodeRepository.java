package com.bls_tool.repositories;

import com.bls_tool.model.type.VerdictNode;
import com.bls_tool.model.type.VerdictNode;
import org.elasticsearch.action.index.IndexRequest;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import java.util.List;

public interface VerdictNodeRepository extends ElasticsearchRepository<VerdictNode, String> {

    VerdictNode findByFilenumber(String filenumber);
}
