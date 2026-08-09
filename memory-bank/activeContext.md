# Active Context

## Current Work Focus
- Memory bank initialization complete
- Project is a minimal Flask + Lit webcomponent Todo app

## Recent Changes
- Initial project setup with FlaskWelApp framework

## Next Steps
- No active tasks — awaiting user direction

## Active Decisions
- None yet

## Important Patterns
- FlaskWelApp base class handles app setup, db, and blueprint registration
- Webcomponents use Jinja2 template blocks (render, form) to customize behavior
- Static assets served via `url_for('todo-item.static', ...)`

## Learnings
- `flask-socketio-lit-html` provides `FlaskWelApp`, `db`, and `configure_blueprint()` helper
- Template hierarchy: `templates/todo.html` extends `webcomponent_base.js`
- `render_template` used for main page, not webcomponent templates