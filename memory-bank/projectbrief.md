# Project Brief: Flask SocketIO Lit-HTML Todo App

## Why This Project Exists
A full-stack Todo application built as a comprehensive example demonstrating the `flask-socketio-lit-html` framework. It showcases how to build a real-time, interactive web app combining Flask backend with Lit-based webcomponents frontend.

## Problems It Solves
- Provides a clean, minimal example of full-stack web development with modern JavaScript (Lit) and Python (Flask)
- Demonstrates real-time communication via Socket.IO between client and server
- Shows how to register and use custom webcomponents in a Flask application

## How It Should Work
1. **Frontend**: Lit-based webcomponents (`<form-todo-item>`, `<ul-todo-item>`) render the Todo UI
2. **Backend**: Flask serves the HTML page and provides a `/todo/` blueprint endpoint
3. **Model**: `Todo` model stores todo items (task string, 80 char limit) in SQLite
4. **Data Flow**: Webcomponents communicate with the Flask backend via Socket.IO for real-time updates
5. **Entry Point**: `app.py` instantiates `TodoApp` which registers the blueprint and serves the main page

## Key Files
- `app.py` — Flask application entry point, defines Todo model, registers blueprint
- `templates/app.html` — Main HTML page hosting Lit webcomponents
- `templates/todo.html` — Jinja2 template for the `<ul-todo-item>` webcomponent
- `requirements.txt` — Dependencies: flask-socketio-lit-html, gunicorn