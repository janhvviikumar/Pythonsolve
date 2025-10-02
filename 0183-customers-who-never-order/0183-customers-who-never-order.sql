# Write your MySQL query statement below
select name "Customers" from customers where id not in(select o.customerid from customers c,orders o where c.id=o.customerid);