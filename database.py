import sqlite3

conn = sqlite3.connect('example.db')
print("opened database successfully")

# creating a table
conn.execute('''CREATE TABLE COMPANY111(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL, 
AGE INT NOT NULL, 
ADRESS CHAR(50),
SALARY REAL);''')


print("Table created successfully")
conn.close()