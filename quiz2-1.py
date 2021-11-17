# Author: ATN 11/17/21

day = input("What is the current day in the schedule? ")

day = day.capitalize()

is_meeting = ["A", "C", "E"]
not_meeting = ["B", "D", "F", "G"]

if(day in is_meeting):
    print(
        "You have class today because it is {0} day.".format(day)
        )
elif(day in not_meeting):
    print(
        "You do not have class today because it is {0} day.".format(day)
        )
else:
    print("{0} is not a valid day. ".format(day))
