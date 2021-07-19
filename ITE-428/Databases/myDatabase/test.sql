--1
select productname, unitprice
	from products 
	natural join categories
	where lower(categoryname) = lower('seafood')
	order by 1;

--2
select productname, unitprice
        from products 
        natural join categories
        where unitprice between 5 and 10
        order by 2 desc, 1;

--3
select upper(country) as c, count(country) as noc
        from suppliers 
        group by country
        order by 2 desc, 1;

--4
select region, count(distinct country) as noc, count(distinct city) as ncity
        from customers
        group by region
        order by 3 desc, 1;

--5
select productId as id, productName, unitPrice * unitsInStock as StockValue
        from products
        where StockValue > 3000
        order by 3 desc;

--6		
select CategoryName as cat, count(ProductId) as pd, sum(unitPrice * unitsInStock) as StockValue
        from products
        natural join categories
        group by CategoryId
        having StockValue > 5000
        order by 3;

--7		
select firstname || ' ' || lastname || ' , ' || TitleOfCourtesy as name, count(orderId) as 'order'
        from employees
        natural join orders
        group by employeeId
        order by 2;

--8		
SELECT CompanyName as name, CategoryName as cat, count(ProductId) as noProd, avg(UnitPrice) as avgPrice
		FROM Suppliers
		NATURAL JOIN Categories
		NATURAL JOIN Products
		GROUP BY SupplierId, CategoryId
		ORDER BY 1;

--9
CREATE VIEW Invoices AS
SELECT o.OrderId, OrderDate, ShipName as Customer, ProductName, od.UnitPrice * Quantity as Price, CompanyName
FROM Orders o
JOIN OrdersDetails od on o.OrderId = od.OrderId
JOIN Shippers s on ShipVia = s.ShipperID
JOIN Products p on od.ProductId = p.ProductId;

SELECT OrderId, OrderDate, Customer, ProductName, Price, CompanyName
FROM Invoices
WHERE OrderId = 10309
ORDER BY 4;

--10
-- CREATE VIEW CustomersBySales AS
SELECT Country, count(OrderId) as 'NoOrder', 
	   sum(UnitPrice * Quantity - UnitPrice * Quantity * Discount) * 1.07 as 'NetPrice', 
	   avg(UnitPrice * Quantity - UnitPrice * Quantity * Discount) * 1.07 as 'Price/Order'
FROM Orders
NATURAL JOIN OrdersDetails
NATURAL JOIN Customers
GROUP BY Country
ORDER BY 4 DESC;

--11
SELECT ProductId, ProductName, UnitPrice, 
	 UnitPrice - (SELECT avg(UnitPrice)
				  FROM Products) as PriceDiff
FROM Products
WHERE UnitPrice > (SELECT avg(UnitPrice)
				   FROM Products)
ORDER BY 3 DESC;

--12
SELECT p.ProductId, ProductName, count(p.ProductId) as NoSales
FROM Products p
JOIN OrdersDetails o ON p.ProductId = o.ProductId
GROUP BY p.ProductId
HAVING NoSales > 50;

--13
SELECT *
FROM Customers;

SELECT CustomerId
FROM Customers;

INSERT INTO CUSTOMERS
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

--14
SELECT ProductId, ProductName, UnitPrice, UnitsInStock, Discontinued
FROM Products
WHERE ProductId = 2;

UPDATE Products
SET Discontinued = 1
WHERE ProductId = 2;
