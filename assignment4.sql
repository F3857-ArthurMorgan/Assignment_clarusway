--RDB&SQL Assignment-4

/*
Charlie's Chocolate Factory company produces chocolates. The following product information is stored: product name, product ID, and quantity on hand. These chocolates are made up of many components. Each component can be supplied by one or more suppliers. The following component information is kept: component ID, name, description, quantity on hand, suppliers who supply them, when and how much they supplied, and products in which they are used. On the other hand following supplier information is stored: supplier ID, name, and activation status.
Assumptions
A supplier can exist without providing components.
A component does not have to be associated with a supplier. It may already have been in the inventory.
A component does not have to be associated with a product. Not all components are used in products.
A product cannot exist without components. 
Do the following exercises, using the data model.
     a) Create a database named "Manufacturer"
     b) Create the tables in the database.
     c) Define table constraints.
*/

CREATE DATABASE Manufacturer
USE Manufacturer
CREATE SCHEMA ccf


CREATE TABLE ccf.Product(
	prod_id INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
	prod_name VARCHAR(50) NULL,
	quantity INT NOT NULL);


CREATE TABLE ccf.Component(
	comp_id INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
	comp_name VARCHAR(50) NOT NULL,
	descript VARCHAR(50) NOT NULL,
	quantity_comp INT NOT NULL);


CREATE TABLE ccf.Supplier(
	supp_id INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
	supp_name VARCHAR(50) NOT NULL,
	supp_location VARCHAR(50) NOT NULL,
	supp_country VARCHAR(50) NOT NULL,
	is_active BIT NOT NULL);


CREATE TABLE ccf.Prod_Comp(
	CONSTRAINT FK_key1 FOREIGN KEY (prod_id) REFERENCES ccf.Product,
	prod_id INT NOT NULL,
	CONSTRAINT FK_key2 FOREIGN KEY (comp_id) REFERENCES ccf.Component,
	comp_id INT NOT NULL,
	quantity_comp INT NOT NULL);


CREATE TABLE ccf.Comp_Supp(
	CONSTRAINT FK_key3 FOREIGN KEY (supp_id) REFERENCES ccf.Supplier,
	supp_id INT NOT NULL,
	CONSTRAINT FK_key4 FOREIGN KEY (comp_id) REFERENCES ccf.Component,
	comp_id INT NOT NULL,
	order_date DATE NOT NULL,
	quantity INT NOT NULL);

