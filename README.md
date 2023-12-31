# **Team 3 Group Project**
# Once Upon AI Time - Storytelling App

## Overview

Once Upon AI Time is a user-friendly storytelling app designed to empower busy parents to create personalised and educational bedtime stories for their children. This README provides essential information to get you started with the application.

## Team Members
_All team members played a crucial role in developing Once Upon AI Time, contributing their skills and expertise in Python logic and scripting. Here's a breakdown of each team member's specific contributions:_
- **Abigail Lumb:** Front-end development, API integration, soundscape integration.
- **Abigail Ridley:** Front-end development, UI/UX design, project management, documentation.
- **Deborah Nzekwu:** API integration, Python logic for story creation, Front-end development, try and except error handling.
- **Jessamine McHugh:** Python logic, API integration, front-end development, Flask development, debugging database errors.
- **Megan Park:** Database design, unit testing.
- **Pamela Seale:** Database design, unit testing. 
- **Safiyah Zaman:** Front-end development, UI/UX design, Flask application development, Python script for Database.

## Features
- **User Authentication:** The app features a login page, visually representing user authentication. However, it's currently a mock-up with no functional user registration or authentication. A single user is hardcoded for demonstration. Future updates will introduce full user authentication capabilities.
- **Theme Selection:** Choose from engaging themes (Pokemon, Dinosaur, Space) for each story.
- **Personalised Story Creation:** Input details such as child's name, age, and pronouns to generate unique stories.
- **Dynamic Retrieval:** Easily access and display stored stories.

## Installation

1. Clone the repository: `git clone Team3_StorytimeApp`
2. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Run the file: `RUN_THIS_demo.py` and follow the prompts.
2. Run the Flask application: `python app.py`
3. Access the application in your browser at `http://localhost:8080/`
  *PLEASE NOTE: this should be run in a chrome browser for full functionality*

## Technologies

- **Python:** Core programming language for backend logic, story generation, and database interaction.
- **Flask:** Web framework for seamless integration of backend with frontend.
- **MySQL:** Database for storing user and story data.
- **dotenv:** Secure management of environment variables.
- **Requests:** Used for making API calls.
- **Random:** Employed for randomizing story templates.
- **Faker:** For generating fake data to populate database.

## Drive containing project documentation and log
[Link to folder](https://drive.google.com/drive/folders/1XGZ6XqsL-OPYqUY6oEpqjoY39EsXf3Ge?usp=sharing) containing Project Report and Activity Log.

## File tree

📦Team3_StorytimeApp
 ┣ 📂static
 ┃ ┣ 📂Audio
 ┃ ┃ ┣ 📜Pokémon.mp3
 ┃ ┃ ┣ 📜alarm.wav
 ┃ ┃ ┣ 📜ate.wav
 ┃ ┃ ┣ 📜battle.wav
 ┃ ┃ ┣ 📜beach.wav
 ┃ ┃ ┣ 📜break.wav
 ┃ ┃ ┣ 📜bubbling.wav
 ┃ ┃ ┣ 📜chime-like.wav
 ┃ ┃ ┣ 📜crying.wav
 ┃ ┃ ┣ 📜explosion.wav
 ┃ ┃ ┣ 📜flash.wav
 ┃ ┃ ┣ 📜grabbed.wav
 ┃ ┃ ┣ 📜growl.wav
 ┃ ┃ ┣ 📜jungle.wav
 ┃ ┃ ┣ 📜missed.wav
 ┃ ┃ ┣ 📜portal.wav
 ┃ ┃ ┣ 📜rainy.wav
 ┃ ┃ ┣ 📜ran.wav
 ┃ ┃ ┣ 📜roar.wav
 ┃ ┃ ┣ 📜roared.wav
 ┃ ┃ ┣ 📜roaring.wav
 ┃ ┃ ┣ 📜rubbing.wav
 ┃ ┃ ┣ 📜stormy.wav
 ┃ ┃ ┣ 📜suit.wav
 ┃ ┃ ┣ 📜tiny.wav
 ┃ ┃ ┣ 📜trapped.wav
 ┃ ┃ ┣ 📜vibration.wav
 ┃ ┃ ┣ 📜warbling.wav
 ┃ ┃ ┣ 📜whistle.wav
 ┃ ┃ ┗ 📜windy.wav
 ┃ ┣ 📂images
 ┃ ┃ ┣ 📂dinosaur
 ┃ ┃ ┃ ┗ 📜dinosaur.png
 ┃ ┃ ┣ 📂login
 ┃ ┃ ┃ ┗ 📜loginpagebg.png
 ┃ ┃ ┣ 📂pokemon
 ┃ ┃ ┃ ┗ 📜pokemon.png
 ┃ ┃ ┣ 📂space
 ┃ ┃ ┃ ┣ 📜.DS_Store
 ┃ ┃ ┃ ┗ 📜space.png
 ┃ ┃ ┣ 📜.DS_Store
 ┃ ┃ ┗ 📜book.png
 ┃ ┣ 📜.DS_Store
 ┃ ┣ 📜dinosaur.css
 ┃ ┣ 📜home.css
 ┃ ┣ 📜login.css
 ┃ ┣ 📜pokemon.css
 ┃ ┣ 📜saved.css
 ┃ ┣ 📜space.css
 ┃ ┣ 📜story.css
 ┃ ┗ 📜theme.css
 ┣ 📂templates
 ┃ ┣ 📜create.html
 ┃ ┣ 📜home.html
 ┃ ┣ 📜index.html
 ┃ ┣ 📜login.html
 ┃ ┣ 📜saved.html
 ┃ ┣ 📜story.html
 ┃ ┗ 📜theme.html
 ┣ 📜.DS_Store
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜RUN_THIS_demo.py
 ┣ 📜app.py
 ┣ 📜config.py
 ┣ 📜db_management.py
 ┣ 📜dinosaur_story_api_calls.py
 ┣ 📜dinosaur_story_components.py
 ┣ 📜mock_data_generator.py
 ┣ 📜pokemon_story_api_calls.py
 ┣ 📜pokemon_story_components.py
 ┣ 📜pronouns.py
 ┣ 📜requirements.txt
 ┣ 📜space_story_api_calls.py
 ┣ 📜space_story_components.py
 ┣ 📜sql_queries.py
 ┣ 📜story_classes.py
 ┣ 📜test_data_generation.py
 ┣ 📜test_dinosaur_story_components.py
 ┣ 📜test_pokemon_story_components.py
 ┣ 📜test_space_story_components.py
 ┣ 📜test_story_api_calls.py
 ┣ 📜test_story_classes.py
 ┗ 📜utils.py

