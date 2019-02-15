
task = []

def view_all_task():
    for task in tasks



def show_menu():
    print("Press 1 to add a new task: ")
    print ("Press 2 to view all task")
    print("Press q to quit: ")

def add_new_task():
    task_name = input("Enter name of task: ")
    task_priority = input("Enter priority")

    task = {"title": task_name, "priority": task_priority}
    task_append(task_name)
    task_append(task_priority)

user_input = ""

while user_input != "q"
    show_menu()
    user_input = input ("enter your choice: ")

    if user_input
