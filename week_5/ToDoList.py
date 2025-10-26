def toDoList():
    print("This is a toDoList program")
    print("Here are some commands that you can use: ")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")
    task_list = []
    choice = int(input("Enter your choice: "))
    while choice > 4 or choice < 1:
        print("Wrong choice, choice must be between 1 and 4")
        choice = int(input("Enter your choice again: "))
    if choice != 4:
        while choice != 4:
            if choice == 1:
                task = input("Enter a task: ")
                task_list.append(task)
                choice = int(input("Next choice: "))
            elif choice == 2:
                k = int(input("Remove a task by number: "))
                while k > len(task_list) or k < 1:
                    print("Invalid choice, try again")
                    k = int(input("Remove a task by number: "))
                else:
                    task_list.remove(task_list[k - 1])
                    choice = int(input("Next choice: "))
            else:
                for i in range(0, len(task_list)):
                    print(str(i + 1) + ". " + task_list[i])
                choice = int(input("Next choice: "))
        else:
            print("Exiting...")
            print("Final list is: ")
            for i in range(0, len(task_list)):
                print(str(i + 1) + ". " + task_list[i])
    else:
        print("Exiting")


toDoList()