--group by
--where vs groupby
--where to filter ungrouped data , used before group by clause
--having  to filter grouped data
--order of keywords
--select from where group by having order by
-- group -aggregate function
-- null wont considered for avg
--count(*) --- all rows
--COUNT(*) includes NULL values in the total. 
--The notation COUNT( column_name ) only considers rows where the column contains a non- NULL value.

CREATE TABLE pib3_gf_employee (
    employee_id      NUMBER(3) PRIMARY KEY,
    employee_name    VARCHAR2(30) NOT NULL,
    department_name  VARCHAR2(40) NOT NULL,
    salary           NUMBER(8, 2)
);

INSERT INTO pib3_gf_employee VALUES (
    101,
    'MANOJ',
    'HR',
    10000
);

INSERT INTO pib3_gf_employee VALUES (
    102,
    'KIRAN',
    'SALES',
    20000
);

INSERT INTO pib3_gf_employee VALUES (
    103,
    'RAVI',
    'HR',
    30000
);

INSERT INTO pib3_gf_employee VALUES (
    104,
    'VIVEK',
    'SALES',
    30000
);

INSERT INTO pib3_gf_employee VALUES (
    105,
    'SUDHIR',
    'IT',
    50000
);

INSERT INTO pib3_gf_employee VALUES (
    106,
    'PAVAN',
    'ADMIN',
    NULL
);

SELECT
    *
FROM
    pib3_gf_employee;
-- insert removes data not structure
COMMIT;

SELECT
    MAX(salary)
FROM
    pib3_gf_employee;

SELECT
    MIN(salary)
FROM
    pib3_gf_employee;

SELECT
    COUNT(*)
FROM
    pib3_gf_employee;

SELECT
    COUNT(DISTINCT salary)
FROM
    pib3_gf_employee; --4 output  ,30
SELECT
    SUM(salary)
FROM
    pib3_gf_employee;

SELECT
    SUM(DISTINCT salary)
FROM
    pib3_gf_employee;

SELECT
    AVG(salary)
FROM
    pib3_gf_employee;

SELECT
    avg(DISTINCT salary)
FROM
    pib3_gf_employee;

SELECT
    MAX(salary),
    MIN(salary),
    SUM(salary)
FROM
    employees;

SELECT
    MAX(salary)     AS high,
    MIN(salary)     AS low,
    SUM(salary)     AS sum
FROM
    employees;
    -- double quotes
SELECT
    MAX(salary)     AS "high salary",
    MIN(salary)     AS "low salary",
    SUM(salary)     AS "sum salary"
FROM
    employees;

SELECT
    COUNT(*)
FROM
    employees;

SELECT
    COUNT(*),
    COUNT(employee_id),
    COUNT(department_id)
FROM
    employees;

SELECT
    COUNT(*),
    COUNT(commission_pct)
FROM
    employees;

SELECT
    COUNT(*)
FROM
    employees
WHERE
    department_id = 30;

SELECT
    SUM(salary)
FROM
    employees
WHERE
    department_id = 30;

SELECT
    COUNT(*)
FROM
    employees
WHERE
        department_id = 30
    AND job_id LIKE '%CLERK';

SELECT DISTINCT
    ( job_id )
FROM
    employees;
----
SELECT
    MAX(salary),
    MIN(salary)
FROM
    employees
WHERE
    job_id = 'SA_MAN';

SELECT
    job_id,
    salary
FROM
    employees
WHERE
    job_id = 'SA_MAN'
ORDER BY
    salary;
--
SELECT
    department_id,
    SUM(salary)
FROM
    employees
GROUP BY
    department_id
ORDER BY
    1;
-- order by 1 in this query table

SELECT
    job_id,
    MAX(salary)
FROM
    employees
GROUP BY
    job_id
ORDER BY
    1;

SELECT
    job_id,
    MAX(salary)
FROM
    employees
GROUP BY
    job_id
HAVING
    MAX(salary) > 10000
ORDER BY
    2 DESC;
--having
SELECT
    job_id,
    MAX(salary)
FROM
    employees 
where department_id <> 30 
GROUP BY
    job_id
HAVING
    MAX(salary) > 10000
order by 2;

SELECT
    department_id, job_id , sum(salary)
FROM employees group by department_id;
--not work
-- to make work
SELECT
    department_id, job_id , sum(salary)
FROM employees group by department_id, job_id
order by 1,2;