from db_management import get_connection, DbConnectionError, create_child_table, create_stories_table, create_user_table
from StoryClasses import Story

def add_user_to_db(username, email, password_hash):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                insert_user_query = """
                    INSERT INTO users (Username, Email, PasswordHash)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(insert_user_query, (username, email, password_hash))
                connection.commit()
                return cursor.lastrowid
    except Exception as e:
        print(f"Error occurred: {e}")
        raise DbConnectionError("Failed to add user to database")


def add_child_to_db(user_id, child_name, age, pronouns):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                insert_child_query = """
                    INSERT INTO child (UserID, ChildName, Age, Pronouns)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_child_query, (user_id, child_name, age, pronouns))
                connection.commit()
                return cursor.lastrowid
    except Exception as e:
        print(f"Error occurred: {e}")
        raise DbConnectionError("Failed to add child to database")



if __name__ == "__main__":
    # Create the necessary tables if they don't exist
    create_user_table()
    create_child_table()
    create_stories_table()

    # Insert a test user record (Charlie's parent)
    parent_username = "charlie_parent"
    parent_email = "parent@email.com"
    parent_password_hash = "placeholder_hash"

    parent_user_id = add_user_to_db(parent_username, parent_email, parent_password_hash)
    print(f"Inserted user with ID: {parent_user_id}")

    # Insert a test child record for Charlie
    test_child_name = "Charlie"
    test_child_age = 8
    test_child_pronouns = "they/them"

    child_id = add_child_to_db(parent_user_id, test_child_name, test_child_age, test_child_pronouns)
    print(f"Inserted child with ID: {child_id}")

