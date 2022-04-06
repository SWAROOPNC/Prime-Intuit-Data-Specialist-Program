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
List all the employee whose name starts with ‘S’ 
List all the employee whose name is having letter ‘L’ as Second character 
List all the employees whose name is having at least 2 L’s in it 
List the employees whose name is having letter ‘E’ as the last but one character 
List all the employees whose name is having letter ‘R’ in the 3rd position 
List all the employees who are having exactly 5 characters in their jobs 
Display employees from whose name is having letter ‘_’ in it 
List the employees whose salary is between 2000 and 3000 
List all the employees whose commission is null 
List all the employees who don’t have a reporting manager 
List all the salesmen in dept 30 
List all the salesmen in dept number 30 and having salary greater than 1500 
List all the employees whose name starts with ‘s’ or ‘a’ 
List all the employees except those who are working in dept 10 & 20. 
List the employees whose name does not start with ‘S’ 
List all the employees who are having reporting managers in dept 10 
Display all the employee who are getting 2500 and excess salaries in dept 20. 
Display all the manager working in dept 20 and 30 
Display all the employee whose job is manager who don’t have  Reporting manager 
Display all the employee who are getting some commission with their designation is neither MANAGER not ANALYST 
Display all the employee whose earning salary not in the range 2500 and 5000 in dept 10 and 20 
 
Display all the manager whose annual sal is ending with zero 
Display all the employees who are CLERK or ANALAYST with salary greater than 1000. 
Display all the employee who are ‘SALESMAN’s having E as the last but one character in ename but salary having exactly 4 character 
Display all the employee who are joined after year 81 
Display all the employee who are joined in FEB 
List the employees who are not working as managers and clerks in dept 10 and 20 with a salary in the range of 1000 to 3000 
 List the employees whose salary not in the range of 1000 to 2000 in dept 10,20,30 except all salesmen 
 List the department names which are having letter ‘O’ in their locations as well as their department names 
 Display all the employees whose job has string ‘MAN’ in it. 
Select all the employees whose name start with P or V in departmetment 10 and 20 
Select all the salesman and clerks who are earcning salary in the range 1000 and 3000 except department 10 
Select all the employees whose are joined before 01-may-81 and after 01-may-80 
Select all the analyst whose name 3rd character start with 'S' and earning salary more than 2500 
Select all the salesman whose salary not between 2000 and 3000 in depaertment 30
