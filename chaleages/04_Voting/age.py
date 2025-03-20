#-----------------------------------------------------------------------------
# Name:        Prutha
# Purpose:     Python program that checks if a person is eligible to vote based on their age.
#
#
# Created:     26-feb-2025
#-----------------------------------------------------------------------------

age = int (input ("what is your age:"))

if age >=18:
    print ("you can vote!!")
elif age >0 and age <=17:
    print ("sorry, too young to vote")