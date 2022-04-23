--1) Write a query to display the employee name and hiredate for all employees in the same department  as fname Shelley but Exclude Shelley.
SELECT
    first_name,
    last_name,
    hire_date
FROM
    employees
WHERE
 first_name != 'Shelley'
and    department_id in (
        SELECT
            department_id
        FROM
            employees
        WHERE
            first_name = 'Shelley'
    );
--2) Create a query to display the employee number and name for all employees who earn more than the average salary.  Sort the results in descending order of salary.
SELECT
    employee_id,
    first_name,
    last_name,
    salary
FROM
    employees
WHERE
    salary > (
        SELECT
            AVG(salary)
        FROM
            employees
    )
ORDER BY
    4;
-- 3) Write a query to display the employee number and name for all employees who work in a department with any  employee whose name contains a T.
select employee_id, first_name, last_name
from employees where department_id in 
(select department_id
from employees where first_name like '%T%'or first_name like '%T%' );

--4) Display the employee name, department number, and job title for all employees whose department location is London.
select first_name, last_name ,department_id,job_id
from employees where department_id in 
(select department_id FROM departments
               WHERE location_id = (select location_id from locations where city='London'));
--5) Display the employee name and salary of all employees who report to King.
select * from employees where manager_id in ( select employee_id  from employees where last_name = 'King')  order by 1;
--6) Display the department number, name,, and job for all employees in the Sales department.
select e.department_id ,d.department_name, e.job_id   from employees e, departments d where e.department_id = d.department_id 
and d.department_name = 'Sales'  ;
--or
select e.department_id ,d.department_name, e.job_id   from employees e, departments d where e.department_id = d.department_id 
and d.department_name = 'Sales' group by  e.department_id ,d.department_name, e.job_id  ;
--7) Display the employee number, name, and salary for all employees who earn more than the average salary and who  work in a department with any employee with a  T  in their name.
SELECT
    employee_id,
    first_name,
    last_name,
    salary
FROM
    employees
WHERE
    salary > (
        SELECT
            AVG(salary)
        FROM
            employees
    )
    and 
    department_id in ( select department_id from employees where first_name like '%t%' or first_name like '%T%' or last_name like '%t%' or last_name like '%T%' )
   order by 1;

--SUBQUERIES EXCERCISES:
select * from employees where  (select * from employees);
-- List the department names that are having no employees at all;

SELECT
    distinct department_id
FROM
    departments
WHERE
    department_id not in (
        SELECT
            distinct department_id
        FROM
            employees
        where employees.department_id=departments.department_id
    );
/* 1. Write a query to display the name (first name and last name) for those employees who gets more 
salary than the employee whose ID is 163. */
select first_name || ' ' || last_name , salary from employees where salary > (select salary from  employees where employee_id = 163) order by 2 desc ;
/* 2. Write a query to display the name (first name and last name), salary, department id, job id for those 
employees who works in the same designation as the employee works whose id is 169. */
select first_name || ' ' || last_name , salary, department_id, job_id from employees where job_id = (select job_id from  employees where employee_id = 163) order by 2 desc ;
/* 3. Write a query to display the name (first name and last name), salary, department id for those employees 
who earn such amount of salary which is the smallest salary of any of the departments. */
select first_name || ' ' || last_name , salary, department_id from employees where salary in (select min(salary) from  employees group by department_id) order by 2 desc ;
--or
select first_name || ' ' || last_name , salary, department_id from employees where salary in (select min(salary) from  employees ) order by 2 desc ;
/* 4. Write a query to display the employee id, employee name (first name and last name) for all employees who 
earn more than the average salary. */
select employee_id, first_name, last_name from employees where salary > (select avg(salary) from  employees) order by 2 desc ;
/* 5. Write a query to display the employee name (first name and last name), employee id and salary of all employees who report to Payam. */
select first_name || ' ' || last_name,  employee_id, salary  from employees where manager_id  = (select employee_id from  employees where first_name = 'Payam' ) order by 2 desc ;
/* 6. Write a query to display the department number, name (first name and last name), job_id and department name for all employees in the 
Finance department. */
/* 6. Write a query to display the department number, name (first name and last name), job_id and department name for all employees in the Finance department. */

