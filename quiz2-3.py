# Author: ATN 11/17/21

import random

numbers = input(
    "What numbers would you like to enter? (Separated with spaces.) "
    )

numbers = numbers.split()

winning_numbers = [
    random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)
    ]

finished = (
    "The winning numbers are {0}, {1}, and {2}.".format(
        winning_numbers[0], winning_numbers[1], winning_numbers[2]
        )
    )

if(numbers[0] and numbers[1] and numbers[2] in winning_numbers):
    print(finished)
    print("You won!")
elif((numbers[0] or numbers[1]) and numbers[2] in winning_numbers):
    print(finished)
    print("You got two numbers correct!")
elif(numbers[0] or numbers[1] or numbers[2] in winning_numbers):
    print(finished)
    print("You got one number correct!")
elif(numbers[0] and numbers[1] and numbers[2] not in winning_numbers):
    print(finished)
    print("None of your numbers were correct.")
