select *
from Invoices
where VendorID = 123

select InvoiceNumber
		,VendorName
from Invoices join Vendors
	on Invoices.VendorID = 
	Vendors.VendorID

select *
from Vendors 
		join Invoices
		on Vendors.VendorID 
		= Invoices.VendorID



