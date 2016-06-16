select VendorName
		,AVG(InvoiceTotal) as [AvgInvTotal]
from Invoices join Vendors
     on Invoices.VendorID 
	 = Vendors.VendorID
group by Vendors.VendorID
		, VendorName  
having AVG(InvoiceTotal) > 10000
order by AvgInvTotal desc

select VendorState, count(*) as [NumInv]
from Invoices join Vendors
		on Invoices.VendorID
		= Vendors.VendorID
group by VendorState

select VendorState as [State]
		,VendorCity as [City]
		,count(*) as [NumInv]
from Invoices join Vendors
		on Invoices.VendorID
		= Vendors.VendorID
group by VendorCity, VendorState
order by VendorState, VendorCity

select InvoiceDate 
		,Count(*) as [NumInv]
		,SUM(InvoiceTotal) as [InvSum]
from Invoices
group by InvoiceDate
having InvoiceDate between 'Jan 01, 2012'
		and 'Jan 31, 2012'
order by InvoiceDate desc














