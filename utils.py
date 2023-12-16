

def get_story_by_id(story_id, db_handler):
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
        # can't close the connection here because it's closed in the calling function
        pass

def find_stories_by_user_id(user_id, db_handler):
    query = "SELECT StoryID, Title, Content, ChildName FROM stories WHERE UserId = %s"
    return db_handler.fetch_query(query, (user_id,))
