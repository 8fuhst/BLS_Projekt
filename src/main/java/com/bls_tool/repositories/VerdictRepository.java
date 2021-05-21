package com.bls_tool.repositories;

import com.bls_tool.model.type.Verdict;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

public interface VerdictRepository extends ElasticsearchRepository<Verdict, String> {
    Page<Verdict> findVerdictBy(String query, Pageable pageable);

    // @Query
    // Page<Verdict> findVerdictByCustomQuery(String query);
}
