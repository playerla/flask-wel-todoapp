# Progress

## What Works (Tested)
- App starts on port 5000 with in-memory SQLite (`sqlite:///:memory:`)
- `GET /todo/all` returns `{"items":[...]}` — list of all todo indexes
- `GET /todo/<int:index>` returns `{"index":N,"todo":"text"}` — individual todo
- `POST /todo` with `{"todo":"text"}` adds a new todo and returns `{"index":N}`
- Todo text field limited to 80 characters (SQLAlchemy `String(80)`)
- Static assets served via `url_for('todo-item.static', ...)`

## What's Left to Build
- TBD — no active plan