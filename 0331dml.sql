DESC employees;
-- null doesnt occupy memory space 
--char for binary or gender mf 01
-- structure includes table columns datatype constraints
CREATE TABLE pib3_products (
    product_id        NUMBER(4) PRIMARY KEY NOT NULL,
    product_name      VARCHAR2(20) NOT NULL,
    quantity          NUMBER(3) CHECK ( quantity > 0 ),
    prod_description  VARCHAR2(20)
);
-- observe no commas in constraints and datatypes within a column , after end of column  , 
SELECT
    *
FROM
    tab;

SELECT
    *
FROM
    pib3_products;

DESC pib3_products;
--- fk pk not displays
CREATE TABLE pib3_orders (
    product_id     NUMBER(4)
        REFERENCES pib3_products ( product_id ),
    order_id       NUMBER(4) PRIMARY KEY NOT NULL,
    quantity_sold  NUMBER(3) CHECK ( quantity_sold > 0 ),
    price          NUMBER(8, 2),
    order_date     DATE
);

SELECT
    *
FROM
    tab;

SELECT
    *
FROM
    pib3_orders;
DESC pib3_orders;
--- duplicate of a table  , create table from another table
--constraints , types , dbms rdbms , data types , prime key , ddl dml tcl , imp qns , copy
-- only copies not null constraints only , but not check constraints 
CREATE TABLE pib3_temp1
    AS
        SELECT
            *
        FROM
            departments;
--- can specify where clause to copy specific 
SELECT
    *
FROM
    tab;
desc departments;
DESC pib3_temp1;
--explain diff bw dele and truct in more conceptual way
--trucate drop
--truncate is clear , drop is like delete in python
-- truncate : all rows data deleted except column names header and table name
-- truncsate cant undo -a auto commit 
--drop ; all rows including column name rows , and table name 
--auto commit
--delete , a particular rows or all rows for records
--can undo or rollback
CREATE TABLE pib3_test1
    AS
        SELECT
            *
        FROM
            departments;

CREATE TABLE pib3_test2
    AS
        SELECT
            *
        FROM
            departments;

DESC departments;

DESC pib3_test1;

DESC pib3_test2;

SELECT
    *
FROM
    departments;

SELECT
    *
FROM
    pib3_test1;

SELECT
    *
FROM
    pib3_test2;

TRUNCATE TABLE pib3_test1;

SELECT
    *
FROM
    pib3_test1;

DESC pib3_test1;
-- diff bw truncate vs drop
DROP TABLE pib3_test2;

SELECT
    *
FROM
    pib3_test2;--drop , error
DESC pib3_test2; -- error
select * from tab ;
PURGE RECYCLEBIN; -- to delete permanently any junk files or tab present in tab if anly just deleted file present 
FLASHBACK ; -- to restore
DESC pib3_test1;

RENAME pib3_test1 TO pib3_test10;

SELECT
    *
FROM
    tab;

SELECT
    *
FROM
    pib3_products;

ALTER TABLE pib3_products ADD model_no VARCHAR(20) NOT NULL;

DESC pib3_products;

ALTER TABLE pib3_products DROP COLUMN model_no;
--can drop column pk also , but referenced key column cant delete
DESC pib3_products;

ALTER TABLE pib3_products RENAME COLUMN prod_description TO product_description;

DESC pib3_products;
-- select is neither ddl nor dml

--dml , about records , insert
SELECT
    *
FROM
    pib3_products;

INSERT INTO pib3_products VALUES (
    1001,
    'CAMERA',
    10,
    'DIGITAL'
);

INSERT INTO pib3_products VALUES (
    1002,
    'LAPTOP',
    23,
    'DELL'
);

SELECT
    *
FROM
    pib3_products;
--all dml are not auto commit
ROLLBACK;
--deleted
SELECT
    *
FROM
    pib3_products;

INSERT INTO pib3_products VALUES (
    1001,
    'CAMERA',
    10,
    'DIGITAL'
);

INSERT INTO pib3_products VALUES (
    1002,
    'LAPTOP',
    23,
    'DELL'
);
--select  both lines and run
COMMIT;

ROLLBACK;
--this dont deletes
--order table
SELECT
    sysdate
FROM
    dual;

SELECT
    systimestamp
FROM
    dual;

INSERT INTO pib3_products VALUES (
    1001,
    'LAPTOP',
    23,
    'DELL'
);

--
INSERT INTO pib3_orders VALUES (
    1003,
    9003,
    5,
    9999.9,
    sysdate
);
--error
INSERT INTO pib3_orders VALUES (
    1002,
    9003,
    5,
    9999.9,
    sysdate
);

SELECT
    *
FROM
    pib3_orders;
--TO GET INPUT
INSERT INTO pib3_orders VALUES (
    '&product_id',
    &order_id,
    '&quantity_sold',
    '&price',
    '&order_date'
);
desc pib3_orders;
SELECT
    *
FROM
    pib3_orders;

SELECT
    *
FROM
    employees
ORDER BY
    2;

SELECT
    *
FROM
    employees
ORDER BY
    2,
    4;

SELECT
    *
FROM
    employees
ORDER BY
    2,
    4,
    7;

UPDATE pib3_orders
SET
    price = 8888
WHERE
    product_id = 1001;

SELECT
    *
FROM
    pib3_products;

INSERT INTO pib3_products VALUES (
    &product_id,
    '&PRODUCT_NAME',
    &quantity,
    '&PRODUCT_DESCRIPTION'
);

INSERT INTO pib3_orders VALUES (
    '&product_id',
    &order_id,
    '&quantity_sold',
    '&price',
    '&order_date'
);

COMMIT;

UPDATE pib3_products
SET
    product_description = 'vivo'
WHERE
    product_id = 1001;

SELECT
    *
FROM
    pib3_products;

UPDATE pib3_products
SET
    product_description = 'Lenovo',
    quantity = 100,
    product_name = 'laptop'
WHERE
    product_id = 1001;

COMMIT;

DESC pib3_temp1;

CREATE TABLE tmpemp
    AS
        SELECT
            *
        FROM
            employees;

SELECT
    *
FROM
    tmpemp;

UPDATE tmpemp
SET
    salary = salary + 200,
    commission_pct = 0.20
WHERE
    employee_id = 108;

SELECT
    *
FROM
    tmpemp
WHERE
    employee_id = 108;

COMMIT;
desc employees;

DELETE FROM tmpemp WHERE employee_id = 108;
-- can delete particular row/s
select * from tmpemp order by employee_id;
--nancy got deleted
rollback;
select * from tmpemp order by employee_id;
commit;
UPDATE tmpemp
SET
salary = 1.1*salary;
rollback;
SAVEPOINT save1;
UPDATE tmpemp
SET
salary = 1.1*salary;
UPDATE tmpemp
SET
salary = 1.1*salary;
UPDATE tmpemp
SET
salary = 1.1*salary;
select * from tmpemp order by employee_id;rollback save1 ; SELECT * FROM TMPEMP ORDER BY EMPLOYEE_ID ;
select count(*) from tmpemp;
delete from tmpemp;
commit;
