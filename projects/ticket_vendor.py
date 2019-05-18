TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (TICKET_PRICE * number_of_tickets) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name? " )
    num_tickets = input("Hey, {}! How many tickets would you like to buy? ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("Sorry, {}! You tried to purchase {} tickets, but only {} are available...".format(name, num_tickets, tickets_remaining))
    except ValueError as err:
        print("An error occourred: {} Please try again.".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("Final price: ${}".format(amount_due))
        proceed = input("{}, would you like to proceed to checkout? (Y/N) ".format(name))
        if proceed.lower() == 'y':
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thanks anyway, {}!".format(name))
print("Sorry, all tickets are sold out...")
