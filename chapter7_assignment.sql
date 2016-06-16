--question 1 start
select *
into VendorCopy
from Vendors

select *
into InvoiceCopy
from Invoices
--question 1 end

--question 2 start
insert into InvoiceCopy
	(VendorID
	,InvoiceTotal
	,TermsID
	,InvoiceNumber
	,PaymentTotal
	,InvoiceDueDate
	,InvoiceDate
	,CreditTotal
	,PaymentDate)
values
	(
	32
	,434.58
	,2
	,'AX-014-027'
	,0.00
	,'07-8-12'
	,'6-21-12'
	,0.00
	,null
	)
--question 2 end

--question 3 start
insert into VendorCopy
	
select VendorName, VendorAddress1, VendorAddress2, VendorCity, VendorState, VendorZipCode
		,VendorPhone, VendorContactLName, VendorContactFName, DefaultTermsID, DefaultAccountNo
from VendorCopy
where VendorState not in ('CA')
--question 3 end

--question 4 start
update VendorCopy
set DefaultAccountNo = 403
from VendorCopy
where DefaultAccountNo = 400
--question 4 end

--question 5 start
--update InvoiceCopy
--set PaymentDate = GETDATE(),
--	PaymentTotal = 'BalanceDue'
--from InvoiceCopy
--where PaymentTotal > 0
--question 5 end?
 
 --question 6 start
 update InvoiceCopy
 set TermsID = 2
where VendorID in
	(select VendorID
	from VendorCopy
	where DefaultTermsID = 2)
--question 6 end

--question 7 start
update InvoiceCopy
 set TermsID = 2
 from InvoiceCopy
	,VendorCopy
where DefaultTermsID = 2
--question 7 end

--question 8 start
delete from VendorCopy
from VendorCopy
where VendorState = 'Minnesota'
--question 8 end

--question 9 start
--delete from VendorCopy
--from
--	(select distinct VendorState 
--	from VendorCopy
--	where VendorState = null)
--question 9 end

	
