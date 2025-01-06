# Write your MySQL query statement below
With InsuranceCounts as (
    select *,
    count(*) over (partition by tiv_2015) as tiv2015_cnt,
    count(*) over (partition by lat, lon) as city_cnt
    from Insurance
)

select round(sum(tiv_2016), 2) as tiv_2016 from InsuranceCounts where tiv2015_cnt > 1 and city_cnt =1;