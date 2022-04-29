

--SELF JOIN:

--Display employee name along with their manager name

select employee_id, (FIRST_NAME||' '||LAST_NAME) AS EMPLOYEE_NAME, 
        manager_id 
        from employees
        order by 1;
        
100	Steven King	
101	Neena Kochhar	100
102	Lex De Haan	100
103	Alexander Hunold 102
104	Bruce Ernst	103
105	David Austin	103
106	Valli Pataballa	103
107	Diana Lorentz	103
108	Nancy Greenberg	101
109	Daniel Faviet	108
110	John Chen	108
111	Ismael Sciarra	108
112	Jose Manuel Urman	108
113	Luis Popp	108
114	Den Raphaely	100        

SELECT (E1.FIRST_NAME||' '||E1.LAST_NAME) AS EMPLOYEE_NAME, 
       (E2.FIRST_NAME||' '||E2.LAST_NAME) AS MANAGER_NAME 
FROM EMPLOYEES E1 INNER JOIN EMPLOYEES E2 
ON E1.MANAGER_ID = E2.EMPLOYEE_ID ; 

SELECT  E1.EMPLOYEE_ID, 
        (E1.FIRST_NAME||' '||E1.LAST_NAME) AS EMPLOYEE_NAME, 
        E1.MANAGER_ID,
        (E2.FIRST_NAME||' '||E2.LAST_NAME) AS MANAGER_NAME
FROM EMPLOYEES E1 INNER JOIN EMPLOYEES E2
--FROM EMPLOYEES E1 LEFT JOIN EMPLOYEES E2
ON E1.MANAGER_ID = E2.EMPLOYEE_ID;

SELECT 
(E1.FIRST_NAME||' '||E1.LAST_NAME)|| ' works for'  AS EMPLOYEE_NAME, 
(E2.FIRST_NAME||' '||E2.LAST_NAME) AS MANAGER_NAME
FROM EMPLOYEES E1 INNER JOIN EMPLOYEES E2
ON E1.MANAGER_ID = E2.EMPLOYEE_ID;

SELECT 
((E1.FIRST_NAME||' '||E1.LAST_NAME)|| ' works for '  || (E2.FIRST_NAME||' '||E2.LAST_NAME) )  
AS "EMPLOYEES WITH THEIR MANAGERS"
FROM EMPLOYEES E1 INNER JOIN EMPLOYEES E2
ON E1.MANAGER_ID = E2.EMPLOYEE_ID;

SELECT (E1.FIRST_NAME || ' works for ' || E2.FIRST_NAME)
FROM EMPLOYEES E1 INNER JOIN EMPLOYEES E2
ON E1.MANAGER_ID = E2.EMPLOYEE_ID;

/*Display the employees who are getting the same salary*/

select employee_id,first_name,last_name,salary from employees order by salary desc;

Neena	Kochhar	    17000
 Lex	De Haan	    17000
Nancy	Greenberg	12008
Shelley	Higgins	    12008
Gerald	Cambrault	11000
Ellen	Abel	    11000
Den	Raphaely	    11000
Clara	Vishney	    10500
Eleni	Zlotkey	    10500
Janette	King	    10000
Peter	Tucker	    10000
Hermann	Baer	    10000
Harrison	Bloom	10000

SELECT   distinct E1.EMPLOYEE_ID,
        (E1.FIRST_NAME||' '||E1.LAST_NAME) AS EMPLOYEE_NAME, 
         E1.SALARY
FROM EMPLOYEES E1 INNER JOIN EMPLOYEES E2
  ON E1.SALARY = E2.SALARY 
 AND E1.EMPLOYEE_ID <> E2.EMPLOYEE_ID
 order by 3 desc,2;   

/*Write a query to display the name of all employees including the name of their manager.*/

SELECT (E1.FIRST_NAME || ' ' || E1.LAST_NAME) AS EMPLOYEE_NAME,
       (E2.FIRST_NAME || ' ' || E2.LAST_NAME) AS MANAGER_NAME
  FROM EMPLOYEES E1
  INNER JOIN EMPLOYEES E2
    ON E1.MANAGER_ID = E2.EMPLOYEE_ID;
/*Write a query to display the first name of all employees and 
  the first name of their manager including those who does not work under any manager.*/
SELECT COUNT(*) FROM (
SELECT (E1.FIRST_NAME||' '||E1.LAST_NAME) AS EMPLOYEE_NAME, 
       (E2.FIRST_NAME||' '||E2.LAST_NAME) AS MANAGER_NAME
FROM EMPLOYEES E1 INNER JOIN EMPLOYEES E2
ON E1.MANAGER_ID = E2.EMPLOYEE_ID);

--SELECT COUNT(*) FROM ( --111
SELECT E1.FIRST_NAME AS EMPLOYEE_NAME,
       E2.FIRST_NAME AS MANAGER_NAME
  FROM EMPLOYEES E1
  LEFT JOIN EMPLOYEES E2
    ON E1.MANAGER_ID = E2.EMPLOYEE_ID
    ;-- this is actual query
    
/*Write a query to display the first name, last name and department number 
for those employees who works in the same department as the employee who holds the 
last name as Taylor.*/

SELECT E1.FIRST_NAME,
       E1.LAST_NAME,
       E1.DEPARTMENT_ID
  FROM EMPLOYEES E1
  INNER JOIN EMPLOYEES E2
    ON E1.DEPARTMENT_ID = E2.DEPARTMENT_ID
      AND E2.LAST_NAME = 'Taylor';    

SELECT FIRST_NAME,LAST_NAME,DEPARTMENT_ID 
  FROM EMPLOYEES 
 WHERE LAST_NAME = 'Taylor' ;

Jonathon  Taylor	80
Winston	  Taylor	50