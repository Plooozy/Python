def show_commands():
    print("\n=== Simple Word Counter ===")
    print("1. Add new sentence")
    print("2. Show word counts")
    print("3. Show commands")
    print("4. Exit")
    print()


def valid_choice(prompt):
    while True:
        choice = input(prompt)
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                return choice
        print("Please enter a number between 1 and 4")


def dictionary_program():
    words = []
    show_commands()
    while True:
        choice = valid_choice("Enter your choice: ")
        if choice == 1:
            sentence = input("Enter a sentence: ").lower()
            for symbol in ",.!?;:":  # Deleting symbols
                sentence = sentence.replace(symbol, "")
            words = sentence.split()
            print("Sentence saved.\n")
        elif choice == 2:
            if not words:
                print("No sentence added yet. Please add a sentence first.\n")
            else:
                dictionary = {}
                for word in words:
                    dictionary[word] = dictionary.get(word, 0) + 1
                print("Words count:")
                for key, value in dictionary.items():
                    print("%s: %d" % (key, value))
                print()
        elif choice == 3:
            show_commands()
        elif choice == 4:
            print("Exiting...")
            break