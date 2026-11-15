import sqlite3

connection = sqlite3.connect("inventory.db")

_ = connection.execute("PRAGMA foreign_keys = ON")

with open("sql/schema.sql", "r") as file:
    sql_schema = file.read()

_ = connection.executescript(sql_schema)

connection.commit()
connection.close()

print("DATABASE CREATED SUCCESSFULLY!")
