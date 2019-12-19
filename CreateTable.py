import mysql.connector

# connection
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythondb")

# create a table
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# show all table
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)