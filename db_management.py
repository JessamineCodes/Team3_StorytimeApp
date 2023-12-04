from mysql.connector import connect, Error
from config import DB_NAME, DB_HOST, DB_USER, DB_PASS

class DbConnectionError(Exception):
    pass 

def get_db_connection():
    try:
        with connect(
            host=DB_HOST, 
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        ) as connection:
            print(f"Connected to DB: {DB_NAME}")
            return connection

    except Error as err:
        raise(DbConnectionError(f"Failed to connect to the database: {err}"))

get_db_connection()