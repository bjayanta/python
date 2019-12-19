import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# fetch only name
mycursor.execute("SELECT name FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)