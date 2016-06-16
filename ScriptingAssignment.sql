use master 

drop database Membership
go

create database Membership
go

use Membership
go

create table Individuals
(
	IndividualID int identity primary key
	,FirstName varchar(50) not null
	,LastName varchar(50) not null
	,Address varchar(50) not null
	,Phone varchar(10) not null
)

create table GroupMembership 
(
	GroupID int references Groups(GroupID) not null
	,IndividualID int references Individuals(IndividualID)
	
)

create table Groups
(
	GroupID int identity primary key not null
	,GroupName varchar(50) not null
	,Dues money not null
)

create clustered index IX_GroupID
	on GroupMembership(GroupID)

create nonclustered index IX_IndividualID
	on GroupMembership(IndividualID)

alter table Individuals
	add DuesPaid money not null
	


use AP
go

alter table Invoices 
	add check (PaymentTotal = 0)
	alter column PaymentDate smalldatetime  null

alter table Invoices 
	add check (PaymentTotal > 0)
	alter column PaymentDate smalldatetime not null


	
	





