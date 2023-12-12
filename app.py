from flask import Flask, render_template
from StoryClasses import Story
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


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
