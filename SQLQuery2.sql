select invoiceNumber as [Invoice #]
	,InvoiceTotal -
	  PaymentTotal -
	  CreditTotal as Balance
from Invoices

select VendorContactFName
		+' '
		+ VendorContactLName as [Full Name]
from Vendors
order by VendorContactLName
		 ,VendorContactFName

select VendorCity
		,VendorState
		,VendorCity
		+ ', ' 
		+VendorState as [City, State]
from Vendors

print 10 % 3

print 3 * 3

print 4 + 5

print 7 - 3

print 9 / 3 

select LEFT (vendorcontactfname, 1)
		+
		+ ', '
		+
		LEFT (vendorcontactlname, 1)
from Vendors
where  LEFT (vendorcontactfname, 1) ='s'

select  VendorState
from Vendors
order by VendorState

select distinct VendorName
				,VendorState
from Vendors
order by VendorState
			,VendorName