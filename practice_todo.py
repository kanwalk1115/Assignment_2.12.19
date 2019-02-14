chores= [{"title": "priority:"}]

def menu():
    print("Press 1 to add chore: ")
    print("Press 2 to delete chore: ")
    print("Press 3 to view all chores: ")
    print("Press q to quit: ")


def add_chore():
     chore_name= input("title:")
     chore_priority= input( "Priority:")
     chore = {"title": chore_name, "priority": chore_priority}
     chores.append(chore)


index = 1
def delete_chore():
    for chore in chores:
        print(chores)
        print(chores,index(chore))
    delete_input = int(input("Name of chore which you wish to remove:"))
    delete= chores.remove(delete_input)
    return delete

def view_all_chore():
    for chore in chores:
        print(chore)


user_input = ""

while user_input != "q":
    menu()
    user_input = input("Enter your choice: ")

    if user_input == "1":
        add_chore()
    elif user_input == "2":
        delete_chore()
    elif user_input == "3":
        view_all_chore()
