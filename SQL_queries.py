
# Insert user into the MySQL database users table
insert_user = "INSERT INTO users (Username, Email, PasswordHash) VALUES (%s, %s, %s)"

# Insert story into the MySQL database stories table
insert_story = "INSERT INTO stories (Title, Content, ChildName, UserId) VALUES (%s, %s, %s, %s)"

# Fetch userID from users table
fetch_user = "SELECT max(UserID) FROM Users"

# Fetch all stories by child name
fetch_all_child_stories = "SELECT Title FROM stories WHERE ChildName = %s"

# Fetch all stories by user ID
fetch_all_user_stories = "SELECT Title FROM stories WHERE UserID = %s"

# Fetch story by story ID
fetch_story_by_id = "SELECT Title, Content FROM stories WHERE StoryID = %s"




