
/*employees in dept 1 & 20*/
SELECT
    *
FROM tab;
desc employees;
SELECT
    *
FROM employees;
--ALL CLERKS & ANAL
SELECT employee_id, first_name,last_name,salary,department_id FROM employees ; 
select * FROM employees where salary=24000;
SELECT * FROM EMPLOYEES WHERE DEPARTMENT_ID IN 10;
-- equal to pass single value
-- like to pass multiple values
SELECT * FROM EMPLOYEES WHERE DEPARTMENT_ID IN 10;
--employees in dept 10 , 20
SELECT * FROM EMPLOYEES WHERE DEPARTMENT_ID IN (10,20);
SELECT * FROM EMPLOYEES WHERE DEPARTMENT_ID = 10 or DEPARTMENT_ID = 20;
--above 2 queries are same
--list all it prohrammers ad vp
SELECT
    DISTINCT job_id
FROM employees;
select * FROM employees where job_id = 'AD_VP' OR job_id = 'IT_PROG';
select * FROM employees where job_id IN ('AD_VP','IT_PROG');
-- max 1000 values can pass in IN operator
--DONT GIVE "" DOUBLE QUOTES , OBSERVE _ IN ids
/* _ wild card one character  % _e% */
select * from employees where job_id LIKE 'AD%';
--gives job id ad_asst . ad pres .,ad vp
-- wmployees where fname starts with s
SELECT * FROM employees where first_name like 'S%';
-- %_ must then use like _for one char
--'case sensitive', single quote % n characters
--employees  first name hav L has second char
SELECT
    DISTINCT first_name
FROM employees;
SELECT
    *
FROM employees WHERE first_name LIKE '_l%';
-- last second letter
select * FROM employees WHERE first_name LIKE '%l_';
-- for 3rd letter l

-- single quote
SELECT
    *
FROM employees WHERE first_name LIKE '__l%';
--atleast 2 lls
select * FROM employees WHERE first_name LIKE '%ll%';
-- employees , first name having letter e last but 1
select * FROM employees WHERE first_name LIKE '%e_';
select * FROM employees WHERE first_name LIKE '%E_'; --no recods
--3rd letter r
select * FROM employees WHERE first_name LIKE '__r%'; --2 __
--fname 5 letters
select * FROM employees WHERE first_name LIKE '_____';
---at leat 5 char , 5_1% , not 4_
select * FROM employees WHERE first_name LIKE '_____%';
-- between
SELECT
    *
FROM employees where salary between 10000 and 20000;
--is operator to compare nulls
--list emp whose commission is null
SELECT
    *
FROM employees where commission_pct is NULL;
-- who dont have rep manager
SELECT
    *
FROM employees where manager_id is NULL;
--logical operators

--all salesman in dept 80
--dataset =collection of relative data 
SELECT
    *
FROM employees where job_id='SA_MAN' AND department_id=80;
SELECT
    *
FROM employees WHERE job_id LIKE 'SA_%';
--SALESMAN DEPT 30 SALARY >1500
SELECT
    *
FROM employees where job_id='SA_MAN'AND department_id=30 AND salary>1500;
SELECT
    *
FROM
    employees
WHERE
        job_id = 'SA_MAN'
    AND department_id = 80
    AND salary > 1500;
--EMP FNAME 's or a
SELECT
    *
FROM
    employees
WHERE
    first_name like 'S%'
    OR first_name like 'A%'
    ORDER BY first_name;
-- use like not =
-- s or a not works
SELECT
    *
FROM
    employees
WHERE
    first_name like 'S%'
    AND first_name like 'A%';
--EMPTY LIST , FOR AND
--NOT IN
--ECXEPT IN DEP 10 AND 20
SELECT
    *
FROM
    employees
WHERE
    department_id NOT IN (10,20);
-- FIRST NAME NOT WITH S
SELECT
    *
FROM
    employees
WHERE
    first_name NOT LIKE 'S%'
    ORDER BY first_name;
--HAVE REP MANAGER IN DEPT 90
SELECT
    *
FROM
    employees
WHERE
    manager_id IS NOT NULL 
    AND department_id=90;
--NOT WORKING AS MANAGERS AND CLERK IN DEP 10 AND 20 , SALARY 1000-9000
SELECT DISTINCT JOB_ID FROM employees;
SELECT
    *
FROM
    employees
WHERE
    SALARY BETWEEN 1000 AND 9000
    AND department_id IN (10,20)
    AND job_id NOT LIKE '%MGR'
    AND job_id NOT LIKE '%CLERK' ;
--SALARY NOT IN RANGE 1000-2000 IN DEP 10,20,30 , EXCPET ALL SALESMAN
SELECT* FROM employees WHERE
    department_id IN (10,20,30)
    AND JOB_ID != 'SA_MAN'
    AND salary NOT BETWEEN 1000 AND 2000 ;
-- <> != NOT EQUAL TO OR NOT IN('sa_MAN')
SELECT* FROM departments ;
SELECT * FROM EMPLOYEES
WHERE
    first_name LIKE '%o%' or first_name LIKE '%O%' 
    and last_name LIKE '%o%'or last_name LIKE'%O%'
    ORDER BY last_name;
SELECT
    *
FROM employees order by salary;
SELECT
    *
FROM employees order by 8;
--aove 2 are same
-- 8 column
-- desc orfrt 
select * FROM employees order by salary asc ;
select * FROM employees order by salary desc ;
select first_name,salary,job_id,employee_id FROM employees order by salary desc ;

select first_name,last_name,(first_name|| ' ' || last_name)as "EMP_name" from employees;

select (first_name|| ' ' || last_name ||' earns monthly salary of '),salary from employees;
select salary,salary*12,(salary*12+10) from employees;
