# PostgreSQL, Designed to store and work with user accounts
import psycopg2
from psycopg2 import OperationalError, DatabaseError
from config import USERS_DB_CONFIG

connection = None
cursor = None

def connectToUsersDB():
    global connection, cursor
    
    try:
        connection = psycopg2.connect(**USERS_DB_CONFIG)
        cursor = connection.cursor()
        return True
    except OperationalError as e:
        print(f"Connection error to DataBase: {e}")
        return False
def closeUsersDB():
    global connection, cursor
    
    if cursor:
        cursor.close()
    
    if connection:
        connection.close()
    
    connection = None
    cursor = None

def checkUserCredentials(login, password):
    connectToUsersDB()
    if not connection or connection.closed:
        print("There is no active connection to the database")
        return False
    
    try:
        query = """
        SELECT EXISTS(
            SELECT 1 FROM users 
            WHERE users_login = %s AND users_password = %s
        )
        """
        cursor.execute(query, (login, password))
        return cursor.fetchone()[0]
    except DatabaseError as e:
        print(f"Error while checking data: {e}")
        return False
    finally:
        closeUsersDB()
