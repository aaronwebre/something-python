name = input("Please enter your name: ")
number = int(input("Please enter a number: "))
print("Hey, {}!\nThe number is {}".format(name, number))
is_fizz = number % 3 == 0
is_buzz = number % 5 == 0

if is_fizz and is_buzz:
    print("is a FizzBuzz number.")
elif is_fizz:
    print("is a Fizz number.")
elif is_buzz:
    print("is a Buzz number.")
else:
    print("is neither a fizzy or a buzzy number.")
