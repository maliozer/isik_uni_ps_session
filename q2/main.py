#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: github.com/maliozer
@license: MIT
"""


#mysql connection problem from python
'''
sudo mysql

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';

'''

### use this -> !pip install mysql-connector
import mysql.connector

#define host, root,passwd,database inline
def mysql_connector():
    db_con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
    )
    return db_con

mysql_con = mysql_connector()

mysql_cursor = mysql_con.cursor()

mysql_cursor.execute("CREATE DATABASE example1")
mysql_con.database = 'example1'

#%%
mysql_cursor.execute("CREATE TABLE Exam (StudentID VARCHAR(11), CourseID VARCHAR(11), Grade INT)")
#%%

sql = "INSERT INTO Exam (StudentID, CourseID, Grade) VALUES (%s, %s, %s)"
val = ("ALi", "Özer", "77")
mysql_cursor.execute(sql, val)
mysql_con.commit()
print(mysql_cursor.rowcount, "record inserted.")

#%%
#show results
mysql_cursor.execute("SELECT * FROM Exam")
myresult = mysql_cursor.fetchall()

for x in myresult:
  print(x)