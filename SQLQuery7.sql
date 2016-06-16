select count(InvoiceNumber) as NumInv
		,SUM(InvoiceTotal) as TotBal
from Invoices
where InvoiceTotal -
		PaymentTotal -
		CreditTotal > 0

select 'After 9/1/2011' as SelDate
		,count(*) as NumInv
		,AVG(InvoiceTotal) as AvInv
		,sum(InvoiceTotal) as Total
		,MIN(InvoiceTotal) as LowInv
		,MAX(InvoiceTotal) as MaxInv 
from Invoices
where InvoiceDate > '9/1/2011'
