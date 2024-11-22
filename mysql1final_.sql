
create database project;
use project;

create table customers(
name varchar(20) not null,
phone bigint(10),
email varchar(50) not null);

create table employee(
employee_id int(5) primary key not null auto_increment,
employee_name varchar(20) not null,
phone_number bigint(10) not null,
email varchar(50) not null,
salary integer default 0,
designation varchar(10) not null
);

create table items(
item_id int(11) primary key auto_increment,
 item_name varchar(50) not null, 
 price int(10) not null,
 unit varchar(10),
 current_stock int(11) default 0
 );
 create table login(
 employee_id int(8) primary key auto_increment,
 uname varchar(20)  not null,
 password varchar(20) not null,
 designation char(10) not null
 ); 
create table purchase(
order_id int(11) not null primary key,
cust_name varchar(20) not null,
phone bigint(10),
date date not null,
reference varchar(50) not null
);
create table tempac(
namet varchar(50),
email varchar(50),
phno bigint(10),
passw varchar(50),
desig varchar(50),
skey varchar(6));

create table tempbill(
SNo varchar(20),
Item varchar(50),
Quantity varchar(10),
Price varchar(10),
Net_Amount varchar(10));
use project;
select * from tempac;
show tables;
select * from employee;
select * from customers;