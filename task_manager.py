"""
Task Manager - v2
A simple CLI task manager built with OOP and JSON persistence.
"""

import json
import os

DATA_FILE = "tasks.json"


class Task:
    """Represents a single task."""

    def __init__(self, name: str, done: bool = False):
        self.name = name
        self.done = done

    def mark_done(self) -> None:
        self.done = True

    def to_dict(self) -> dict:
        """Convert the task into a JSON-serializable dict."""
        return {"name": self.name, "done": self.done}

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Rebuild a Task object from a dict (used when loading from file)."""
        return cls(name=data["name"], done=data["done"])

    def __str__(self) -> str:
        status = "done" if self.done else "not done yet"
        return f"{self.name} - {status}"


class TaskManager:
    """Manages a collection of Task objects and handles persistence."""

    def __init__(self, data_file: str = DATA_FILE):
        self.data_file = data_file
        self.tasks: list[Task] = []
        self.load()

    # ---------- persistence ----------

    def load(self) -> None:
        """Load tasks from the JSON file, if it exists."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in raw_data]

    def save(self) -> None:
        """Save current tasks to the JSON file."""
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2, ensure_ascii=False)

    # ---------- operations ----------

    def add_task(self, name: str) -> None:
        self.tasks.append(Task(name))
        self.save()

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def delete_task(self, index: int) -> bool:
        """Delete task by 1-based index. Returns True if successful."""
        real_index = index - 1
        if 0 <= real_index < len(self.tasks):
            del self.tasks[real_index]
            self.save()
            return True
        return False

    def mark_task_done(self, index: int) -> bool:
        """Mark task as done by 1-based index. Returns True if successful."""
        real_index = index - 1
        if 0 <= real_index < len(self.tasks):
            self.tasks[real_index].mark_done()
            self.save()
            return True
        return False


def get_valid_index(prompt: str) -> int | None:
    """Ask the user for a task number, return int or None if invalid input."""
    choice = input(prompt)
    try:
        return int(choice)
    except ValueError:
        print("Please enter a valid number.")
        return None


def main() -> None:
    manager = TaskManager()

    menu = (
        "\nTask Manager\n"
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Delete Task\n"
        "4. Mark Task as Done\n"
        "5. Exit"
    )

    while True:
        print(menu)
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter the task name: ").strip()
            if name:
                manager.add_task(name)
                print("Task added.")
            else:
                print("Task name cannot be empty.")

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.view_tasks()
            index = get_valid_index("Enter task number to delete: ")
            if index is not None:
                if manager.delete_task(index):
                    print("Task deleted successfully.")
                else:
                    print("Invalid task number.")

        elif choice == "4":
            manager.view_tasks()
            index = get_valid_index("Enter task number to mark as done: ")
            if index is not None:
                if manager.mark_task_done(index):
                    print("Task marked as done.")
                else:
                    print("Invalid task number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
