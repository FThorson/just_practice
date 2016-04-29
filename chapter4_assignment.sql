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




