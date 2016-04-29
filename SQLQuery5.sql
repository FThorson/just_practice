select VendorName
		,InvoiceNumber
		,InvoiceID
from Vendors left outer join Invoices
	on Vendors.VendorID = 
	Invoices.VendorID
where InvoiceNumber is not null
order by VendorName








