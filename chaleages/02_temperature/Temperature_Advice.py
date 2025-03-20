#-----------------------------------------------------------------------------
# Name:         Prutha
# Purpose:  	Write a Python program that asks the user for the current 
#               02_temperature and suggests whether they should wear a jacket,
#               short-sleeves, or stay indoors.
#
# Day:         25-Feb-2025
#-----------------------------------------------------------------------------

temprature = int(input("Enter the temprature:"))
if temprature <= 10:
    print("It's cold outside. Wear a jacket!")
elif temprature >= 10 and temprature <= 20:
    print("its a nice day. Wear short-sleeves!")
elif temprature >= 25:
    print("It's hot outside. Stay cool!")