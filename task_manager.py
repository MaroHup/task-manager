def add_task():
    input_task = input("Enter the task name: ")
    task = {"name": input_task, "done": False}
    task_list.append(task)


def view_tasks():
    if not task_list:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(task_list, start=1):
            if task["done"] == True:
                status = "done"
            else:
                status = "not done yet"
            print(f"{index}. {task['name']} - {status}")


def delete_task():
    view_tasks()
    choice = input("Enter task number to delete: ")
    try:
        task_index = int(choice) - 1
        if 0 <= task_index < len(task_list):
            del task_list[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")


task_list = []

while True:
    print("Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
