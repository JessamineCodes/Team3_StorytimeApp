import mysql.connector
from config import HOST_NAME, DB_NAME, USER, PASS
from StoryClasses import space_story_instance, space_story,  dinosaur_story_instance, dinosaur_story


class DbConnectionError(Exception):
    pass


class QueryExecutionError(Exception):
    pass


class DatabaseHandler:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=HOST_NAME,
                user=USER,
                password=PASS
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
                    Username VARCHAR(50),
                    Email VARCHAR(100),
                    PasswordHash VARCHAR(255),
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
                        Title VARCHAR(100),
                        Content TEXT,
                        DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
                        UserID INT,
                        ChildName VARCHAR(100),
                        FOREIGN KEY (UserID) REFERENCES users(UserID)
                    )
                
            """)
            # FOREIGN KEY (UserID) REFERENCES users(UserID)
            self.connection.commit()
        except Exception as e:
            print(f"Error creating 'stories' table: {e}")
            raise DbConnectionError("Failed to add 'stories' table to storybook DB")


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

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")

db_handler = None
# Example usage
try:
    db_handler = DatabaseHandler()
    username = "megan"
    email = "megan@megan.com"
    password = "5678"

    insert_user_query = "INSERT INTO users (Username, Email, PasswordHash) VALUES (%s, %s, %s)"
    db_handler.execute_query(insert_user_query, (username, email, password))




    # Insert the space story text into the MySQL database
    insert_space_story_query = "INSERT INTO stories (Title, Content, ChildName, UserId) VALUES (%s, %s, %s, %s)"
    db_handler.execute_query(insert_space_story_query,
                             (f"{space_story_instance.child_name}'s Space Story", space_story, space_story_instance.child_name, 1))
#i'm not sure how to take the user id from Users table without inputting again
    # Insert the dinosaur story text into the MySQL database
    insert_dinosaur_story_query = "INSERT INTO stories (Title, Content, ChildName, UserId) VALUES (%s, %s, %s, %s)"
    db_handler.execute_query(insert_dinosaur_story_query,
                             (f"{dinosaur_story_instance.child_name}'s Dinosaur Story", dinosaur_story,
                              dinosaur_story_instance.child_name, 2))
finally:
    # Close the MySQL connection
    db_handler.close_connection()
