select InvoiceNumber, InvoiceDate, invoiceTotal
from invoices
where InvoiceID between 1 and 10 / 2 + 3 * 6 - 13
order by InvoiceNumber
