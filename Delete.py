import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)

mycursor = mydb.cursor()

# Delete Record
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)


# Prevent SQL Injection
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
