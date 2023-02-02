#create tables inside database

import mysql.connector

db_connector = mysql.connector.connect(host="localhost",user="root",password="root1234",db="newdatabase2")
db_cursor = db_connector.cursor()

#db_cursor.execute("create table stud_details(roll_no int,name varchar(20))")
#db_cursor.execute("create table teacher_details(teacher_id int,name varchar(20))")

"""
if tables already created...
"""
db_cursor.execute("show tables")
for i in db_cursor:
    print(i)
print()

db_cursor.execute("desc stud_details")
for i in db_cursor:
    print(i)
print()

db_cursor.execute("desc teacher_details")
for i in db_cursor:
    print(i)

db_connector.close()
