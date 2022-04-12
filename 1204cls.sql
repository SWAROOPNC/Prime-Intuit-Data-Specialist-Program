SELECT
    *
FROM
    departments
ORDER BY
    1;
--1)
SELECT
    *
FROM
    employees    e,
    departments  d
WHERE
        e.department_id = d.department_id
    AND d.department_name = 'Marketing'
ORDER BY
    1;
--or
SELECT
    *
FROM
    employees
WHERE
    department_id = (
        SELECT
            department_id
        FROM
            departments
        WHERE
            department_name = 'Marketing'
    );
-- single row sub query
--if 2 dept name given 2 dept no passes multiple row subqueries
--2)dept names having IT prog
SELECT
    department_id,
    department_name
FROM
    departments
WHERE
    department_id IN (
        SELECT
            department_id
        FROM
            employees
        WHERE
            job_id = 'IT_PROG'
    );

--3
SELECT
    department_id,
    department_name
FROM
    departments
WHERE
    department_id IN (
        SELECT
            department_id
        FROM
            employees
        WHERE
            job_id = 'IT_PROG'
    );



--3 employees in operations and sales dept

--
SELECT
    *
FROM
    departments;

SELECT
    *
FROM
    employees
WHERE
    department_id IN (
        SELECT
            department_id
        FROM
            departments
        WHERE
            department_name = 'Sales'
            OR department_name = 'Operations'
    )
ORDER BY
    1;
    
    
    ----ass1
SELECT
    *
FROM
    departments
WHERE
    department_id IN (
        SELECT
            department_id
        FROM
            employees
        WHERE
            job_id = 'SH_CLERK'
    )
ORDER BY
    1;
  --ass2
SELECT
    *
FROM
    employees
WHERE
    department_id IN (
        SELECT
            department_id
        FROM
            departments
        WHERE
            department_name LIKE '%o%'
            OR department_name LIKE '%O%'
    )
ORDER BY
    1;
  
---
SELECT
    department_name
FROM
    departments
WHERE
    department_id IN (
        SELECT
            department_id
        FROM
            employees
        GROUP BY
            department_id
        HAVING
            COUNT(*) >= 1
    );
----

SELECT
    department_name
FROM
    departments
WHERE
    department_id IN (
        SELECT
            department_id
        FROM
            employees
        GROUP BY
            department_id
        HAVING
            COUNT(*) >= 4
    );
    
    ---
    
    SELECT * FROM departments
WHERE
    department_id IN (
        SELECT department_id
        FROM
            employees
        GROUP BY
            department_id
        HAVING
            COUNT(*) = 0
    );
    
select * from departments where department_id not in ( select distinct department_id from employees);

SELECT
    *
FROM
    employees
ORDER BY
    salary;
  ---1st max salary  
SELECT
    *
FROM
    employees
WHERE
    salary = (
        SELECT
            MAX(salary)
        FROM
            employees
    );


--2nd max salary
SELECT
    *
FROM
    employees
WHERE
    salary = (
        SELECT MAX(salary) FROM employees WHERE salary < 
                (
                SELECT
                    MAX(salary)
                FROM
                    employees
            )
    );
-- only india first rest ascending
--4th min 
SELECT * FROM employees WHERE
    salary = (
                 SELECT min(salary) FROM employees WHERE salary >
                    (SELECT min(salary) FROM employees WHERE salary >
                 ( SELECT min(salary) FROM employees WHERE salary > 
                ( SELECT min(salary) FROM  employees )))
    );

( SELECT
    *
FROM
    countries
WHERE
    country_name = 'India'
)
UNION
( SELECT
    *
FROM
    countries
WHERE
    country_name != 'India'
);
