/*; SEMICOLON MUST , COMMA AS SEPERATORS*/
/* SELECT column1, function_name(column2) FROM table_name WHERE condition GROUP BY column1, column2 HAVING condition ORDER BY column1, column2;*/
SELECT
    employee_id,
    first_name,
    salary,
    ( salary * 12 ) AS annual_salary
FROM
    employees;

SELECT
    employee_id,
    first_name,
    salary,
    ( salary * 12 ) AS "ANNUAL SALARY"
FROM
    employees;

DESC departments;

SELECT
    *
FROM
    departments;
    
/* Ctrl+F7 to beautify sql script, CONTROL SPACE AFTER WRITING */
SELECT
    d.department_id,
    d.department_name
FROM
    departments d;
/*WORKS FOR ALIAS ALSO AND WO ALSO, FIRST WRITE SELECT FROM TABLENAME THEN COLUMN NAMES*/
SELECT
    department_id,
    department_name,
    manager_id
FROM
    departments
ORDER BY
    manager_id;

SELECT
    department_name
FROM
    departments
WHERE
    manager_id = 200;
/*-- Alt " , for font STYLE variable , sql not case sensitive , go to line control enter run */
SELECT
    employee_id,first_name,salary
FROM employees;
