# System Patterns

## Architecture
- **FlaskWelApp** (base class from `flask_socketio_lit_html.webcomponent_base`) provides:
  - Flask application instance
  - SQLAlchemy `db` instance
  - Blueprint registration for webcomponents
- **TodoApp** extends FlaskWelApp:
  - Defines `Todo` SQLAlchemy model with `todo` column (String(80))
  - Registers `<todo-item>` webcomponent blueprint at `/todo/`
  - Serves main page at `/` via `render_template('app.html')`

## Component Relationships
```
app.html (main page)
├── <form-todo-item>  — Form for adding new todos
└── <ul-todo-item>   — List displaying todos
    └── templates/todo.html  — Jinja2 template extending webcomponent_base.js
        └── {% block render %} — Renders individual todo item (checkbox + text)
        └── {% block form %}   — Renders add-todo form (input + submit button)
```

## Critical Implementation Paths
1. **Todo Model**: `app.py:6-9` — SQLAlchemy model with single `todo` column
2. **Blueprint Registration**: `app.py:15` — `Todo.configure_blueprint()` registers webcomponent
3. **Webcomponent Template**: `templates/todo.html` — Extends `webcomponent_base.js` with render and form blocks
4. **Main Page**: `templates/app.html` — Hosts both webcomponents on page load