package com.bls_tool.repositories;

import com.bls_tool.model.type.Verdict;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.elasticsearch.annotations.Query;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

public interface VerdictRepository extends ElasticsearchRepository<Verdict, String> {
    Page<Verdict> findVerdictBy(String query, Pageable pageable);

    // Page<Verdict> findVerdictBydocumentnumber(String query, Pageable pageable);

    Page<Verdict> findVerdictByDate(String query, Pageable pageable);

    //Verdict findVerdictByDocumentnumber(String query);

    @Query("{\"query\": {\"match\": [{\"documentnumber\": {\"query\": docnr}}]}}")
    Verdict findVerdictByDocumentnumber(String docnr);

    // @Query
    // Page<Verdict> findVerdictByCustomQuery(String query);
}
