# test_script.py
from db_management import DatabaseHandler
from StoryClasses import Story

def test_story_creation():
    db_handler = DatabaseHandler()

    try:
        # Insert user into the MySQL database
        username, email, password = "megan", "megan@megan.com", "5678"
        insert_user_query = "INSERT INTO users (Username, Email, PasswordHash) VALUES (%s, %s, %s)"
        db_handler.execute_query(insert_user_query, (username, email, password))

        # Get most recent userID
        fetch_user_query = "SELECT max(UserID) FROM Users"
        userID = db_handler.fetch_query(fetch_user_query)[0][0]

        # Create a Story instance and insert it into the database
        space_story_instance = Story("Jo", "she", "12", "space")
        space_story = space_story_instance.generate_story()
        insert_story_query = "INSERT INTO stories (Title, Content, ChildName, UserId) VALUES (%s, %s, %s, %s)"
        db_handler.execute_query(insert_story_query, (f"{space_story_instance.child_name}'s Space Story", space_story, space_story_instance.child_name, userID))

        # Retrieve and print all stories for a specific child
        fetch_stories_query = "SELECT Title FROM stories WHERE ChildName = 'Rose'"
        stories = db_handler.fetch_query(fetch_stories_query)
        print(stories)

    finally:
        db_handler.close_connection()

if __name__ == "__main__":
    test_story_creation()
