import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="timmy12345"
)

print(mydb)