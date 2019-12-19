import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)

mycursor = mydb.cursor()

# where
sql = "SELECT * FROM customers WHERE address='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# Wildcard Characters
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# Prevent SQL Injection
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)