/* CORELATED SUBQUERIES - CORRELATED NESTED QUERIES - EXIST / NOT EXIST Subqueries*/

--IT IS A SUBQUERY THAT USES VALUES FROM OUTER QUERY AND FOLLOWS TOP TO DOWN APPROACH

SELECT
    *
FROM
    pi_corr_employees;

SELECT
    *
FROM
    pi_corr_departments;

/* PI_CORR_EMPLOYEES TABLE  */

--DROP TABLE PI_CORR_EMPLOYEES;

/*CREATE TABLE PI_CORR_EMPLOYEES 
(EMP_ID VARCHAR2(5) PRIMARY KEY,
 EMP_NAME VARCHAR2(30) NOT NULL,
 EMP_ADDRESS VARCHAR2(50));
 
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E1','AJAY','MYSURU');
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E2','AKSHAY','KOLLEGAL');
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E3','BHOOMIKA','MYSURU');
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E4','CHANDANI','MADDUR');
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E5','DEEPTHI','MANDYA');
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E6','KIRAN','MYSURU');
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E7','RAHUL','BENGALURU');
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E8','SWATHI','TUMKUR');
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E9','SUMITH','BENGALURU');
INSERT INTO PI_CORR_EMPLOYEES VALUES ('E10','TEJAS','TUMKUR');*/
COMMIT;

/*  PI_CORR_DEPARTMENTS TABLE  */

--DROP TABLE PI_CORR_DEPARTMENTS;

/*CREATE TABLE PI_CORR_DEPARTMENTS
(DEPT_ID VARCHAR2(20) PRIMARY KEY,
 DEPT_NAME VARCHAR2(30) NOT NULL,
 EMP_ID VARCHAR2(5) REFERENCES PI_CORR_EMPLOYEES(EMP_ID)
 );
 
INSERT INTO PI_CORR_DEPARTMENTS VALUES ('D1','HR','E1');
INSERT INTO PI_CORR_DEPARTMENTS VALUES ('D2','SALES','E2');
INSERT INTO PI_CORR_DEPARTMENTS VALUES ('D3','IT','E3');
INSERT INTO PI_CORR_DEPARTMENTS VALUES ('D4','ADMIN','E4');
INSERT INTO PI_CORR_DEPARTMENTS VALUES ('D5','TESTING','E5');
INSERT INTO PI_CORR_DEPARTMENTS VALUES ('D6','OPERATIONS','E6');
INSERT INTO PI_CORR_DEPARTMENTS VALUES ('D7','ACCOUNTS','E7');
INSERT INTO PI_CORR_DEPARTMENTS VALUES ('D8','MARKETING',null);*/
COMMIT;

SELECT
    *
FROM
    pi_corr_employees;

SELECT
    *
FROM
    pi_corr_departments;

--Example: Find all employees detail who work in any department ?

SELECT
    *
FROM
    pi_corr_employees e
WHERE
    EXISTS (
        SELECT
            *
        FROM
            pi_corr_departments d
        WHERE
            d.emp_id = e.emp_id
    );

/*
1) Get the candidate key/primary key from the outer query  --> emp id = E1
2) Execute the inner query using the primary key value --> compare with each record of inner query values 
3) Use values from inner query to qualify or disqualify --> True /false
the loop continues 
*/

--NOT EXISTS:               

SELECT
    *
FROM
    pi_corr_employees e
WHERE
    NOT EXISTS (
        SELECT
            *
        FROM
            pi_corr_departments d
        WHERE
            d.emp_id = e.emp_id
    );

/*======== Find Nth(1st,2nd,3rd....N) Highest Salary ===========*/

SELECT
    *
FROM
    employees;

SELECT
    salary
FROM
    employees
ORDER BY
    salary DESC;

--WRITE A QUERY TO DISPLAY THE MAX/HIGHEST SALARY FROM EMPLOYEE TABLE:

SELECT
    MAX(salary)
FROM
    employees;  

--WRITE A QUERY TO DISPLAY THE EMPLOYEE NAME WHO IS TAKING MAX SALARY FROM EMPLOYEE TABLE:
                --(SUBQUERY OR NESTED QUERY)

SELECT
    first_name
    || ' '
    || last_name AS employee_name,
    salary --> OUTER QEURY
FROM
    employees
WHERE
    salary = (
        SELECT
            MAX(salary)
        FROM
            employees
    );  --> INNER QUERY
 
 --complete employee details who earns max salary:

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
 
--WRITE A QUERY TO DISPLAY THE 2ND HIGHEST SALARY FROM EMPLOYEE TABLE:

--<> - not equal to 
SELECT
    MAX(salary)
FROM
    employees
WHERE
    salary <> (
        SELECT
            MAX(salary)
        FROM
            employees
    );

--< - less than
SELECT
    MAX(salary)
FROM
    employees
WHERE
    salary < (
        SELECT
            MAX(salary)
        FROM
            employees
    );
 
--NOT IN
SELECT
    MAX(salary)
FROM
    employees
WHERE
    salary NOT IN (
        SELECT
            MAX(salary)
        FROM
            employees
    ); 

