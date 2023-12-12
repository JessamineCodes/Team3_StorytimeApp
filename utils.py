from db_management import DatabaseHandler

def get_story_by_id(story_id):
    # intialise db_handler
    db_handler = DatabaseHandler()

    # fetch story details from database using fetch_query method
    try:
        fetch_story_query = f"SELECT Title, Content FROM stories WHERE StoryID = {story_id}"
        story_details = db_handler.fetch_query(fetch_story_query)

        # if there is a result then return first item in list (should only be one story, but it's returned in an array)
        if story_details:
            return story_details[0]
        else:
            return None

    finally:
        db_handler.close_connection()
