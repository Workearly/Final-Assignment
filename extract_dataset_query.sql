select * from finance_liquor_sales;

select count(*) from finance_liquor_sales; 
-- 196

select * from finance_liquor_sales a
where 1=1
and a.date >= '2016-01-01' 
and a.date <= '2019-12-31' 
order by a.date;

-- SELECT COLUMN_NAME,DATA_TYPE
--  from INFORMATION_SCHEMA. COLUMNS where table_schema = 'liquorsales' and table_name = 'finance_liquor_sales'

-- select * from finance_liquor_sales