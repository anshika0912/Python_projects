class Task: # Define a class named Task
    
    def __init__(self, title, description):    # Constructor method for initializing a Task object
        self.title = title  # Initialize the task title attribute
        self.description = description  # Initialize the task description attribute
        self.completed = False  # Initialize the completed attribute to False

   
    def mark_as_completed(self): # Method to mark a task as completed
        self.completed = True

    
    def __str__(self): # Method to represent a task as a string (for display purposes)
        status = "Completed" if self.completed else "Not Completed"  # Determine task status
        return f"{self.title} - {self.description} ({status})"  # Return a formatted string representation



class TaskManager: # Define a class named TaskManager
    
    def __init__(self): # Constructor method for initializing a TaskManager object
        self.tasks = []  # Initialize a list to store tasks

    
    def add_task(self, task): # Method to add a task to the task manager
        self.tasks.append(task)  # Append the given task to the list of tasks

   
    def list_tasks(self):   # Method to list all tasks in the task manager
        if not self.tasks:
            print("No tasks found.")  # Print a message if no tasks are available
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")  # Print task index and details for each task

    
    def mark_task_completed(self, task_index):  # Method to mark a task as completed by its index
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]  # Get the task based on the provided index
            task.mark_as_completed()  # Mark the task as completed
            print(f"Task '{task.title}' marked as completed.")  # Print a completion message
        else:
            print("Invalid task index.")  # Print an error message for an invalid task index

   
    def remove_completed_tasks(self):   # Method to remove completed tasks from the task manager
        self.tasks = [task for task in self.tasks if not task.completed]
        # Create a new list of tasks that are not completed (filter out completed tasks)
        print("Completed tasks removed.")  # Print a message indicating completed tasks were removed



if __name__ == "__main__":   # Sample usage of the task manager
    task_manager = TaskManager()  # Create an instance of TaskManager

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Completed Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")  # Get user input for menu choice

        if choice == "1":
            title = input("Enter task title: ")  # Get user input for task title
            description = input("Enter task description: ")  # Get user input for task description
            task = Task(title, description)  # Create a Task object
            task_manager.add_task(task)  # Add the task to the task manager
            print("Task added successfully.")  # Print a success message

        elif choice == "2":
            print("\nList of Tasks:")
            task_manager.list_tasks()  # List all tasks in the task manager

        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            task_manager.mark_task_completed(task_index)  # Mark a task as completed

        elif choice == "4":
            task_manager.remove_completed_tasks()  # Remove completed tasks from the task manager

        elif choice == "5":
            break  # Exit the program if the user chooses to quit

        else:
            print("Invalid choice. Please try again.")  # Print an error message for an invalid menu choice
