# Write your MySQL query statement below
select 
  Department, 
  Employee, 
  Salary 
from 
  (
    select 
      e.name as Employee, 
      salary, 
      dense_rank() over (
        partition by departmentId 
        order by 
          salary desc
      ) as salary_rank, 
      d.name as Department 
    from 
      employee e 
      left join department d on e.departmentId = d.id
  ) ranked_employees 
where 
  salary_rank <= 3