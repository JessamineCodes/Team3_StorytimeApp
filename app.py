from flask import Flask, render_template, request, redirect, url_for
from StoryClasses import Story
from db_management import DatabaseHandler
app = Flask(__name__)

db_manager = DatabaseHandler()

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
        return redirect(url_for('create_story', theme=selected_theme))
    return render_template('theme.html')

@app.route('/create_story/<theme>', methods=['GET', 'POST'])
def create_story(theme):
    if request.method == 'POST':
        child_name = request.form['child_name']
        child_pronouns = request.form['child_pronouns']
        child_age = request.form['child_age']
        story_instance = Story(child_name, child_pronouns, child_age, theme)
        story_text = story_instance.generate_story()
        # Next you would save the story and get its ID.
        # story_id = save_story_to_db(story_text)
        # return redirect(url_for('show_story', story_id=story_id))
    return render_template('create_story.html', theme=theme)


@app.route('/story/<int:story_id>')
def show_story(story_id, db_handler=db_manager):
    # Use story_id to fetch story details from your database
    story = Story.find_story_by_id(story_id, db_handler)  # Fetch story using the get_story_by_id method

    # if return a result
    if story:
        # Pass the 'story' object to the template
        return render_template('story.html', story=story)
    else:
        return "Story not found"

if __name__ == '__main__':
    # automatically reload the application to reflect any changes in the code
    app.run(debug=True, port=8080)
