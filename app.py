from flask import Flask, render_template, request, redirect, url_for

import sql_queries
from story_classes import  SpaceStory, DinosaurStory, PokemonStory
from db_management import StoryManager
from sql_queries import insert_story, fetch_all_user_stories
app = Flask(__name__)

# db_manager = DatabaseHandler()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # implement login logic.
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/theme', methods=['GET', 'POST'])
def select_theme():
    if request.method == 'POST':
        selected_theme = request.form['theme']
        # Redirect to the story creation page with the chosen theme
        return redirect(url_for('create', theme=selected_theme))
    return render_template('theme.html')


@app.route('/create/<theme>', methods=['GET', 'POST'])
def create(theme):
    if request.method == 'POST':
        # db_handler = db_manager

        child_name = request.form['child_name']
        child_pronouns = request.form['child_pronouns']
        child_age = request.form['child_age']
        user_id = request.form['user_id']

        # Create an instance of the appropriate story class based on the theme
        if theme == "space":
            story_instance = SpaceStory(child_name, child_pronouns, child_age)
        elif theme == "dinosaur":
            story_instance = DinosaurStory(child_name, child_pronouns, child_age)
        elif theme == "pokemon":
            story_instance = PokemonStory(child_name, child_pronouns, child_age)
        else:
            return "Invalid story theme", 400

        story_text = story_instance.generate_story()

        # Insert the story into the database
        story_title = f"{child_name}'s {theme.title()} Story"
        story_manager = StoryManager()
        story_manager.execute_query(insert_story, (story_title, story_text, child_name, user_id))
        story_id = story_manager.fetch_all_user_stories(user_id)[-1]

        print(story_id)
        return redirect(url_for('show_story', story_id=story_id))

    return render_template('create.html', theme=theme)


@app.route('/story/<int:story_id>')
def show_story(story_id):
    story_manager = StoryManager()
    story = story_manager.fetch_query(sql_queries.fetch_story_by_id, story_id)

    if story:
        return render_template('story.html', story=story)
    else:
        return "Story not found"



@app.route('/saved/<int:user_id>')
def show_saved_stories(user_id):
    story_manager = StoryManager()
    stories = story_manager.fetch_query(sql_queries.fetch_all_user_stories, user_id)

    if stories:
        return render_template('saved.html', stories=stories)
    else:
        return "No stories found"


if __name__ == '__main__':
    # automatically reload the application to reflect any changes in the code
    app.run(debug=True, port=8080)
