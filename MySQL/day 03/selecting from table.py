##import mysql.connector
##
##db_connector  = mysql.connector.connect(
##    host = "localhost",
##    user = "root",
##    password = "root1234",
##    db = "newdatabase2")
##db_cursor = db_connector.cursor()
##
##db_cursor.execute("select name,salary from emp_details where salary >1000")
##
##db_connector.commit()
##db_connector.close()
##

import mysql.connector

db_connector  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root1234",
    db = "newdatabase2")
db_cursor = db_connector.cursor()

db_cursor.update("update emp_details set salary=50000 where emp_id=101")
db_cursor.execute("select name,salary from emp_details where salary >40000")

db_connector.commit()
db_connector.close()

