#-----------------------------------------------------------------------------
# Name:        Prutha
# Purpose:     Write a program that generates a random number between `1` and `10`
#              and keeps asking the user to guess it using a `while` loop **until
#              they guess correctly**.
#
# Created:     4-Mar-2025
#-----------------------------------------------------------------------------

import random

number = random.randint (1, 10)

while True :
    num_from_user = int(input("guess a number from 1 to 10:"))

    if num_from_user == number:
        print("You did ittt!!!!!")
        break

    else:
        print("try again")
