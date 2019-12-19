import mysql.connector

# connection
mydb = mysql.connector.connect(host="localhost", user="root", passwd="")

# create a db
mycursor = mydb.cursor()

# cursor.execute("CREATE DATABASE pythondb")
mycursor.execute("CREATE DATABASE IF NOT EXISTS pythondb")

# show all db
mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)