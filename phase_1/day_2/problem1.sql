-- https://leetcode.com/problems/department-top-three-salaries/
select 
b.name as Department, a.name as Employee, salary
from (
    select *, 
    Dense_Rank() over (partition by departmentId order by salary desc) r
    from Employee 
) a
left join Department b on a.departmentId = b.id
where a.r <= 3 