/*WRITE A QUERY TO DISPLAY THE EMPLOYEE NAME/EMPLOYEE DETAILS 
  WHO IS TAKING 2ND HIGHEST SALARY FROM EMPLOYEE TABLE:*/

SELECT
    ( first_name
      || ' '
      || last_name ) AS employee_name,
    salary
FROM
    employees
WHERE
    salary = (
        SELECT
            MAX(salary)
        FROM
            employees
        WHERE
            salary <> (
                SELECT
                    MAX(salary)
                FROM
                    employees
            )  --NOT IN
    );

--2nd Highest  --> 2 inner + 1 outer query  = 3 queries

/*WRITE A QUERY TO DISPLAY THE EMPLOYEE NAME/EMPLOYEE DETAILS 
  WHO IS TAKING 3RD HIGHEST SALARY FROM EMPLOYEE TABLE:*/

SELECT
    ( first_name
      || ' '
      || last_name ) AS employee_name,
    salary
FROM
    employees
WHERE
    salary = (
        SELECT
            MAX(salary)                                                    --24000
        FROM
            employees
        WHERE
            salary < (
                SELECT
                    MAX(salary)                                   --25000
                FROM
                    employees
                WHERE
                    salary < (
                        SELECT
                            MAX(salary)
                        FROM
                            employees
                    )
            ) --26000
    ); 

--3rd Highest  --> 3 inner + 1 outer query  = 4 queries   
--nth Highest  --> (n-1) inner + 1 outer query  = n queries

/*======== Find Nth(1st,2nd,3rd....N) Highest Salary - Using Correlated Subquery =========*/
--do not run below , its generic formula;
SELECT
    employee_id,
    salary
FROM
    employees e1
