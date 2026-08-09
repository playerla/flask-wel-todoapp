# Tech Context

## Technologies
- **Backend**: Python, Flask, Flask-SocketIO, SQLAlchemy
- **Frontend**: JavaScript, Lit (webcomponents), Socket.IO client
- **Database**: SQLite (via SQLAlchemy db.Model)
- **Template Engine**: Jinja2

## Development Setup
- **Framework**: `flask-socketio-lit-html` — Provides `FlaskWelApp`, `db` (SQLAlchemy), blueprint registration helpers
- **Install**: `pip install flask-socketio-lit-html`
- **Entry Point**: `app.py` runs on port 5000 (configurable via `PORT` env var)
- **Template Directory**: `templates/` contains `app.html` (main page) and `todo.html` (webcomponent template)

## API Endpoints (per component)
- `GET /componentname` — Static JS module (webcomponent implementation)
- `GET /componentname/all` — List of all component indexes
- `GET /componentname/<int:index>` — Component with primary key
- `DELETE /componentname/<int:index>` — Delete component
- `POST /componentname` — Create or update component via JSON
- `GET /componentname/dump` — Full database dump

## Template Blocks (webcomponent_base.js)
- `{% extends "webcomponent_base.js" %}` — Base template
- `{% block render %}` — HTML view of the component
- `{% block style %}` — CSS for the component
- `{% block form %}` — HTML form for creating/modifying components
- `{% block style_form %}` — CSS for the form

## Cache Strategy
- `Item._get()` reads cache before network requests
- GET/POST updates local `sessionStorage` cache on fetch success
- Can pre-populate `sessionStorage` with `GET /componentname/dump` for offline apps

## Technical Constraints
- Todo item text field limited to 80 characters
- Static assets (socketio-4.1.2.js, element.js) served via `url_for('todo-item.static', ...)`
- Webcomponent custom element registered via `Todo.configure_blueprint()`
- Main page renders via `render_template('app.html')`

## Verified Working Flow
1. `python3 /workspaces/flask-wel-todoapp/app.py` → starts on port 5000
2. `curl -s -X POST -H 'Content-Type: application/json' -d '{"todo": "test task"}' http://127.0.0.1:5000/todo` → `{"index":1}`
3. `curl -s http://127.0.0.1:5000/todo/all` → `{"items":[1]}`
4. `curl -s http://127.0.0.1:5000/todo/1` → `{"index":1,"todo":"test task"}`
