def calculator():
    people_count = int(input("How many people are sharing the bill?\n"))
    if people_count <= 0:
        print("Not valid number of people, must be at least 1.")
    else:
        people_name = input("What are your names? (enter names devided by space)\n")
        name_list = people_name.split(" ")
        if len(name_list) != people_count:
            print("Number of people and number of names do not match.")
        else:
            total = float(input("What's the total bill amount? $\n"))
            if total < 0:
                print("Not valid total amount, cannot be negative.")
            else:
                tip = int(input("What percentage tip would you like to leave? (e.g., 20 for 20%)\n"))
                if tip < 0:
                    print("Not valid tip, cannot be negative.")
                else:
                    total_tip = total * (tip / 100)
                    total_with_tip = total + total_tip
                    each_person = total_with_tip / people_count
                    print("Total bill: $%0.2f" % total)
                    print("Tip (%d%%): $%0.2f" % (tip, total_tip))
                    print("Total bill plus tip: $%0.2f" % total_with_tip)
                    for name in name_list:
                        print("%s should pay: $%0.2f" % (name, each_person))
                    if tip > 20:
                        print("Thank you for your generosity!")


calculator()
