from flask_socketio_lit_html.webcomponent_base import FlaskWelApp, db
from flask import render_template
from os import environ


class Todo(db.Model):
    """Todo webcomponent model"""
    todo = db.Column(db.String(80))


class TodoApp(FlaskWelApp):
    def __init__(self):
        super(TodoApp, self).__init__(__name__)
        # Register <todo-item> webcomponent to use /todo/ endpoint blueprint and custom render from todo.html jinja template
        self.register_blueprint(Todo.configure_blueprint())
        # TodoApp main page
        self.add_url_rule('/', "TodoApp", lambda : render_template('app.html'))

def app(environ, start_response=None):
    TodoApp().runApp(port=environ.get('PORT') or 5000)

if __name__ == "__main__":
    app(environ)
