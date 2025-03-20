#-----------------------------------------------------------------------------
# Name:        Prutha
# Purpose:     Write a program that prints numbers from `1` to `10`, but
#              **skips even numbers** using the `continue` statement.
#
# Created:     4-Mar-2025
#-----------------------------------------------------------------------------

for i in range(1, 10):
    if i % 2 == 0: #if its divide by 2
        continue
    print(i)

