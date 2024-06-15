select a.id from ECOLI_DATA a
left join ECOLI_DATA b on a.parent_id = b.id
left join ECOLI_DATA c on b.parent_id = c.id
where c.parent_id is null and c.id is not null
order by id