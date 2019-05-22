sodas = ["Pepsi", "Coke", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "Twix", "Kitkat"]

while True:
    choice = input("Would you like a SODA, CHIPS or CANDY? ").lower()
    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that")
            continue
    except IndexError:
        print("We're all out of {}, sorry".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))
        
