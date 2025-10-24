def toDoList():
    print("This is a toDoList program")
    print("Here are some commands that you can use: ")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")
    k = 0
    choice = int(input("Enter your choice: "))
    if choice > 4 or choice < 1:
        print("Wrong choice, choice must be between 1 and 4")
        choice = int(input("Enter your choice: "))
        while choice != 4:
            if choice == 1:
                task = input("Enter a task: ") # need to change this line
                choice = int(input("Next choice: "))
            if choice == 2:
                task = input("Remove a task by number: ") # need to find out how to change this
                choice = int(input("Next choice: "))
            if choice == 3:
                print(task)
                choice = int(input("Next choice: "))
        else:
            print("Exiting")
    else:
        print("Exiting")


toDoList()
