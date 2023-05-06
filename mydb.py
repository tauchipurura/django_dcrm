# install Mysql on your computer
#pip install mysql
#pip install mysql-connector-python
#

import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = 'h1213034k'
)

#prepare a cursor object

cursorObject = dataBase.cursor()

#Create a database

cursorObject.execute("CREATE DATABASE tau")

print("All Done!")