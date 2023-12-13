# import mysql.connector to connect to database
import mysql.connector
# import user credentials from config file
from config import DB_HOST, DB_NAME
# dotenv module allows for .env file access
from dotenv import load_dotenv
# operating system dependent functionality
import os
# import story class instance to retrieve child's name and story text
# from StoryClasses import space_story_instance, space_story, dinosaur_story_instance, dinosaur_story
import pprint
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
                database=DB_NAME
            )

            self.cursor = self.connection.cursor()

            # Create the database if it doesn't exist
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            self.connection.commit()

            # Switch to the specified database
            self.cursor.execute(f"USE {DB_NAME}")
            self.connection.commit()

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
        except Exception as e:
            print(f"Error executing query: {e}")
            raise QueryExecutionError('Failed to execute query.')
        finally:
            cursor.close()

    # query to read the database
    def fetch_query(self, query: any):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Error executing fetch query: {e}")
            raise QueryExecutionError('Failed to execute fetch query.')
        finally:
            cursor.close()

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")






