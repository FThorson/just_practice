select *
into InvoiceCopy --Made up name for the copy
from Invoices

select *
into VendorCopy
from Vendors
-- Use "drop" to remove a table
--drop table InvoiceCopy
-- Use "delete" to remove only the data from a table 
--delete VendorCopy 

insert Invoices
		values
		(
		97,--VendorID
		'39',--InvNum
		GETDATE(), --InvDate
		375.75, --InvTotal
		245.85, --PayTotal
		130.56, --CreditTotal
		3, --TermsID
		GETDATE() + 90, --InvDueDate
		null --PayDate
		)