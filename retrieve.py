import sqlite3

conn = sqlite3.connect('example.db')
print("opened database successfully")

cursor = conn.execute("SELECT id,name,address,salary from company111")

for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("ADDRESS=", row[3])
    print("SALARY =", row[4])

print("operation done successfully")
conn.close()
