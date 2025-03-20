#-----------------------------------------------------------------------------
# Name:        Prutha
# Purpose:     Write a program that starts at `10` and counts down to `1`,
#              but if the user enters `"stop"`, the countdown should break.
#
# Created:     4-Mar-2025
#-----------------------------------------------------------------------------
count = 10

while count > 0:
    user_input = input(f"Countdown: {count} (Type 'stop' to end): ")

    if user_input.lower() == "stop":
        print("Countdown stopped!")  #to stop the countdown
        break

    count -= 1

if count == 0:
    print("Countdown finished!") #if it stops befor the user says soo