WHERE
    ( n - 1 ) = (
        SELECT
            COUNT(DISTINCT salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );

--FIRST HIGHEST SALARY -> N-1 FORMULA --> (N=1)  --> 1-1 

SELECT
    employee_id,
    first_name,
    salary
FROM
    employees
ORDER BY
    3 DESC;

SELECT
    e1.employee_id,
    e1.first_name,
    e1.salary
FROM
    employees e1
WHERE
    1 - 1 = (
        SELECT
            COUNT(DISTINCT e2.salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );  ---0,1,2,3

--SECOND HIGHEST SALARY -> N-1 FORMULA --> (N=2)  --> 2-1=1 

SELECT
    e1.employee_id,
    e1.first_name,
    e1.salary
FROM
    employees e1
WHERE
    2 - 1 = (
        SELECT
            COUNT(DISTINCT e2.salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );
                                      
--THIRD HIGHEST SALARY-> N-1 FORMULA --> (N=3)  --> 3-1=2 

SELECT
    e1.employee_id,
    e1.first_name,
    e1.salary
FROM
    employees e1
WHERE
    3 - 1 = (
        SELECT
            COUNT(DISTINCT e2.salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );

--FOURTH HIGHEST SALARY-> N-1 FORMULA --> (N=4)  --> 4-1=3 

SELECT
    e1.employee_id,
    e1.first_name,
    e1.salary
FROM
    employees e1
WHERE
    4 - 1 = (
        SELECT
            COUNT(DISTINCT e2.salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );

SELECT
    employee_id,
    salary
FROM
    employees
ORDER BY
    salary DESC;  

--SEVENTH HIGHEST SALARY-> N-1 FORMULA --> (N=7)  --> 7-1=6 

SELECT
    e1.employee_id,
    e1.first_name,
    e1.salary
FROM
    employees e1
WHERE
    7 - 1 = (
        SELECT
            COUNT(DISTINCT e2.salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );

--DISTINCT

SELECT DISTINCT
    e1.salary
FROM
    employees e1
WHERE
    6 = (
        SELECT
            COUNT(DISTINCT e2.salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );

--TENTH HIGHEST SALARY-> N-1 FORMULA --> (N=10)  --> 10-1=9 

SELECT
    e1.employee_id,
    e1.salary
FROM
    employees e1
WHERE
    10 - 1 = (
        SELECT
            COUNT(DISTINCT e2.salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );
             
             
-- how to find the 1st, 4th and 8th highest salary ?

SELECT
    employee_id,
    first_name,
    salary
FROM
    employees
ORDER BY
    3 DESC;

207	26000
208	23000
145	14000

SELECT DISTINCT SALARY,EMPLOYEE_ID FROM EMPLOYEES ORDER BY SALARY DESC;

SELECT A.EMPLOYEE_ID, A.SALARY FROM (
SELECT E1.EMPLOYEE_ID, E1.SALARY  
  FROM EMPLOYEES E1 
 WHERE 1-1 = (SELECT COUNT(DISTINCT E2.SALARY) 
              FROM EMPLOYEES E2 
             WHERE E2.SALARY > E1.SALARY)
             
UNION

SELECT E1.EMPLOYEE_ID, E1.SALARY  
  FROM EMPLOYEES E1 
 WHERE 4-1 = (SELECT COUNT(DISTINCT E2.SALARY) 
              FROM EMPLOYEES E2 
             WHERE E2.SALARY > E1.SALARY)

UNION

SELECT E1.EMPLOYEE_ID, E1.SALARY  
  FROM EMPLOYEES E1 
 WHERE 8-1 = (SELECT COUNT(DISTINCT E2.SALARY) 
              FROM EMPLOYEES E2 
             WHERE E2.SALARY > E1.SALARY))A ORDER BY 2 DESC;

===========================================================================================                    

/*  Difference between Nested Subquery, Correlated Subquery and Joins  */

/*
When a query is included inside another query, the Outer query is known as Main Query, 
and Inner query is known as Subquery.

In Nested Query,  Inner query runs first, and only once. 
Outer query is executed with result from Inner query.
Hence, Inner query is used in execution of Outer query.

In Correlated Query,  Outer query executes first and for every Outer query row Inner query is executed. 
Hence, Inner query uses values from Outer query.

Joins are used when we need to fetch the data from multiple tables
To find the Emp Id, Emp Name,Dept Id & Dept Name...we use Joins
*/

SELECT * FROM PI_CORR_EMPLOYEES;
SELECT * FROM PI_CORR_DEPARTMENTS;

--Find all employees detail who works in any department ?

--NESTED QUERY or SIMPLE QUERY or NON-CORRELATED SUB QUERY

SELECT * FROM PI_CORR_EMPLOYEES E
WHERE EMP_ID IN (SELECT EMP_ID 
                   FROM PI_CORR_DEPARTMENTS D
                 ); 

--CORRELATED SUBQUERY

SELECT * FROM PI_CORR_EMPLOYEES E 
WHERE EXISTS (SELECT * 
                FROM PI_CORR_DEPARTMENTS D
               WHERE D.EMP_ID = E.EMP_ID);

--NOT EXISTS:               

SELECT * FROM PI_CORR_EMPLOYEES E 
WHERE NOT EXISTS (SELECT * 
                FROM PI_CORR_DEPARTMENTS D
               WHERE D.EMP_ID = E.EMP_ID);               

--JOINS: (CROSS PRODUCT + CONDITION)

SELECT COUNT(*) FROM PI_CORR_EMPLOYEES;   --10
SELECT COUNT(*) FROM PI_CORR_DEPARTMENTS; --8

SELECT * FROM PI_CORR_EMPLOYEES E ,PI_CORR_DEPARTMENTS D;  --cartesian product - 10 * 8 = 80
SELECT * FROM PI_CORR_EMPLOYEES E , PI_CORR_DEPARTMENTS D where E.EMP_ID = D.EMP_ID; --with condition

SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_ID,D.DEPT_NAME 
  FROM PI_CORR_EMPLOYEES E INNER JOIN PI_CORR_DEPARTMENTS D
    ON E.EMP_ID = D.EMP_ID
ORDER BY 1; = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
      

-- Display the least salary from the employee table.

SELECT
    employee_id,
    salary
FROM
    employees e1
WHERE
    ( 1 - 1 ) = (
        SELECT
            COUNT(DISTINCT salary)
        FROM
            employees e2
        WHERE
            e2.salary < e1.salary
    ); 

-- Display top 3 person's salaries from the employee table.               

SELECT
    e1.employee_id,
    e1.first_name,
    e1.salary
FROM
    employees e1
WHERE
    4 - 1 > (
        SELECT
            COUNT(DISTINCT e2.salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );               
             --note = not included
--Write a query to display bottom 3 salaries

SELECT
    e1.employee_id,
    e1.first_name,
    e1.salary
FROM
    employees e1
WHERE
    4 - 1 > (
        SELECT
            COUNT(DISTINCT e2.salary)
        FROM
            employees e2
        WHERE
            e2.salary < e1.salary
    )
ORDER BY
    3;  
--
--Display 1st and 4th maximum salary in a single query

SELECT
    salary
FROM
    employees
ORDER BY
    1 DESC;   --26K & 23K

SELECT
    employee_id,
    salary
FROM
    employees e1
WHERE
    ( 1 - 1 ) = (
        SELECT
            COUNT(DISTINCT salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    )
UNION
SELECT
    employee_id,
    salary
FROM
    employees e1
WHERE
    ( 4 - 1 ) = (
        SELECT
            COUNT(DISTINCT salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );
               
--Display 1st, 4th & 6th highest salaries in a single query  

SELECT
    salary
FROM
    employees
ORDER BY
    1 DESC;   --26K,23K,21K

SELECT
    employee_id,
    salary
FROM
    employees e1
WHERE
    ( 1 - 1 ) = (
        SELECT
            COUNT(DISTINCT salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    )
UNION
SELECT
    employee_id,
    salary
FROM
    employees e1
WHERE
    ( 4 - 1 ) = (
        SELECT
            COUNT(DISTINCT salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    )
UNION
SELECT
    employee_id,
    salary
FROM
    employees e1
WHERE
    ( 6 - 1 ) = (
        SELECT
            COUNT(DISTINCT salary)
        FROM
            employees e2
        WHERE
            e2.salary > e1.salary
    );