CREATE TABLE suppliers
    (supplier_id number(4,0) primary key ,
    supplier_name varchar(50) not null);

select * from suppliers;
desc suppliers;

CREATE TABLE orders
    (order_id number(4,0) primary key ,
    supplier_id number(4,0)  references suppliers(supplier_id),
    order_date date );
select * from orders;
desc orders;

select * from tab;
purge recyclebin;

insert into suppliers values (1000,'IBM');
insert into suppliers values (1001,'HP');
insert into suppliers values (1002,'MS');
insert into suppliers values (1003,'NvD');

select * from suppliers;

insert into orders values (5011,1000,to_date('1-Jan-21','DD-MM-YY'));
insert into orders values (5012,1001,to_date('2-Jan-21','DD-MM-YY'));

select * from orders;

drop table orders;
CREATE TABLE orders
    (order_id number(4,0) primary key ,
    supplier_id number(4,0) ,
    order_date date );
select * from orders;

insert into orders values (5011,1000,to_date('1-Jan-21','DD-MM-YY'));
insert into orders values (5012,1001,to_date('2-Jan-21','DD-MM-YY'));
insert into orders values (5013,1004,to_date('3-Jan-21','DD-MM-YY'));

commit;
alter table orders add constraint  foreign key(supplier_id) references suppliers(supplier_id) enable;

select s.supplier_id , s.supplier_name, o.order_id,o.order_date
from suppliers s
inner join orders o
on s.supplier_id = o.supplier_id;
commit;

select s.supplier_id , s.supplier_name, o.order_id,o.order_date
from suppliers s
left outer join orders o
on s.supplier_id = o.supplier_id;
--left outer join or left join
--old syntax
select s.supplier_id , s.supplier_name, o.order_id,o.order_date
from suppliers s
, orders o
where s.supplier_id = o.supplier_id(+);

select s.supplier_id , s.supplier_name, o.order_id,o.order_date
from suppliers s
right outer join orders o
on s.supplier_id = o.supplier_id;
--old sytax
select s.supplier_id , s.supplier_name, o.order_id,o.order_date
from suppliers s
, orders o
where s.supplier_id(+) = o.supplier_id;

select s.supplier_id , s.supplier_name, o.order_id,o.order_date
from suppliers s
full outer join orders o
on s.supplier_id = o.supplier_id;
--full join or full outer join
--old sytax
select s.supplier_id , s.supplier_name, o.order_id,o.order_date
from suppliers s
, orders o
where s.supplier_id = o.supplier_id;

-- from here its messed up
--self join