select 
e.department_id, 
e.first_name ||  ' ' ||  e.last_name , 
e.job_id , d.department_name 
from employees e , departments d 
where e.department_id = d.department_id 
and  e.department_id in (select department_id from  departments  where department_name Like '%Finance%' ) order by 1 ;

/* 7. Write a query to display all the information of an employee whose salary and reporting person id is 3000 and 121, respectively. */
/* 7. Write a query to display all the information of an employee whose salary and reporting person id is 3000 and 121, respectively. */

select * from employees where salary = 3000 and manager_id = 121;
/* 8. Display all the information of an employee whose id is any of the number 134, 159 and 183. */
/* 8. Display all the information of an employee whose id is any of the number 134, 159 and 183. */

select * from employees where employee_id = 134 or employee_id = 159 or employee_id = 183;
/* 9. Write a query to display all the information of the employees whose salary is within the range 1000 and 3000. */
/* 9. Write a query to display all the information of the employees whose salary is within the range 1000 and 3000. */

select * from employees where salary between 1000 and 3000;
/* 10. Write a query to display all the information of the employees whose salary is within the range of smallest 
salary and 2500. */
/* 10. Write a query to display all the information of the employees whose salary is within the range of smallest salary and 2500. */

select * from employees where salary between (select min(salary) from employees ) and 3000;
/* 11. Write a query to display all the information of the employees who does not work in those departments 
where some employees works whose manager id within the range 100 and 200. */

select * from employees where department_id not in 
( select department_id from employees where manager_id between 100 and 200 );
/* 12. Write a query to display all the information for those employees whose id is any id who earn the second highest salary. */
--using subquery

select * from employees where salary = 
( select max(salary) from employees 
where salary < (select max(salary) from employees ));
-- using correlated sub query
SELECT * 
FROM
    employees e1
WHERE
    ( 2 - 1 ) = (
        SELECT
            COUNT(DISTINCT salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );
/* 14. Write a query to display the employee number and name (first name and last name) for all employees 
who work in a department with any employee whose name contains a T. */
SELECT
    employee_id ,
    first_name ,
    last_name 
FROM
    employees
WHERE 
    department_id in ( select department_id from employees where first_name like '%t%' or first_name like '%T%' or last_name like '%t%' or last_name like '%T%' )
    order by 1;
/* 16. Display the employee name (first name and last name), employee id, and job title for all employees whose 
department location is Toronto. */
select first_name, last_name ,employee_id, job_id
from employees
where department_id in 
(select department_id FROM departments
               WHERE location_id = ( select location_id from locations where city = 'Toronto'));
/* 17. Write a query to display the employee number, name (first name and last name) and job title for all 
employees whose salary is smaller than any salary of those employees whose job title is MK_MAN. */
select * from employees where salary < 
( select salary from employees 
where job_id = 'MK_MAN');
/* 18. Write a query to display the employee number, name (first name and last name) and job title for all 
employees whose salary is smaller than any salary of those employees whose job title is MK_MAN. Exclude Job 
title MK_MAN. */
select * from employees where salary < 
( select salary from employees 
where job_id = 'MK_MAN') and job_id != 'MK_MAN' ;

/* 19. Write a query to display the employee number, name (first name and last name) and job title for all employees whose salary is more than any salary of those employees whose job title is PU_MAN. Exclude job title PU_MAN. */
select * from employees where salary > 
( select salary from employees 
where job_id = 'PU_MAN') and job_id != 'PU_MAN' ;
/* 20. Write a query to display the employee number, name (first name and last name) and job title for all employees whose salary is more than any average salary of any department. */
select employee_id, first_name, last_name,job_id from employees where salary > (select min(avg(salary)) from  employees group by department_id) order by 2 desc ;