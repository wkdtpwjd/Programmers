select a.REST_ID,a.REST_NAME,a.FOOD_TYPE,a.FAVORITES,a.ADDRESS,round(avg(b.REVIEW_SCORE),2) as SCORE
from REST_INFO as a inner join REST_REVIEW as b
on a.REST_ID = b.REST_ID
where a.address like '서울%'
group by rest_id
order by score desc,a.favorites desc
