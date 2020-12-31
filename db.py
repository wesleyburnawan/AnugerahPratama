import mysql.connector
from . import config 

mydb = mysql.connector.connect(
  host="anugerahpratamadb.cfdze5qbk9tk.ap-southeast-1.rds.amazonaws.com",
  user="wesleyburnawan",
  password = config.dbPassword,
  port = 3306,
  db = "anugerah_pratama",
  autocommit = True
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

def createUser(userID, password):
    query = """
        INSERT INTO users(username, password)
        VALUES(%(username)s, %(password)s)
        """
    userInfo = {
        "username": userID, 
        "password": password
    }
    cursor.execute(query, userInfo)

def deleteUser(userID):
    query = """
        DELETE FROM users
        WHERE username = %(username)s
        """
    userInfo = {
        "username": userID
    }
    cursor.execute(query, userInfo)

def updateUser(oldUserID, newUserID, newPassword):
    query = """
        UPDATE users
        SET 
            password = %(newPassword)s,
            username = %(newUserID)s
        WHERE username = %(oldUserID)s
        """
    userInfo = {
        "newPassword": newPassword,
        "newUserID": newUserID,
        "oldUserID": oldUserID
    }
    cursor.execute(query, userInfo)
        
def login(userID): 
    query = """
        SELECT password FROM users 
        WHERE
            username = %(username)s
        """
    userInfo = {
        "username": userID
    }
    cursor.execute(query, userInfo)
    return cursor.fetchone()
