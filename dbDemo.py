import mysql.connector
from utilities.configurations import *

# connect Mysql with parameters: host, database, user, password
# conn = mysql.connector.connect(host='localhost', database='APIDevelop',
#                                user='testUser', password='Abcd123@')

# Call getSqlConnection method from external file configurations.py
conn = getSQLConnection()
print("Connected Status?: ", conn.is_connected())

# Executing queries
cursorObj = conn.cursor()
cursorObj.execute('select * from CustomerInfo')

# fetchone gets only first row from db
# row = cursorObj.fetchone()
# print("first row from table CustomerInfo: ",row)
# print("print out index[3] from first row: ", row[3])

# fetchall start from second row as fetchone was done before
rowAll = cursorObj.fetchall()
count = 0
for r in rowAll:
    count += 1
    print("Row",count, r)

# Iterate thru row list and sum up amount in column 3 (index[2]
total = 0
for r in rowAll:
    total += r[2]
print("Total amount: ", total)

assert total == 340

# Update db from python: give a query, data > use method execute(), then commit()
# query1 = 'update customerInfo set Location = %s where CourseName = %s'
# data1 = ("VN", "Jmeter")
# cursorObj.execute(query1, data1)
# conn.commit()

# query2 = 'insert into CustomerInfo values("WebServices",CURRENT_DATE(),21,"Asia")'
# cursorObj.execute(query2)
# conn.commit()

# query3 = 'delete from customerInfo where courseName = "WebServices"'
# cursorObj.execute(query3)
# conn.commit()

