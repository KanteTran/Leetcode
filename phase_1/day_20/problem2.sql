-- Write your PostgreSQL query statement below 
-- https://leetcode.com/problems/investments-in-2016/description/?envType=study-plan-v2&envId=top-sql-50
with same_tiv as (
    select tiv_2016,
    count(*) over(partition by tiv_2015) as t1,
    count(*) over(partition by lat,lon) as t2
    from Insurance
)
select * from same_tiv