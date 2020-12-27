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

def createUser(userID, passwords):
    query = """
        INSERT INTO users(username, password)
        VALUES('""" + userID + "','" + passwords + "')"
    cursor.execute(query)
    mydb.commit()

def deleteUser(userID):
    query = """
        DELETE FROM users
        WHERE username = '""" + userID + "'"
    cursor.execute(query)
    mydb.commit()

def updateUser(UserID, newPassword):
    query = """
        UPDATE users
        SET 
            password = '""" + newPassword + "'" + """
        WHERE username = '""" + UserID + "'"
    print(query)
    cursor.execute(query)
    mydb.commit()
        




"""
build function : login, store user password mysql
build git branch, commit, push
"""
