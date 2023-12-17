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
# import sql queries from sql_queries file
import sql_queries


# Function to read a file that contains environment variables
load_dotenv()

DB_CONFIG = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': DB_NAME,
    'host': DB_HOST
}

# create class to create, connect to and populate stories database
class DatabaseHandler:

    def __init__(self, db_config):
        try:
            self.connection = mysql.connector.connect(
                host=db_config['host'],
                user=db_config['user'],
                password=db_config['password'],
            )

        except Exception as e:
            print(f"Error establishing database connection: {e}")
            raise DbConnectionError("Failed to connect to the database")

    # query to write to the database
    def execute_query(self, query, data=None):

        try:
            cursor = self.connection.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error executing query: {e}")
            raise QueryExecutionError('Failed to execute query.')
        finally:
            cursor.close()

    # query to read the database
    def fetch_query(self, query, data=None):
        cursor = None
        try:
            if data:
                data = (data,)

            cursor = self.connection.cursor()
            cursor.execute(query, data)
            print(query)
            print(data)
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


class SetUpAndTearDownHandler(DatabaseHandler):

    def __init__(self, db_config=DB_CONFIG):
        super().__init__(db_config)
        self.db_config = db_config
        self.cursor = self.connection.cursor()
        self.db_handler = None

    def setup(self):

        # Create the database if it doesn't exist
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_config['database']}")
        self.connection.commit()

        # Switch to the specified database
        self.cursor.execute(f"USE {self.db_config['database']}")
        self.connection.commit()

        try:

            self.cursor.execute("""
                                CREATE TABLE IF NOT EXISTS users (
                                    UserID INT PRIMARY KEY AUTO_INCREMENT,
                                    Username VARCHAR(50) NOT NULL,
                                    Email VARCHAR(100) NOT NULL,
                                    PasswordHash VARCHAR(255) NOT NULL,
                                    DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP
                                    )
                                """)

            self.connection.commit()  # Commit the changes
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

        except Exception as e:
            print(f"Error creating 'stories' table: {e}")
            raise DbConnectionError("Failed to add 'stories' table to storybook DB")

        self.close_connection()

    def teardown(self):

        try:
            self.cursor.execute(f"DROP DATABASE {self.db_config['database']}")
            self.connection.commit()

        except mysql.connector.Error as err:
            print(f"Database {self.db_config['database']} does not exist. Dropping db failed")
        self.close_connection()


class StoryManager(DatabaseHandler):

    def __init__(self, db_config=DB_CONFIG):
        super().__init__(db_config)
        self.db_handler = None
        self.execute_query(f"USE {db_config['database']}")

    def insert_user(self, username, email, password):
        self.execute_query(sql_queries.insert_user, (username, email, password))

    def insert_story(self, story_instance, content):
        title = story_instance.get_title()
        self.execute_query(sql_queries.insert_story,
                           (title, content, story_instance.child_name, story_instance.user_id))

    def fetch_all_user_stories(self, userid):
        result = self.fetch_query(sql_queries.fetch_all_user_stories, userid)
        if result:
            return [i[0] for i in result]
        return None

    def fetch_user_id(self):
        result = self.fetch_query(sql_queries.fetch_user)
        if result:
            return result[0][0]
        else:
            return None

    def fetch_story_by_id(self, storyid):
        result = self.fetch_query(sql_queries.fetch_story_by_id, storyid)
        if result:
            return result
        else:
            return None
