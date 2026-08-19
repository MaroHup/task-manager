# Task Manager (CLI)

A simple command-line task manager built with Python, using OOP principles and JSON-based persistence.

## Features

- Add tasks
- View all tasks with their status
- Delete a task
- Mark a task as done
- Tasks persist between runs (saved to `tasks.json`)

## Why this project

Built as a practice project after completing month 1 of an AI/Python learning roadmap, focused on applying object-oriented programming (classes, encapsulation, serialization) instead of relying on plain functions and global state.

## Tech

- Python 3 (standard library only, no external dependencies)
- `json` module for persistence

## Project structure

- `Task`: represents a single task (name, done status), knows how to convert itself to/from a dict.
- `TaskManager`: owns the list of tasks, handles all operations (add/view/delete/mark done) and reading/writing `tasks.json`.
- `main()`: the CLI loop that ties everything together.

## Run it

```bash
python task_manager.py
```

## Possible next steps

- Add task priorities / due dates
- Add unit tests
- Convert to a Flask/CLI package with argparse instead of an interactive menu
