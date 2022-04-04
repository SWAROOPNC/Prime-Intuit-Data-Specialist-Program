--1Display all the employees whose name start with P
DESC employees;

SELECT
    *
FROM
    employees
WHERE
    first_name LIKE 'P%';
--2Display all the analyst and clerks  in department 10 and 20\

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
    job_id LIKE '%clerk'
    AND department_id IN ( 10, 20 );
--3 List all the department names which are having blank space in their location and having Dname with at least two EE's
SELECT
    d.department_name,
    l.city
FROM
    departments  d,
    locations    l
WHERE
        d.location_id = l.location_id
    AND l.city LIKE '% %' 
    and d.department_name LIKE '%e%e%' or  d.department_name LIKE '%E%E%' or d.department_name LIKE '%e%E%' or d.department_name LIKE '%E%e%' ;
--4 Display all the employees who are having at least two AA's in their job description and salary . the range 1200 to 2800 . dept 10,20,30.
-- job decription not there or so used job id
SELECT
    *
FROM
    employees
WHERE
    salary BETWEEN 1200 AND 2800
    AND department_id IN ( 10, 20, 30 ) 
    and job_id like '%A%A%' ;
--5 Display all the employees who aren't having any reporting manager with number ending with '8' and 
--not working as 'MANAGER' or 'SALESMAN' in dept 30. , , like mgr or sa_man
SELECT
    *
FROM
    employees
WHERE
    manager_id NOT LIKE '%8'
    AND job_id NOT IN ( 'SA_MAN' )
    AND job_id NOT LIKE '%MGR'
    and department_id = 30;
--6-List all the employees who are not getting any commission with their designation neither 'CLERK' nor 'MANAGER' and joined in the year 81 and getting salary more than 1500.
SELECT
    *
FROM
    employees
WHERE
    job_id NOT LIKE '%MGR'
    AND job_id NOT LIKE '%CLERK'
    AND commission_pct IS NULL
    AND salary>1500
    and hire_date LIKE '__-__-81';
--YEAR()
--7 List all the employees who. name is having at least FIVE characters and joined in the year 80 or 81 and having a reporting manager with salary in the range 800 to 2000
--. dept 30 or 40. List all the employees where report.g manager ED is ending with the number 8?
desc employees;
select * from employees where first_name like'_____%'
and hire_date LIKE '__-__-81' or hire_date LIKE '__-__-80'
and manager_id is not null
and salary between 800 and 2000
and department_id in (30,40);
--8 List all the employ.s whrere reporting manager id ends with number 8
select * from employees where manager_id like '%8';
--9  LIST ALL EMPLOYEES WHOSE JOB IS SAlesman and salary ranges between 1500 and 3000
select * from employees where job_id = 'SA_MAN'
and salary between 1500 and 3000;
--10  List all the employees who's salary .. the range of 1000 to 2000 . dept 10,20,30 except all clerks?
select * from employees where salary between 1000 and 2000 and
department_id in (10,20,30)
and job_id not like '%CLERK';