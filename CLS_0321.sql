/*SELECT * FROM TAB; -- line commenting /* multilinecomment*/ 
--DESCRIBE
--DESC employees; 
-- IT DOESNT SHOW UNIQUE , JUST NOT NULL OR DATA TYPE
--SELECT * FROM employees ;
--SELECT EMPLOYEE_ID, FIRST_NAME , LAST_NAME , SALARY FROM employees;
--select  from employees where salary=3000;
--select * from employees where job_id='IT_PROG';*/
-- Alt + " , for font variable 
SELECT * FROM EMPLOYEES WHERE JOB_ID='SH_CLERK';
select * from employees where salary<5000;
select * from employees where job_id='PU_CLERK';
select * from employees where department_id=90; 
select * from employees where department_id in 90; -- same as above , use of in