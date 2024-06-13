select a.flavor from first_half as a
inner join ICECREAM_INFO as b
on a.flavor = b.flavor
where a.TOTAL_ORDER > 3000 and b.INGREDIENT_TYPE = 'fruit_based'
order by a.total_order desc;