# PVG_HelpDesk_ruleBasedExpertSystem
PVG's College of Engineering Help Desk Expert System
This is a simple web-based, rule-based expert system designed to act as a virtual help desk for PVG's College of Engineering. It provides quick answers to common questions about campus facilities, departments, and general information by applying a set of "if-then" rules.

The project is built to demonstrate the core components of an expert system within a full-stack web application: a knowledge base, an inference engine, and a user-friendly interface.

Key Features
Rule-Based Logic: A Python backend with a knowledge base of if-then rules.

Simple Web Interface: A clean and modern user interface built with basic HTML, CSS, and JavaScript.

Conversational Experience: The system responds to user queries in a chat-like format.

Easy to Extend: New rules can be added to the Python script without changing the frontend code.

How to Run the Application
Follow these steps to get the application up and running on your local machine.

Prerequisites
Python 3.x

pip (Python package installer)

1. Clone the Repository
If you haven't already, clone this repository to your local machine:

git clone https://github.com/ajinkya252005/PVG_HelpDesk_ruleBasedExpertSystem
cd PVG_HelpDesk_ruleBasedExpertSystem

2. Install Dependencies
This project requires the Flask framework for the backend. Install it using pip:

pip install Flask flask-cors

3. Start the Backend Server
Navigate to the project directory and run the Python backend. This will start a web server on http://127.0.0.1:5000.

python app.py

Important: Keep this terminal window open. The server must be running for the frontend to work.

4. Open the Frontend
With the server running, open the index.html file in your web browser. You can do this by double-clicking the file or by dragging it into a new browser tab.

The web page will load, and you can begin interacting with the expert system.

Project Structure
app.py: The Python backend. It contains the expert system's knowledge base and inference engine, and exposes an API endpoint using Flask.

index.html: The main frontend file. It provides the application's structure and user interface.

style.css: The CSS file. It handles the styling and visual design of the frontend.

script.js: The JavaScript file. It manages user interactions, sends questions to the backend API, and displays the responses.

Technologies Used
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

License
This project is licensed under the MIT License.
