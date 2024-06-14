SELECT COUNT(id) AS count 
FROM ECOLI_DATA 
WHERE 
    (GENOTYPE & 2 = 0) 
    AND 
    ((GENOTYPE & 1) <> 0 OR (GENOTYPE & 4) <> 0);
