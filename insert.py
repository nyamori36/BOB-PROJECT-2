import sqlite3

conn = sqlite3.connect('example.db')
print("opened database successfully")

conn.execute("INSERT INTO COMPANY111(ID,NAME, AGE ,ADDRESS,SALARY)\
                VALUES(1,'GOOGLE',7,'WESTLANDS',2500.00)");

conn.execute("INSERT INTO COMPANY111(ID,NAME, AGE ,ADDRESS,SALARY)\
                VALUES(2,'CHROME',7,'WESTLANDS',2500.00)");

conn.execute("INSERT INTO COMPANY111(ID,NAME, AGE ,ADDRESS,SALARY)\
                VALUES(3,'EDGE',7,'WESTLANDS',2500.00)");

conn.close("INSERT INTO COMPANY111(ID,NAME, AGE ,ADDRESS,SALARY)\
                VALUES(4,'FIREFOX',7,'WESTLANDS',2500.00)");

conn.commit()
print("Records created successfully")
conn.close()