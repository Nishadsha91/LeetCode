-- # Write your MySQL query statement below
-- SELECT  c.name , o.id FROM Customers c
-- JOIN Orders o
-- WHERE o.id NOT IN c.name

SELECT c.name AS Customers 
FROM Customers c
LEFT JOIN Orders o
    ON c.id = o.customerId
WHERE o.id IS NULL;
