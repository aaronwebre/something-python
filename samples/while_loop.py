import sys

MASTER_USER = 'aaron'
username = input("Please enter your unsername: ")
attempt_count = 1
while username != MASTER_USER:
    if attempt_count > 3:
        sys.exit("Too many invalid username attempts")
    username = input("Invalid username. Try again: ")
    attempt_count += 1
print("Welcome home!")
