import mysql.connector
from config import HOST_NAME, DB_NAME, USER, PASS
from StoryClasses import Story, space_story
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

    # Create the 'stories' table if it doesn't exist
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS stories (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    child_name VARCHAR(255),
                    theme VARCHAR(255),
                    story_text TEXT
                )
            """)
            self.connection.commit()
        except Exception as e:
            print(f"Error occurred: {e}")
            raise DbConnectionError("Failed to add users table to storybook DB")
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

# Example usage
try:
    db_handler = DatabaseHandler()

    # Testing the class by creating a space story object and printing the story text
    #space_story = Story("Jo", "she", "12", "space").generate_story()
    print(space_story)

    # Insert the space story text into the MySQL database
    insert_space_story_query = "INSERT INTO stories (child_name, theme, story_text) VALUES (%s, %s, %s)"
    db_handler.execute_query(insert_space_story_query, ("Jo", "space", space_story))

    # Testing the class by creating a dino story object and printing the story text
    dino_story = Story("Rose", "she", "9", "dinosaur").generate_story()
    print(dino_story)

    # Insert the dinosaur story text into the MySQL database
    insert_dino_story_query = "INSERT INTO stories (child_name, theme, story_text) VALUES (%s, %s, %s)"
    db_handler.execute_query(insert_dino_story_query, ("Rose", "dinosaur", dino_story))


    username = "pam seale"
    email = "pam@pam.com"
    password = "1234"

    insert_user_query = "INSERT INTO users (Username, Email, PasswordHash) VALUES (%s, %s, %s)"
    db_handler.execute_query(insert_user_query, (username, email, password))

finally:
    # Close the MySQL connection
    db_handler.close_connection()
