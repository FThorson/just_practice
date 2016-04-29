--AP Database
select distinct VendorName
from Vendors join Invoices
	on Vendors.VendorID =
	Invoices.VendorID
where VendorState = 'CA'
order by VendorName desc

select AccountDescription
from GLAccounts left outer join InvoiceLineItems
	on GLAccounts.AccountNo =
	InvoiceLineItems.AccountNo
where InvoiceLineItems.AccountNo is null

	select InvoiceNumber
			,InvoiceTotal - 
			PaymentTotal -
			CreditTotal as Balance
			,'Pay Me Now!' as [Paid?]
	from Invoices
	where InvoiceTotal - 
		PaymentTotal -
		CreditTotal > 0
union
	select InvoiceNumber
			,InvoiceTotal - 
			PaymentTotal -
			CreditTotal as Balance
			,'Your All Paid Up.' as [Paid?]
	from Invoices
	where InvoiceTotal - 
		PaymentTotal -
		CreditTotal = 0

--Examples Database
	select CustomerFirst
			,CustomerLast
	from Customers
intersect
	select FirstName
			,LastName
	from Employees
	order by CustomerLast, CustomerFirst

	select CustomerFirst
			,CustomerLast
	from Customers
except
	select FirstName
			,LastName
	from Employees
	order by CustomerLast, CustomerFirst






