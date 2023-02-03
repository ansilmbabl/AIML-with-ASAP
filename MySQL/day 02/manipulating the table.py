#inserting single row of data

##import mysql.connector
##
##db_connector  = mysql.connector.connect(
##    host = "localhost",
##    user = "root",
##    password = "root1234",
##    db = "newdatabase2")
##db_cursor = db_connector.cursor()
##db_cursor.execute("insert into stud_details(roll_no,name) values(101,'Abc')")
###db_cursor.execute("select * from stud_details")
##db_connector.commit()
##db_connector.close()


##import mysql.connector
##
##db_connector  = mysql.connector.connect(
##    host = "localhost",
##    user = "root",
##    password = "root1234",
##    db = "newdatabase2")
##db_cursor = db_connector.cursor()
###db_cursor.execute("insert into stud_details(roll_no,name) values(101,'Abc')")
##stmnt = ("insert into stud_details(roll_no,name)"
##         "values(%s,%s)")
##val = (102,"Xyz")
##db_cursor.execute(stmnt,val)
##db_connector.commit()
##db_connector.close()

##import mysql.connector
##
##db_connector  = mysql.connector.connect(
##    host = "localhost",
##    user = "root",
##    password = "root1234",
##    db = "newdatabase2")
##db_cursor = db_connector.cursor()
###db_cursor.execute("insert into stud_details(roll_no,name) values(101,'Abc')")
##stmnt = ("insert into stud_details(roll_no,name)"
##         "values(%s,%s)")
##val = [(103,"Pqr"),(105,"Xcv"),(106,"Vbd")]
##db_cursor.executemany(stmnt,val)
##db_connector.commit()
##db_connector.close()

##import mysql.connector
##
##db_connector  = mysql.connector.connect(
##    host = "localhost",
##    user = "root",
##    password = "root1234",
##    db = "newdatabase2")
##db_cursor = db_connector.cursor()
###db_cursor.execute("insert into stud_details(roll_no,name) values(101,'Abc')")
##roll_no = int(input("Roll number: "))
##name = input("name: ")
##db_cursor.execute("insert into stud_details(roll_no,name) values({},'{}')".format(roll_no,name))
####db_cursor.execute("select * from stud_details")
##db_connector.commit()
##db_connector.close()

##unique value (id)

##import mysql.connector
##
##db_connector  = mysql.connector.connect(
##    host = "localhost",
##    user = "root",
##    password = "root1234",
##    db = "newdatabase2")
##db_cursor = db_connector.cursor()
###primary key
##db_cursor.execute("create table emp_details(emp_id int primary key, name varchar(40) not null, salary int)")
##
##db_connector.commit()
##db_connector.close()


# inserting values

##import mysql.connector
##
##db_connector  = mysql.connector.connect(
##    host = "localhost",
##    user = "root",
##    password = "root1234",
##    db = "newdatabase2")
##db_cursor = db_connector.cursor()
###primary key
###db_cursor.execute("create table emp_details(emp_id int primary key, name varchar(40) not null, salary int)")
##
##try:
##    stmnt = ("insert into emp_details(emp_id,name,salary)"
##             "values(%s,%s,%s)")
##    val = [(101,"Akhash",30000),
##           (102,"Sumesh",35000),
##           (103,"Ananya",40000)]
##    db_cursor.executemany(stmnt,val)
##except Exception as e:
##    print(e)
### db_cursor.execute("select * from emp_details")
##db_connector.commit()
##db_connector.close()

# alter table

##import mysql.connector
##
##db_connector  = mysql.connector.connect(
##    host = "localhost",
##    user = "root",
##    password = "root1234",
##    db = "newdatabase2")
##db_cursor = db_connector.cursor()
###primary key
###db_cursor.execute("create table emp_details(emp_id int primary key, name varchar(40) not null, salary int)")
##db_cursor.execute("ALTER TABLE teacher_details modify teacher_id int primary key")
##
### db_cursor.execute("select * from emp_details")
##db_connector.commit()
##db_connector.close()

# deleting from table

import mysql.connector

db_connector  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root1234",
    db = "newdatabase2")
db_cursor = db_connector.cursor()
#primary key
#db_cursor.execute("create table emp_details(emp_id int primary key, name varchar(40) not null, salary int)")
db_cursor.execute("delete from stud_details where roll_no = 101")

# db_cursor.execute("select * from emp_details")
db_connector.commit()
db_connector.close()
