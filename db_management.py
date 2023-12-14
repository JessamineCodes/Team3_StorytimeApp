# import mysql.connector to connect to database
import mysql.connector
# import user credentials from config file
from config import DB_HOST, DB_NAME
# dotenv module allows for .env file access
from dotenv import load_dotenv
# operating system dependent functionality
import os

# import story class instance to retrieve child's name and story text
from StoryClasses import space_story_instance, space_story, dinosaur_story_instance, dinosaur_story, pokemon_story_instance, pokemon_story


from pprint import pprint

load_dotenv()


# create error for DB connection exception handling
class DbConnectionError(Exception):
    pass


# create error for query execution exception handling
class QueryExecutionError(Exception):
    pass


# create class to create, connect to and populate stories database
class DatabaseHandler:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=DB_HOST,
                user= os.getenv('DB_USER'),
                password=os.getenv('DB_PASS'),
            )

            self.cursor = self.connection.cursor()

            # Create the database if it doesn't exist
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            self.connection.commit()
            print("storybook DB created (if not exists)")

            # Switch to the specified database
            self.cursor.execute(f"USE {DB_NAME}")
            self.connection.commit()
            print("storybook DB in use")

        except Exception as e:
            print(f"Error establishing database connection: {e}")
            raise DbConnectionError("Failed to connect to the database")

        try:

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    UserID INT PRIMARY KEY AUTO_INCREMENT,
                    Username VARCHAR(50) NOT NULL,
                    Email VARCHAR(100) NOT NULL UNIQUE,
                    PasswordHash VARCHAR(255) NOT NULL,
                    DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """)

            self.connection.commit()  # Commit the changes
            print("Table users added to storybook DB")
        except Exception as e:
            print(f"Error creating 'users' table: {e}")
            raise DbConnectionError("Failed to add 'users' table to storybook DB")

        try:

            # Create the 'stories' table if it doesn't exist
            self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS stories (
                        StoryID INT PRIMARY KEY AUTO_INCREMENT,
                        Title VARCHAR(100) NOT NULL,
                        Content TEXT NOT NULL,
                        DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
                        UserID INT NOT NULL,
                        ChildName VARCHAR(100) NOT NULL,
                        FOREIGN KEY (UserID) REFERENCES users(UserID)
                    )

            """)

            self.connection.commit()
            print("Table stories added to storybook DB")
        except Exception as e:
            print(f"Error creating 'stories' table: {e}")
            raise DbConnectionError("Failed to add 'stories' table to storybook DB")

    # query to write to the database
    def execute_query(self, query, data=None):

        try:
            cursor = self.connection.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("query executed: write to storybook DB")
        except Exception as e:
            print(f"Error executing query: {e}")
            raise QueryExecutionError('Failed to execute query.')
        finally:
            cursor.close()

    # query to read the database
    def fetch_query(self, query: any):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            print("query executed: read from storybook DB")
            return cursor.fetchall()

        except Exception as e:
            print(f"Error executing fetch query: {e}")
            raise QueryExecutionError('Failed to execute fetch query.')
        finally:
            if cursor is not None:
                cursor.close()

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")


db_handler = None
# example usage
if __name__ == '__main__':
    try:
        db_handler = DatabaseHandler()
        username = "megan2"
        email = "megan23@megan.com"
        password = "5678"
        userID = None

        # Insert user into the MySQL database users table
        insert_user_query = "INSERT INTO users (Username, Email, PasswordHash) VALUES (%s, %s, %s)"
        db_handler.execute_query(insert_user_query, (username, email, password))

        # Bring back most recent userID from users table (list of tuples returned)
        fetch_user_query = "SELECT max(UserID) FROM Users"
        userID = db_handler.fetch_query(fetch_user_query)[0][0]

        # Insert the space story text into the MySQL database
        insert_space_story_query = "INSERT INTO stories (Title, Content, ChildName, UserId) VALUES (%s, %s, %s, %s)"
        db_handler.execute_query(insert_space_story_query,
                                (f"{space_story_instance.child_name}'s Space Story", space_story,
                                space_story_instance.child_name, userID))

        # Insert the dinosaur story text into the MySQL database
        insert_dinosaur_story_query = "INSERT INTO stories (Title, Content, ChildName, UserId) VALUES (%s, %s, %s, %s)"
        db_handler.execute_query(insert_dinosaur_story_query,
                                (f"{dinosaur_story_instance.child_name}'s Dinosaur Story", dinosaur_story,
                                dinosaur_story_instance.child_name, userID))

        # Insert the pokemon story text into the MySQL database
        insert_pokemon_story_query = "INSERT INTO stories (Title, Content, ChildName, UserId) VALUES (%s, %s, %s, %s)"
        db_handler.execute_query(insert_pokemon_story_query,
                                (f"{pokemon_story_instance.child_name}'s Pokemon Story", pokemon_story,
                                pokemon_story_instance.child_name, userID))

        # Bring back all stories for a specific child (pprint used: list of tuples)
        fetch_all_stories_query = "SELECT Title FROM stories WHERE ChildName = 'Rose'"
        pprint(db_handler.fetch_query(fetch_all_stories_query))

    finally:
        # Close the MySQL connection
        db_handler.close_connection()
