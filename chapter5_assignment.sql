-- Question 1 start
select Vendors.VendorID
		,SUM(PaymentTotal) as PaymentSum
from Invoices join Vendors 
		on Invoices.VendorID 
		= Vendors.VendorID
group by Vendors.VendorID
order by Vendors.VendorID
--Question 1 end

--Question 2 start
select top 10  SUM(PaymentTotal) as PaymentSum
			,Vendors.VendorName
from Vendors join Invoices
		on Invoices.VendorID
		= Vendors.VendorID
group by Vendors.VendorName
order by Vendors.VendorName
--Question 2 end

--Question 3 start
select Vendors.VendorName
		,SUM(InvoiceTotal) as [InvoiceSum]
		,COUNT(InvoiceNumber)
from Vendors join Invoices
	on Vendors.VendorName
	= Invoices.VendorID
group by Vendors.VendorName
--Question 3 end?

--Question 4 start
select GLAccounts.AccountDescription
		,COUNT(InvoiceLineItemAmount) as [LineItemCount]
		,SUM(InvoiceLineItemAmount) as [InvoiceLineSum]
from GLAccounts join InvoiceLineItems
	on InvoiceLineItems.AccountNo
	= GLAccounts.AccountNo
where InvoiceLineItemAmount > 1
group by GLAccounts.AccountDescription
order by LineItemCount desc
--Question 4 end

--Question 5 start
select GLAccounts.AccountNo
		,Invoices.InvoiceDate
		,COUNT(InvoiceLineItemAmount) as [LineItemCount]
		,SUM(InvoiceLineItemAmount) as [InvoiceLineSum]
from GLAccounts join InvoiceLineItems
	on InvoiceLineItems.AccountNo
	= GLAccounts.AccountNo
	join Invoices on
	Invoices.InvoiceDate =
	GLAccounts.AccountNo
where Invoices.InvoiceDate between '12-1-2011' and '2-29-2012'
group by GLAccounts.AccountNo, Invoices.InvoiceDate
order by LineItemCount desc
--Question 5 end?

--Question 6 start
select SUM (AccountNo) as [Total]
from InvoiceLineItems
group by InvoiceLineItemAmount with rollup
--Question 6 end?

--Question 7 start

--Question 7 end

--Question 8 start		


