--DISPLAY THE DEPARTMENT NAME WHICH HAS HIGHEST EMPLOYEES?

SELECT DEPARTMENT_ID,COUNT(*) 
FROM EMPLOYEES 
GROUP BY DEPARTMENT_ID 
order by 2 desc;

SELECT DEPARTMENT_ID,DEPARTMENT_NAME FROM DEPARTMENTS where DEPARTMENT_ID=50;

SELECT DEPARTMENT_ID,COUNT(*) 
  FROM EMPLOYEES 
GROUP BY DEPARTMENT_ID 
 HAVING COUNT(*)=(SELECT MAX(COUNT(*)) FROM EMPLOYEES GROUP BY DEPARTMENT_ID);

SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME, COUNT(*) as "Highest Number of Employees"---E.EMPLOYEE_ID
FROM EMPLOYEES E INNER JOIN DEPARTMENTS D
  ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_NAME,D.DEPARTMENT_ID
HAVING COUNT(*)=(SELECT MAX (COUNT(*)) FROM EMPLOYEES E GROUP BY E.DEPARTMENT_ID);