from textwrap import dedent
from sys import exit

tasks = []
def add_task():
    """
    prompts the user to enter the number 
    of tasks and the tasks
    """
    num_of_tasks_to_add = int(input("Enter the number of tasks to add:\n"))
    for task in range(num_of_tasks_to_add):
        task = input("Enter task:\n")
        if task not in tasks:
            tasks.append(task)
            print("Task added succesfully.")
            print(f"current tasks:{tasks}")
        else:
            print("Task already exists. Choose something else")

def delete_task():
    """
    Deletes tasks from our list of tasks
    """
    task_to_delete = input("Enter task to delete:\n")

    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        print(f"Task deleted:{task_to_delete}")
        print(f"Remaining tasks:{tasks}")

    else:
        print("Invalid! No Such task exists")
        print("Add tasks:")
        add_task()
        delete_task()


def mark_completed_tasks():
    """Marks completed tasks
    """
    completed_task = input("Enter completed task:")
    if completed_task in tasks:
        print(f"{completed_task} marked successfully!")
        print("Feel free to delete it from the to do list")
    else:
        print("Invalid! No such task exists.")
        print("Add tasks first:")
        add_task()
        mark_completed_tasks()
        delete_task()



def display_menu():
    info = dedent("""
      This a simple to do list.
      You can Add, delete, mark completed 
      tasks and remove them from the list.

      To add taks: enter 1
      To delete tasks: enter 2
      To Mark Completed Task: enter 3
      To exit: Enter 4.
      What do you want to do?\n
    
      
      """)
    
    print(info)

    response = int(input("Enter a number:"))

    if response == 1:
        print("You chosen to add tasks.")
        add_task()
    elif response == 2:
        print("You've chosen to delete tasks.")
        delete_task()
    elif response == 3:
        print("You chosen to mark completed task:")
        mark_completed_tasks()
    elif response == 4:
        print("You've chosen to exit.")
        print("Exiting...")
        exit(0)
    else:
        print("Invalid! Follow the instructions in the display")
        print("Try again:")
        display_menu()

if __name__ == "__main__":
    display_menu()
