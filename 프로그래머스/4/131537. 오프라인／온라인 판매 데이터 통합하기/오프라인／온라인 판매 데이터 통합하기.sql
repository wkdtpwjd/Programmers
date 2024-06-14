select date_format(sales_date,'%Y-%m-%d') as sales_date,PRODUCT_ID,USER_ID,SALES_AMOUNT from 
online_sale
where substr(sales_date,1,7) = '2022-03'

union all 

select date_format(sales_date,'%Y-%m-%d') as sales_date,PRODUCT_ID,null as user_id ,SALES_AMOUNT from 
offline_sale
where substr(sales_date,1,7) = '2022-03'

order by sales_date,product_id,user_id;