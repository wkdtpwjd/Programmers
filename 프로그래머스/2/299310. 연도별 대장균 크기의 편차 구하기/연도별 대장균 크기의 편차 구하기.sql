-- 코드를 작성해주세요
with mytable as (select YEAR(DIFFERENTIATION_DATE) as mo,max(SIZE_OF_COLONY) as max_v from ecoli_data
group by YEAR(DIFFERENTIATION_DATE))

select YEAR(a.DIFFERENTIATION_DATE) as YEAR,
b.max_v-a.SIZE_OF_COLONY as YEAR_DEV,
a.ID 
from ECOLI_DATA a
join mytable b on YEAR(a.DIFFERENTIATION_DATE)= b.mo
order by YEAR,YEAR_DEV