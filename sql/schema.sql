CREATE TABLE "Categories"(
	category_id INTEGER PRIMARY KEY,
	category_name TEXT);
	
SELECT * FROM "Categories";
-- INSERT INTO "Categories" IF NOT EXISTS (category_name)VALUES("electronics"), ("clothing"), ("music");
-- DELETE FROM Categories;

CREATE TABLE "Products"(
	product_id INTEGER PRIMARY KEY,
	product_name TEXT NOT NULL,
	category_id INTEGER,
	Supplier_id INTEGER,
	price DECIMAL(10, 2) NOT NULL,
	
	FOREIGN KEY (category_id)
		REFERENCES Categories(category_id)
	

	FOREIGN KEY (Supplier_id)
		REFERENCES Suppliers(supplier_id)

	);
	
-- SELECT*FROM "Products";
-- INSERT INTO "Products" (product_id, product_name, category_id, Supplier_id, price) VALUES (123, "shampoo", 1, 123, 1.1);

CREATE TABLE "Suppliers" (
	supplier_id INTEGER PRIMARY KEY,
	supplier_name TEXT NOT NULL,
	email TEXT UNIQUE
	);

