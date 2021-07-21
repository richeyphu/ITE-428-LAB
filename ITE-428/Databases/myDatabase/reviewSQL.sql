SELECT * from Products;

--1
SELECT ProductName, UnitPrice, UnitsInStock
FROM Products;

--2
SELECT ProductName, UnitPrice as 'Price', UnitsInStock
FROM Products;

--3
SELECT ProductName,UnitPrice as 'Price', UnitsInStock, UnitPrice * UnitsInStock as 'ValueInStock'
FROM Products;

--4
SELECT upper(ProductName) as 'Product', UnitPrice as 'Price', UnitsInStock, UnitPrice * UnitsInStock as 'ValueInStock'
FROM Products;

--5
SELECT upper(ProductName) as 'Product', UnitPrice as 'Price', UnitsInStock, UnitPrice * UnitsInStock as 'ValueInStock'
FROM Products
ORDER BY 4 DESC;

--6
SELECT upper(ProductName) as 'Product', UnitPrice as 'Price', UnitsInStock, UnitPrice * UnitsInStock as 'ValueInStock'
FROM Products
WHERE ValueInStock >= 3000
ORDER BY 4 DESC;

--7
SELECT upper(ProductName) as 'Product', UnitPrice as 'Price', UnitsInStock, UnitPrice * UnitsInStock as 'ValueInStock'
FROM Products
WHERE ValueInStock >= 3000 AND Price < 100
ORDER BY 4 DESC;

--8
SELECT upper(ProductName) as 'Product', UnitPrice as 'Price', UnitsInStock, UnitPrice * UnitsInStock as 'ValueInStock'
FROM Products
WHERE UnitsInStock IN (0, 10, 20)
ORDER BY 3 DESC, 1 ASC;

--9
SELECT upper(ProductName) as 'Product', UnitPrice as 'Price', UnitsInStock, UnitPrice * UnitsInStock as 'ValueInStock'
FROM Products
WHERE UnitsInStock BETWEEN 10 AND 20
ORDER BY 3 DESC, 1 ASC;

--10
SELECT CompanyName, ContactName, Country, City, Fax
FROM Suppliers;

--11
SELECT CompanyName, ContactName, Country, City, Fax
FROM Suppliers
WHERE Country = 'USA';

--12
SELECT CompanyName, ContactName, Country, City, Fax
FROM Suppliers
WHERE Country = 'USA' AND Fax IS NULL;

--13
SELECT CompanyName, ContactName, Country, City, Fax
FROM Suppliers
WHERE upper(Country) like 'S%';

--14
SELECT CompanyName, ContactName, Country, City, Fax
FROM Suppliers
WHERE lower(Country) like '%a';

--15
SELECT CompanyName, ContactName, Country, City, Fax
FROM Suppliers
WHERE lower(Country) like '%an%';

--16
SELECT CompanyName, ContactName, Country, City, Fax
FROM Suppliers
WHERE lower(Country) like '__an%';

--17
SELECT CompanyName, Country, City
FROM Customers
WHERE lower(Country) like '%land';

--18
SELECT TitleOfCourtesy, FirstName, LastName, BirthDate
FROM Employees;

--19
SELECT TitleOfCourtesy || ' ' || FirstName || ' ' || LastName as 'Emp', BirthDate
FROM Employees;

--20
SELECT TitleOfCourtesy || ' ' || FirstName || ' ' || LastName as 'Emp', BirthDate
FROM Employees
ORDER BY 2 DESC;

--21
SELECT TitleOfCourtesy || ' ' || FirstName || ' ' || LastName as 'Emp', BirthDate
FROM Employees
WHERE BirthDate like '1995%'
ORDER BY 2 ASC;

--22
SELECT TitleOfCourtesy || ' ' || FirstName || ' ' || LastName as 'Emp', BirthDate
FROM Employees
WHERE BirthDate like '_____01%'
ORDER BY 2 ASC;

--23
SELECT ProductName, CompanyName as 'SupplierCompanyname'
FROM Products
NATURAL JOIN Suppliers;

--24
SELECT ProductName, CompanyName as 'SupplierCompanyname', CategoryName
FROM Products
NATURAL JOIN Suppliers
NATURAL JOIN Categories;

--25
SELECT OrderId, OrderDate, ShipName as 'Customer', TitleOfCourtesy || ' ' || FirstName || ' ' || LastName as 'Employee', s.CompanyName as 'Shipper'
FROM Orders 'o'
JOIN Customers 'c' ON o.CustomerId = c.CustomerId
JOIN Employees 'e' ON o.EmployeeId = e.EmployeeId
JOIN Shippers 's' ON o.ShipVia =  s.ShipperID;

--26
SELECT count(ProductId) 'NoOfProduct', sum(UnitPrice) 'SumOfUnitprice', max(UnitPrice) 'MaxOfUnitprice', min(UnitPrice) 'MinOfUnitprice', avg(UnitPrice) 'AverageOfUnitprice'
FROM Products;

--27
SELECT CategoryName, count(ProductId) 'NoOfProduct'
FROM Products
NATURAL JOIN Categories
GROUP BY CategoryId;

--28
SELECT CategoryName, count(ProductId) 'NoOfProduct'
FROM Products
NATURAL JOIN Categories
GROUP BY CategoryId
ORDER BY 2 DESC;

--29
SELECT CategoryName, count(ProductId) 'NoOfProduct'
FROM Products
NATURAL JOIN Categories
GROUP BY CategoryId
HAVING NoOfProduct < 10
ORDER BY 2 DESC;

--30
INSERT INTO Categories (CategoryName, Description)
VALUES ('catname1', NULL), 
	   ('catname2', 'des2');

--31
UPDATE Categories
SET Description = 'update des3'
WHERE CategoryId = 10; 

--32
DELETE FROM Categories
WHERE CategoryId = 10; 
