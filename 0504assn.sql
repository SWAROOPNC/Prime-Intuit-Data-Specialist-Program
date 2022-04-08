--List all the employees in dept 20. 
select * from employees where department_id = 20;
--List the employee earning more than Rs 2500;
select * from employees where salary > 2500;
--Display all the salesmen 
select * from employees where job_id = 'SA_MAN';
--List the employees in department 10 and 20. 
select * from employees where department_id in (10,20);
--List all the clerks and analyst. 
SELECT DISTINCT
    ( job_id )
FROM
    employees;
-- no analyst jobid found
SELECT
    *
FROM
    employees
WHERE
    job_id LIKE '%clerk';
--List all the employee whose name starts with ‘S’ 
SELECT
    *
FROM
    employees
WHERE
    first_name LIKE 'S%';
--List all the employee whose name is having letter ‘L’ as Second character 
SELECT
    *
FROM
    employees
WHERE
    first_name LIKE '_l%';
--List all the employees whose name is having at least 2 L’s in it 
SELECT
    *
FROM
    employees
WHERE
    first_name LIKE '%l%l%' or first_name LIKE 'L%l%';
--List the employees whose name is having letter ‘E’ as the last but one character 
SELECT
    *
FROM
    employees
WHERE
    first_name LIKE '%e_';
--List all the employees whose name is having letter ‘R’ in the 3rd position 
SELECT
    *
FROM
    employees
WHERE
    first_name LIKE '__r%';
--List all the employees who are having exactly 5 characters in their jobs 
SELECT
    *
FROM
    employees
WHERE
    first_name LIKE '%l%l%' or first_name LIKE '_____';
--Display employees from whose name is having letter ‘_’ in it 
SELECT
    *
FROM
    employees
WHERE
first_name LIKE '%_%' ;
--List the employees whose salary is between 2000 and 3000 
SELECT
    *
FROM
    employees
WHERE
    salary BETWEEN 2000 AND 3000 ;
--List all the employees whose commission is null 
select *from employees where commission_pct is null;
--List all the employees who don’t have a reporting manager 
select *from employees where manager_id is null;
--List all the salesmen in dept 30 
select *from employees where job_id = 'SA_MAN' and department_id = 30;
--List all the salesmen in dept number 30 and having salary greater than 1500 
select *from employees where job_id = 'SA_MAN' and department_id = 30 and salary>1500;
--List all the employees whose name starts with ‘s’ or ‘a’ 
select *from employees where first_name like 'S%' or first_name like 'A%' ;
--List all the employees except those who are working in dept 10 & 20. 
select *from employees where department_id NOT IN (10,20);
--List the employees whose name does not start with ‘S’ 
select *from employees where first_name NOT like 'S%'  ;
--List all the employees who are having reporting managers in dept 10 
select *from employees where manager_id is not null and department_id=30 ;
--Display all the employee who are getting 2500 and excess salaries in dept 20. 
select *from employees where salary>2500 and department_id=20 ;
--Display all the manager working in dept 20 and 30 
select *from employees where job_id LIKE '%MGR' and department_id in (20,30) ;
--Display all the employee whose job is manager who don’t have  Reporting manager 
select *from employees where job_id LIKE '%MGR' and manager_id is null ;
--Display all the employee who are getting some commission with their designation is neither MANAGER not ANALYST 
-- no analyst
select *from employees where commission_pct is not null and job_id not like '%MGR';;
--Display all the employee whose earning salary not in the range 2500 and 5000 in dept 10 and 20 
 select *from employees where salary not between 2500 and 5000 and department_id in (10,20) ;
--Display all the manager whose annual sal is ending with zero 
 select employee_id, first_name, last_name, salary , (12*salary) as "ANNUAL_SALARY" from employees where job_id like '%MGR' and 12*salary like '%0'   ;
  select employee_id, first_name, last_name, salary , (12*salary) as "ANNUAL_SALARY" from employees where job_id like '%MGR' and 5 like '%0'   ;
--Display all the employees who are CLERK or ANALAYST with salary greater than 1000. 
-- no analysts
  select * from employees where job_id like '%CLERK' and salary>1000   ;
--Display all the employee who are ‘SALESMAN’s having E as the last but one character in ename but salary having exactly 4 character 
  select * from employees where job_id = 'SA_MAN' and last_name like '%e_' and salary like '____'   ;
--Display all the employee who are joined after year 81 
  select * from employees where hire_date  > '01-01-81';  --not work
--Display all the employee who are joined in FEB 
  select * from employees where hire_date  like '__-02-__'; --works 
  select * from employees where month hire_date is 02;  --not work
--List the employees who are not working as managers and clerks in dept 10 and 20 with a salary in the range of 1000 to 3000 
  select * from employees where job_id not  like '%MGR' and  job_id not  like '%CLERK' and department_id in (10,20)  and salary between 1000 and 3000;
 --List the employees whose salary not in the range of 1000 to 2000 in dept 10,20,30 except all salesmen 
   select * from employees where job_id <> 'SA_MAN'  and department_id in (10,20,30)  and salary not between 1000 and 2000;
 --List the department names which are having letter ‘O’ in their locations as well as their department names 
 --covered in previous 0404sql assignment , similar to that
 SELECT
    d.department_name,
    l.city
FROM
    departments  d,
    locations    l
WHERE
        d.location_id = l.location_id
    AND l.city LIKE '%o%' or l.city LIKE '%O%' 
    and d.department_name LIKE '%O%' or  d.department_name LIKE '%o%' ;
 --Display all the employees whose job has string ‘MAN’ in it. 
   select * from employees where job_id  like '%MAN%' ;
--Select all the employees whose name start with P or V in departmetment 10 and 20 
   select * from employees where first_name  like 'P%' or first_name  like 'V%'  and department_id in (10,20);
--Select all the salesman and clerks who are earcning salary in the range 1000 and 3000 except department 10 
   select * from employees where job_id = 'SA_MAN' and job_id like '%CLERK' and salary BETWEEN 1000 AND 3000  and department_id <> 10;
--Select all the employees whose are joined before 01-may-81 and after 01-may-80 
   select * from employees where hire_date BETWEEN '01-05-80' AND '01-05-81';
--Select all the analyst whose name 3rd character start with 'S' and earning salary more than 2500 
-- no analysts
--Select all the salesman whose salary not between 2000 and 3000 in depaertment 30
   select * from employees where job_id = 'SA_MAN' and salary not BETWEEN 2000 AND 3000 and department_id = 30;