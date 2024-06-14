-- 코드를 작성해주세요
select count(id) as count from ECOLI_DATA 
where !(GENOTYPE&2) and (genotype&5)