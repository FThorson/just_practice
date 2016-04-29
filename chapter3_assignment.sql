--Start number 1
select VendorContactFName
		,VendorContactLName
		,VendorName
from Vendors
order by VendorContactLName
		,VendorContactFName
--End number 1

--Start number 2
select InvoiceNumber as [Number]
		,InvoiceTotal as [Total]
		,PaymentTotal +
		CreditTotal as [Credits]
		,InvoiceTotal -
		PaymentTotal as [Balance]
from Invoices
--End number 2

--Start number 3
select VendorContactLName
		+','
		+ VendorContactFName as [Full Name]
from Vendors
order by VendorContactLName
		 ,VendorContactFName
--End number 3

--Start number 4
select InvoiceTotal
		,InvoiceTotal
		*
		.1 as [Percentage]
		,InvoiceTotal 
		+
		.1 as [Total Percentage]
from Invoices
order by InvoiceTotal desc
--End number 4

--Start number 5
select InvoiceNumber as [Number]
		,InvoiceTotal as [Total]
		,PaymentTotal +
		CreditTotal as [Credits]
		,InvoiceTotal -
		PaymentTotal as [Balance]
from Invoices
where InvoiceTotal
      >=
	  500
	  or
	  InvoiceTotal
	  <= 10000
--End number 5

--Start number 6
select VendorContactLName
from Vendors
where Left (VendorContactLName, 1) = 'A'
		or
		 Left (VendorContactLName, 1) = 'B'
		 or
		 Left (VendorContactLName, 1) = 'C'
		 or
		 Left (VendorContactLName, 1) = 'E'
--End number 6

--Start number 7
select PaymentDate
from Invoices
where PaymentDate is null
--End number 7??

