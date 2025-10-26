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
            while choice > 4 or choice < 1:
                print("Wrong choice, choice must be between 1 and 4")
                choice = int(input("Enter your choice again: "))

            if choice == 1:
                task = input("Enter a task: ")
                task_list.append(task)
                choice = int(input("Next choice: "))

            elif choice == 2:
                if len(task_list) == 0:
                    print("No tasks to remove.")
                    choice = int(input("Next choice: "))
                    continue

                k = input("Remove a task by number (or press Enter to cancel): ")

                if k == "":
                    print("Nothing was removed.")
                    choice = int(input("Next choice: "))
                    continue

                if not k.isdigit():
                    print("Invalid input! You must enter a number.")
                    choice = int(input("Next choice: "))
                    continue

                k = int(k)
                if k > len(task_list) or k < 1:
                    print("Invalid task number.")
                else:
                    removed_task = task_list[k - 1]
                    task_list.remove(task_list[k - 1])
                    print(f"Removed task: {removed_task}")

                choice = int(input("Next choice: "))

            else:
                if len(task_list) == 0:
                    print("Your to-do list is empty.")
                else:
                    for i in range(0, len(task_list)):
                        print(str(i + 1) + ". " + task_list[i])
                choice = int(input("Next choice: "))

        else:
            print("Exiting...")
            if len(task_list) == 0:
                print("Your to-do list is empty.")
            else:
                print("Final list is: ")
                for i in range(0, len(task_list)):
                    print(str(i + 1) + ". " + task_list[i])
    else:
        print("Exiting")


toDoList()
