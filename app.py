import os

# Function to load tasks from file
def load_tasks(filename="tasks.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

# Function to save tasks to file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to view tasks
def view_tasks(tasks):
    if tasks:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

# Function to mark a task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num] += " [Completed]"
        print(f"Task {task_num + 1} marked as complete.")
    else:
        print("Invalid task number.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
