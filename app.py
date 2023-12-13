from flask import Flask, render_template, request, redirect, url_for
from StoryClasses import Story
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # implement login logic.
        # For now, redirect to the theme selection page.
        return redirect(url_for('select_theme'))
    return render_template('login.html')


@app.route('/theme_selection', methods=['GET', 'POST'])
def select_theme():
    if request.method == 'POST':
        selected_theme = request.form['theme']
        # Redirect to the story creation page with the chosen theme
        return redirect(url_for('create_story', theme=selected_theme))
    return render_template('theme_selection.html')


@app.route('/story/<int:story_id>')
def show_story(story_id):
    # Use story_id to fetch story details from your database
    story = Story.find_story_by_id(story_id)  # Fetch story using the get_story_by_id method

    # if return a result
    if story:
        # Pass the 'story' object to the template
        return render_template('story.html', story=story)
    else:
        return "Story not found"

if __name__ == '__main__':
    # automatically reload the application to reflect any changes in the code
    app.run(debug=True, port=8080)
