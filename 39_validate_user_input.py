def user_choice():
    choice = "Wrong"
    accepted_range = range(0, 10)
    within_range = False

    while not choice.isdigit() or within_range == False:
        choice = input("Enter a number between 0 to 10: ")
        if not choice.isdigit():
            print("Sorry that is not a digit!")
        if choice not in accepted_range:
            print("Entered digit is not between 0 to 10!")
    within_range = True
    return int(choice)


result = user_choice()
print(result)
