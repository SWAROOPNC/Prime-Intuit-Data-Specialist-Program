--SELECT FROM WHERE GROUP BY HAVING ORDER  BY
SELECT * FROM pib3_gf_employee;

--WHERE PARTICULAR ROW /S , PIck employees
--GROUP , SECTIONS , aggregate employee by dept wise 
--STANDARD TEMPLATE , COMMENT IT 
SELECT
    *
FROM
WHERE
GROUP BY
HAVING
ORDER BY ;
--GROUP BY MUST USE IN SELECT , SELECT COLUMNS MUST BE IN GROUP BY
-- GROUP BY TO COLLECT DATA ACROSS MULTIPLE RECORDS , AND GROUP RESULTS BYB O NE OR MORE COLUMNS
--TOTAL SALARY OF ALL DEPARTMENTS
SELECT
    department_id,SUM(SALARY)
FROM employees
--WHERE
GROUP BY department_id
--HAVING
ORDER BY 1 ;

--MAX SAL OF EACH JOB
SELECT
   JOB_ID,MAX(SALARY) 
FROM employees
--WHERE
GROUP BY JOB_ID
--HAVING
ORDER BY 1;
--https://www.techonthenet.com/sql/index.php