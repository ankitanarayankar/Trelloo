import json
from datetime import datetime

# Task class to define tasks
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'completed': self.completed
        }

# TaskManager class to handle task operations
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Pending"
            print(f"{idx}. {task.title} | {task.due_date} | {status}")
            print(f"   Description: {task.description}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, f, indent=4)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                tasks_data = json.load(f)
                for task_dict in tasks_data:
                    task = Task(task_dict['title'], task_dict['description'], task_dict['due_date'])
                    task.completed = task_dict['completed']
                    self.tasks.append(task)
        except FileNotFoundError:
            pass  # No saved tasks yet

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            task_manager.add_task(title, description, due_date)
            print("Task added successfully.")

        elif choice == "2":
            task_manager.list_tasks()

        elif choice == "3":
            task_manager.list_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            task_manager.mark_task_completed(index)

        elif choice == "4":
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
