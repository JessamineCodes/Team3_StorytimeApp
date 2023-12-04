from db_management import get_db_connection, DBConnectionError
from pprint import pprint

def add_user(username, email, password):
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}')")
                connection.commit()
                print(f"User {username} added to the database.")
    except DBConnectionError as err:
        print(err)


