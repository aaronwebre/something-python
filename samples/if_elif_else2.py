first_name = input("What is your first name?  ")
print("Hello,", first_name)
if first_name == "Aaron":
    print(first_name, "is kinda learing python.")
elif first_name == "Heather":
    print(first_name, "is also kinda learning.")
else:
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Ok, you're {}... If you can read...".format(age))
    print("Everyone can go ahead and learn python, {}".format(first_name))
print("Have a good one {}!".format(first_name))
