--Question 1 start
select officeLocation
from Offices
--End?

--Question 2 start
select*
from Offices
order by country, state, city
--End

--Question 3 start
select employeeNumber
		,firstName
		,lastName
from Employees join Offices
	on Employees.officeCode =
	Offices.officeCode
where officeLocation = 'Sydney'
--end?

--Question 4 start
select customerName =
		lastName, firstName
from Customers as [C] join Employees as [E]
	on C.salesRepEmployeeNumber =
	E.employeeNumber
--end

--Question 5 start
select productName
from Products

--end?

--Question 6 start
select Products.productCode
		,productName
		,orderNumber
from Products join OrderDetails
	on OrderDetails.productCode =
	Products.productCode
where orderNumber = null
--end

--Question 7 start
select orderNumber
		,orderDate
		,status
		,comments
from Orders
where shippedDate between 'June 01, 2003' and 'April 01, 2004'
order by orderDate desc
--end

