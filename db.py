import mysql.connector

mydb = mysql.connector.connect(
  host="anugerahpratamadb.cfdze5qbk9tk.ap-southeast-1.rds.amazonaws.com",
  user="wesleyburnawan",
  password="Basketball55$",
  port = 3306,
  db = "anugerah_pratama"
)

cursor = mydb.cursor()

def createUserTable():
    query = """
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(100) NOT NULL PRIMARY KEY, 
            password TEXT NOT NULL
        ) 
        """
    cursor.execute(query)

def deleteUserTable():
    query = "DROP TABLE users"
    cursor.execute(query) 

"""
build function :createUser, deleteUser, updateUser, login, 
store user password mysql
build git branch, commit, push
"""
