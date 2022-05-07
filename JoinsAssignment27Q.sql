--1.   Write a query in SQL to display the first name, last name, department number, and department name for each employee. 
select e.first_name, e.last_name,e.department_id , d.department_name
from employees e
inner join departments d
on e.department_id = d.department_id;
--2.   Write a query in SQL to display the first and last name, department, city, and state province for each employee. 
select * from employees; --fname , lname , depId
select * from departments; --depID , depname , loc id 
select * from locations; --location id city state prov
select e.first_name,e.last_name,e.department_id,d.department_name,d.location_id,l.city,l.state_province from employees e ,departments d , locations l
where e.department_id = d.department_id
and d.location_id = l.location_id;
--alternate way same as normal style
select e.first_name,e.last_name,e.department_id,d.department_name,d.location_id,l.city,l.state_province 
from employees e 
inner join departments d on e.department_id = d.department_id
inner join locations l on d.location_id = l.location_id;      
                                                                                                      
--3.   Write a query in SQL to display the first name, last name, salary, and job grade for all employees. 

select first_name, last_name,salary, job_id from employees;

--4.   Write a query in SQL to display the first name, last name, department number and department name, for all employees for departments 80 or 40.
select e.first_name, e.last_name, e.salary, e.department_id,d.department_name 
from employees e , departments d 
where e.department_id= d.department_id 
and e.department_id in (80,40); ---35 rows
--ansi style
select e.first_name, e.last_name, e.salary, e.department_id,d.department_name 
from employees e inner join departments d 
on e.department_id= d.department_id 
where e.department_id in (80,40); ---35 rows
--5.   Write a query in SQL to display those employees who contain a letter z to their first name and also display their last name, department, city, and state  province.
select * from departments;--depid , dep name , manag id , loc id 
select * from locations; --location_id ., city,state_province , country_id
select e.first_name, e.last_name, e.department_id, d.department_name , l.city , l.state_province
from employees e , departments d , locations l
where e.department_id= d.department_id 
and d.location_id = l.location_id; --106 rows
--ansi style
SELECT
    e.first_name,
    e.last_name,
    e.department_id,
    d.department_name,
    l.city,
    l.state_province
FROM
         employees e
    INNER JOIN departments  d ON e.department_id = d.department_id
    INNER JOIN locations    l ON d.location_id = l.location_id; --106 rows

--6.   Write a query in SQL to display all departments including those where does not have any employee.
select * from departments;
--7.   Write a query in SQL to display the first and last name and salary for those employees who earn less than the employee earn whose number is 182.
select first_name, last_name, salary from employees where salary < ( select salary from employees where employee_id = 182 ) ;
--8.   Write a query in SQL to display the first name of all employees including the first name of their manager.
select * from employees;
select e1.first_name emp_name , e2.first_name manag_name from employees e1 , employees e2 where e1.manager_id = e2.employee_id  ;
--9.   Write a query in SQL to display the department name, city, and state province for each department.
select department_id, department_name, location_id from departments;
select location_id,city,state_province from locations;
select d.department_name, d.location_id, l.city, l.state_province 
from departments d
inner join locations l
on d.location_id = l.location_id;
--10. Write a query in SQL to display the first name, last name, department number and name, for all employees who have or have not any department.
SELECT
    e.first_name , e.last_name , e.department_id , d.department_name
FROM employees e inner join departments d
on e.department_id = d.department_id;
--12. Write a query in SQL to display the first name, last name, and department number for those employees who works in the same department as the     
--- employee who holds the last name as Taylor. 
select first_name, last_name , department_id from employees where department_id in
( select department_id from employees where last_name = 'Taylor');
--13. Write a query in SQL to display the job title, department name, full name (first and last name ) of employee, 
--and starting date for all the jobs which started on or after 1st January, 1993 and ending with on or before 31 August, 1997 

select j.job_title,d.department_name ,e.first_name || ' ' || e.last_name full_name  
from employees e , 
jobs j  , 
departments d
where e.job_id = j.job_id 
and e.department_id = d.department_id
and hire_date >= '07-06-02' 
and hire_date <='15-05-03' ;
--ansi style
select j.job_title,d.department_name ,e.first_name || ' ' || e.last_name full_name  
from employees e 
inner join 
jobs j  on e.job_id = j.job_id 
inner join departments d
on e.department_id = d.department_id
where hire_date >= '07-06-02' 
and hire_date <='15-05-03' ;
--14. Write a query in SQL to display job title, full name (first and last name ) of employee, and the difference between maximum salary for the job and salary of the employee. 


SELECT
    job_title,
    first_name || ' ' || last_name AS employee_name,
    max_salary - salary    AS salary_difference
FROM
         employees
    NATURAL JOIN jobs;

