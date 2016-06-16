--Sorry Joe, this is incomplete. I have been having a rough couple of weeks.
--This is not my best work. I will do better from now on. 


--Question 1 start
select *
from Vendors join
	Invoices
	on Vendors.VendorID = Invoices.VendorID
--Question 1 end

--Question 2 start
select VendorName
		,InvoiceNumber
		,InvoiceDate
		,InvoiceTotal -
		 PaymentTotal +
		CreditTotal as Total
from Vendors join Invoices
	on Vendors.VendorID = 
	Invoices.VendorID
where InvoiceTotal > 0
--Question 2 end?


--Question 3 start
select VendorName
		,DefaultAccountNo
		,AccountDescription
from Vendors join GLAccounts
		on Vendors.DefaultAccountNo =
		GLAccounts.AccountNo
order by AccountDescription
		,VendorName
--Question 3 end

--Question 4 start

--Question 4 end

--Question 5 start
select VendorName as Vendor
		,InvoiceDate as Date
		,InvoiceNumber as Number
		,InvoiceSequence as #
		,InvoiceLineItemAmount as LineItem
from Vendors as [v] join
	Invoices as [i] 
	on v.VendorID = i.VendorID join
	InvoiceLineItems as [il]
	on il.InvoiceID = i.InvoiceID
order by Vendor
		,Date
		,Number
		,#
--Question 5 end

--Question 6 start
select VendorID
		,VendorName
		,VendorContactFName + ',' 
		 + ' ' + VendorContactLName as [Name]
from Vendors
--Question 6 end

--Question 7 start
select AccountDescription, GLAccounts.AccountNo
from GLAccounts left outer join InvoiceLineItems
		on GLAccounts.AccountNo 
		= InvoiceLineItems.AccountNo
--Question 7 end




