import sqlite3

conn = sqlite3.connect('example.db')
print("opened database successfully")

conn.execute("UPDATE COMPANY7 set SALARY = 12500.00 where ID = 1")
conn.commit()


cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY111 ")
for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("ADDRESS=", row[3])
    print("SALARY =", row[4])

print("operation done successfully")
conn.close()
