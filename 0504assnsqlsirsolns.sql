--1. Display all manager whose annual salary is ending with zero. 

SELECT EMPLOYEE_ID,FIRST_NAME,LAST_NAME, SALARY, MANAGER_ID 
FROM EMPLOYEES ORDER BY 1;

SELECT DISTINCT MANAGER_ID FROM EMPLOYEES ORDER BY 1;

SELECT EMPLOYEE_ID,FIRST_NAME,LAST_NAME, SALARY,(SALARY*12) AS ANNUAL_SALARY
  FROM EMPLOYEES 
 WHERE EMPLOYEE_ID IN (SELECT DISTINCT MANAGER_ID FROM EMPLOYEES)
 AND (SALARY*12) LIKE '%0';

--2. Display all employees who have joined after year 81 or year 2005
SELECT * FROM EMPLOYEES WHERE HIRE_DATE > '31-DEC-2005';

--3. Display all employees who have joined in FEBRUARY. 
SELECT * FROM EMPLOYEES WHERE HIRE_DATE LIKE '%FEB%';

--4. Display all employees who have joined before 01/05/81 and after 01/05/80.
--before 31/12/2010 and after 01/05/2005
SELECT * FROM EMPLOYEES WHERE HIRE_DATE BETWEEN '01-MAY-2005' AND '31-DEC-2010';