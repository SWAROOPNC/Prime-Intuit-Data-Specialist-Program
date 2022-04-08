--2) Display job-wise highest salary only if the highest salary is more than 10000 
--excluding department 30.Sort the data based on highest salary in the ascending order.
SELECT
    job_id,
    MAX(salary)
FROM
    employees
WHERE department_id <>30
GROUP BY
    job_id
HAVING
    MAX(salary) > 10000
order by 2;
--ASSIGNMENT
--1) Display the department numbers along with the number of employees in it
select department_id,COUNT(employee_id) from employees group by department_id order by 1;
--2) Display the department numbers which are having more than 5 employees in them
select department_id,COUNT(employee_id) from employees group by department_id having COUNT(employee_id) >5 order by 1;
--4) Display the department numbers which are having more than 15000 as their 
--departmental total salary
select department_id,sum(salary) from employees group by department_id having sum(salary) >15000 order by 1;
--3) Display the maximum salary for each of the job excluding all the employees whose name ends with 's'
select job_id,max(salary) from employees where last_name not like '%s' group by job_id  order by 1;
--Display the minimum Salary for each of the job excluding all the 
--employees whose name ends with K
SELECT
    JOB_ID,MIN(salary)
FROM employees
WHERE last_name not like '%k'
GROUP BY JOB_ID
--HAVING
ORDER BY 1 ;
--Display the max salary for each of the job excluding all the 
--employee whose having commission.
SELECT
    JOB_ID,MAX(salary)
FROM employees
WHERE commission_pct is null
GROUP BY JOB_ID
--HAVING
ORDER BY 1 ;