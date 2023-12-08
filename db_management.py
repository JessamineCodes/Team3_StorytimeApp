from mysql.connector import connect
from config import DB_HOST, DB_NAME
from dotenv import load_dotenv # dotenv module allows for
import os #


load_dotenv()
def get_connection():
    connection = connect(host=DB_HOST,
                         user= os.getenv('DB_USER'),
                         password=os.getenv('DB_PASS'),
                         database=DB_NAME
                         )
    if connection:
        print('Connected to DB: {}'.format(DB_NAME))

    return connection


class DbConnectionError(Exception):
    pass


def create_user_table():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                create_users_query = """
                    CREATE TABLE IF NOT EXISTS users (
                        UserID INT PRIMARY KEY AUTO_INCREMENT,
                        Username VARCHAR(50),
                        Email VARCHAR(100),
                        PasswordHash VARCHAR(255),
                        DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """
                cursor.execute(create_users_query)
                connection.commit()  # Commit the changes
                print("Table users added to storybook DB")


    except Exception as e:
        print(f"Error occurred: {e}")
        raise DbConnectionError("Failed to add users table to storybook DB")

def create_child_table():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                create_children_query = """
                    CREATE TABLE IF NOT EXISTS child (
                        ChildID INT PRIMARY KEY AUTO_INCREMENT,
                        UserID INT,
                        ChildName VARCHAR(50),
                        Age INT,
                        Pronouns VARCHAR(50),
                        FOREIGN KEY (UserID) REFERENCES users(UserID)
                    )
                """
                cursor.execute(create_children_query)
                connection.commit()  # Commit the changes
                print("Table children added to storybook DB")


    except Exception as e:
        print(f"Error occurred: {e}")
        raise DbConnectionError("Failed to add children table to storybook DB")

def create_stories_table():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                create_stories_query = """
                    CREATE TABLE IF NOT EXISTS stories (
                        StoryID INT PRIMARY KEY AUTO_INCREMENT,
                        Title VARCHAR(100),
                        Content TEXT,
                        DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
                        ChildID INT,
                        FOREIGN KEY (ChildID) REFERENCES Child(ChildID)
                    )
                """
                cursor.execute(create_stories_query)
                connection.commit()  # Commit the changes
                print("Table stories added to storybook DB")


    except Exception as e:
        print(f"Error occurred: {e}")
        raise DbConnectionError("Failed to add stories table to storybook DB")



#Testing
connection = get_connection()
# create_user_table()
# create_child_table()
# create_stories_table()