--15. Write a query in SQL to display the name of the department, average salary and number of employees working in that department who got commission.
select d.department_name , AVG(e.salary),COUNT(e.EMPLOYEE_ID) from employees E , departments d
where e.department_id = d.department_id 
and e.commission_pct is not null
group by d.department_name;
--ansi
select d.department_name , AVG(e.salary),COUNT(e.EMPLOYEE_ID) from employees E inner join departments d
on e.department_id = d.department_id 
where e.commission_pct is not null
group by d.department_name;
--16. Write a query in SQL to display the full name (first and last name ) of employees, job title and
--the salary differences to their own job for those employees who is working in the department ID 80.

/* 16. Write a query in SQL to display the full name (first and last name ) of employees, job title and 
the salary differences to their own job for those employees who is working in the department ID 80. */

SELECT e.first_name,  e.last_name ,
       j.job_title,
       (j.max_salary - e.salary) as salary_diff
  FROM employees e
  INNER JOIN jobs j
    ON e.job_id = j.job_id
      WHERE e.department_id = 80;
--- github answers link
--https://github.com/tweichle/w3resource-SQL-Exercises/blob/master/SQL%20Exercises%20-%20JOINS%20on%20HR%20Database.sql
--17. Write a query in SQL to display the name of the country, city, and the departments which are running there.
SELECT c.country_name,
       l.city,
       d.department_name
  FROM countries c
  INNER JOIN locations l
    ON c.country_id = l.country_id
  INNER JOIN departments d
    ON l.location_id = d.location_id;
--18. Write a query in SQL to display department name and the full name (first and last name) of the manager.
SELECT d.department_name,
     e.first_name, e.last_name
  FROM departments d
  INNER JOIN employees e
    ON d.manager_id = e.employee_id;
--19. Write a query in SQL to display job title and average salary of employees.
SELECT j.job_title,
       AVG(e.salary)
  FROM employees e
  INNER JOIN jobs j
    ON e.job_id = j.job_id
  GROUP BY j.job_title;

--20. Write a query in SQL to display the details of jobs which was done by any of the employees who is presently earning a salary on and above 12000.
SELECT jh.*
  FROM employees e
  INNER JOIN job_history jh
    ON e.employee_id = jh.employee_id
      WHERE salary >= 12000.00;
--21. Write a query in SQL to display the country name, city, and number of those departments where at least 2 employees are working.
SELECT c.country_name,
       l.city,
       COUNT(d.department_id)
  FROM countries c
  INNER JOIN locations l
    ON c.country_id = l.country_id
  INNER JOIN departments d
     ON l.location_id = d.location_id
  WHERE d.department_id IN (SELECT e.department_id
                              FROM employees e
                              GROUP BY e.department_id 
                              HAVING COUNT(e.employee_id) >= 2)
  GROUP BY c.country_name, l.city;
--22. Write a query in SQL to display the department name, full name (first and last name) of manager, and their city. 
SELECT d.department_name,
     e.first_name, e.last_name,
       l.city
  FROM employees e
  INNER JOIN departments d
    ON e.employee_id = d.manager_id
  INNER JOIN locations l
    ON d.location_id = l.location_id;
--23. Write a query in SQL to display the employee ID, job name, number of days worked in for all those jobs in department 80. 
SELECT jh.employee_id,
       j.job_title,
       (jh.end_date - jh.start_date) AS num_days
  FROM jobs j
  INNER JOIN job_history jh
    ON j.job_id = jh.job_id
      WHERE jh.department_id = 80;
--24. Write a query in SQL to display the full name (first and last name), and salary of those employees who working in any department located in London.
SELECT e.first_name,  e.last_name ,
       e.salary
  FROM employees e
  INNER JOIN departments d
    ON e.department_id = d.department_id
  INNER JOIN locations l
    ON d.location_id = l.location_id
      WHERE l.city = 'London';
--25. Write a query in SQL to display full name(first and last name), job title, starting and ending date of last jobs
--for those employees with worked without a commission percentage.
SELECT e.first_name, e.last_name ,
       j.job_title,
       jh.*
  FROM employees e
  INNER JOIN (SELECT MAX(start_date) AS starting_date,
                     MAX(end_date) AS ending_date,
                     employee_id
                FROM job_history
                GROUP BY employee_id) jh
    ON e.employee_id = jh.employee_id
  INNER JOIN jobs j
    ON e.job_id = j.job_id
      WHERE e.commission_pct = 0;
--26. Write a query in SQL to display the department name and number of employees in each of the department.
SELECT d.department_name,
       COUNT(e.employee_id) AS num_employees
  FROM departments d
  INNER JOIN employees e
    ON d.department_id = e.department_id
  GROUP BY d.department_name;
--27. Write a query in SQL to display the full name (first and last name) of employee with ID and name of the country presently where (s)he is working. 
SELECT 
        e.first_name, e.last_name,
       e.employee_id,
       c.country_name
  FROM employees e
  INNER JOIN departments d
    ON e.department_id = d.department_id
  INNER JOIN locations l
    ON d.location_id = l.location_id
  INNER JOIN countries c
    ON l.country_id = c.country_id ;