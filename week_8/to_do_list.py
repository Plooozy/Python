def commands():
    print("\n1. Add a new task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")
    print("To enter command, input a number of command")

def reader(filename):
    tasks = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                task = line.strip() #
                if task:              #check that line is not empty
                    tasks.append(task)
    except FileNotFoundError:
        open(filename, "w", encoding="utf-8").close() #in case file doesn't exist we create one
    return tasks

def writer(filename, tasks):
    with open(filename, "w", encoding="utf-8") as f: # so basically this always rewrites the whole file, with
        for task in tasks:                           # the tasks we have at the moment
            f.write(task + "\n")                     # not so optimized but it just works

def add_task(task_list, filename):
    task = input("Enter a task: ")
    task_list.append(task)
    writer(filename, task_list)    # so here we rewrite the whole file every time we add a new task (:
    print("Task added: %s" % task)


def remove_task(task_list, filename):
    if not task_list:
        print("No tasks to remove.")
        return

    for i in range(0, len(task_list)):
        print(str(i + 1) + ". " + task_list[i])  # here the whole list is printed to choose what to remove

    k = input("Remove a task by number (or press Enter to cancel): ")

    if k == '':
        print("Nothing was removed.") # if user press enter he exits from removing function
        return

    if not k.isdigit():
        print("Invalid input! You must enter a number.") # check for digit
        return

    k = int(k)
    if k < 1 or k > len(task_list):
        print("Invalid task number.") # check for existing tasks
        return

    removed_task = task_list.pop(k - 1)
    writer(filename, task_list)           # here we also rewrite the whole file, but now it's kinda reasonable (:
    print("Removed task: %s" % removed_task)


def view_tasks(task_list):
    if not task_list:       # check for empty task list
        print("Your to-do list is empty.")
    else:
        print("\nYour current tasks:")
        for i in range(0, len(task_list)):
            print(str(i + 1) + ". " + task_list[i])


def get_choice():
    while True:
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice < 1 or choice > 4:
                print("Choice must be between 1 and 4.")
            else:
                return choice
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")


def to_do_list():
    filename = "tasks.txt"
    task_list = reader(filename)
    print("\n===This is a toDoList program===")
    print("Here are some commands that you can use: ")
    while True:
        commands()
        choice = get_choice()

        if choice == 1:
            add_task(task_list, filename)
        elif choice == 2:
            remove_task(task_list, filename)
        elif choice == 3:
            view_tasks(task_list)
        elif choice == 4:
            print("\nExiting...")
            if not task_list:
                print("Your to-do list is empty.")
            else:
                print("Final list:")
                for i in range(0, len(task_list)):
                    print(str(i + 1) + ". " + task_list[i])
            break

to_do_list()