-- 코드를 작성해주세요                      
with ranktable as (select id,size_of_colony,ntile(4) over (order by size_of_colony desc) as ranking from ecoli_data)

select id,case
when ranking = 1 then 'CRITICAL'
when ranking = 2 then 'HIGH'
when ranking = 3 then 'MEDIUM'
when ranking = 4 then 'LOW'
end
as COLONY_NAME
from ranktable
order by id