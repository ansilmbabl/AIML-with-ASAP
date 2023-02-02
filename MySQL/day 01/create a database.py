#create a database

import mysql.connector

db_connector = mysql.connector.connect(host="localhost",user="root",password="root1234")
db_cursor = db_connector.cursor()
db_cursor.execute("create database newdatabase2")
db_connector.close()
