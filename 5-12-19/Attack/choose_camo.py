def choose_camo():
    chosen_camo =[]

    camo_number = 0
    user_input = 0

    print("Please input the camouflaged gate combinations, one at a time. \n")
    print("1 - AND \n")
    print("2 - NAND \n")
    print("3 - OR \n")
    print("4 - NOR \n")
    print("5 - XOR \n")
    print("6 - XNOR \n")
    print("7 - End \n")

    user_input = input("Selection: ")

    while user_input != 7:
        if user_input == 1:
            chosen_camo.append('AND')
        elif user_input == 2:
            chosen_camo.append('NAND')
        elif user_input == 3:
            chosen_camo.append('OR')
        elif user_input == 4:
            chosen_camo.append('NOR')
        elif user_input == 5:
            chosen_camo.append('XOR')
        elif user_input == 6:
            chosen_camo.append('XNOR')
        else:
            break
