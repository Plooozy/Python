def calculator():
    people = int(input("How many people are sharing the bill? "))
    total = float(input("What's the total bill amount? $"))
    tip = int(input("What percentage tip would you like to leave? (e.g., 20 for 20%) "))

    if people <= 0:
        print("Not valid number of people, must be at least 1.")
    elif total < 0:
        print("Not valid total amount, cannot be negative.")
    elif tip < 0:
        print("Not valid tip %, cannot be negative.")
    else:
        total_tip = total * (tip / 100)
        total_with_tip = total + total_tip
        each_person = total_with_tip / people

        print("Total bill plus tip: $%0.2f" % total_with_tip)
        print("Each person should pay: $%0.2f" % each_person)


calculator()