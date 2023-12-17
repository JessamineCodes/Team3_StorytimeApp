# import mysql.connector to connect to database
import mysql.connector
# import user credentials from config file
from config import DB_HOST, DB_NAME
# dotenv module allows for .env file access
from dotenv import load_dotenv
# operating system dependent functionality
import os
# import exception classes from utils file
from utils import DbConnectionError, QueryExecutionError
import test_data_generation as td
import SQL_queries

load_dotenv()





# create class to create, connect to and populate stories database
class DatabaseHandler:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=DB_HOST,
                user=os.getenv('DB_USER'),
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
        cursor = None
        try:
            cursor = self.connection.cursor()
            if data:
                cursor.execute(query, data)
                self.connection.commit()
                if query.lower().startswith('insert'):
                    # Return the ID of the last inserted row
                    return cursor.lastrowid
            else:
                cursor.execute(query)
            self.connection.commit()
            print("query executed: write to storybook DB")
        except Exception as e:
            print(f"Error executing query: {e}")
            raise QueryExecutionError('Failed to execute query.')
        finally:
            if cursor is not None:
                cursor.close()

    # query to read the database
    def fetch_query(self, query, data=None):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
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



class StoryManager(DatabaseHandler):

    def __init__(self):
        super().__init__()
        self.db_handler = None

    def insert_user(self, username, email, password):
        self.execute_query(SQL_queries.insert_user, (username, email, password))

    def insert_story(self, story_instance, content):
        title = story_instance.get_title()
        self.execute_query(SQL_queries.insert_story,
                           (title, content, story_instance.child_name, story_instance.user_id))

    def fetch_all_child_stories(self, child):
        result = self.fetch_query(SQL_queries.fetch_all_child_stories, child)
        if result:
            return [i[0] for i in result]
        return None

    def fetch_all_user_stories(self, userid):
        result = self.fetch_query(SQL_queries.fetch_all_user_stories, userid)
        if result:
            return [i[0] for i in result]
        return None

    def fetch_user_id(self):
        result = self.fetch_query(SQL_queries.fetch_user)
        if result:
            return result[0][0]
        return None


if __name__ == '__main__':
    try:
        db_handler = DatabaseHandler()
        story_manager = StoryManager()

        # Populating database with mock data via test_data_generation

        for x in range (td.parents):
            story_manager.insert_user(td.list_user_dicts[x]['username'], td.list_user_dicts[x]['email'], td.list_user_dicts[x]['password'])
            x += 1

        for x in range (td.total_stories):
            db_handler.execute_query(SQL_queries.insert_story, (td.list_story_dicts[x]['title'], td.list_story_dicts[x]['content'], td.list_story_dicts[x]['child_name'], td.list_story_dicts[x]['userID']))
            x += 1


    finally:
        # Close the MySQL connection
        story_manager.close_connection()

db_handler = None
