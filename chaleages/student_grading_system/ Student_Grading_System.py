#-----------------------------------------------------------------------------
# Name:        Prutha Patil
# Purpose:     progam to tell what score thsy got bassed on there  "%" 		
#
# Created:     24-Feb-2025
#-----------------------------------------------------------------------------


scor = int(input("enter your scor out of 100:"))
if scor > 89:
    print("Grade: A") 
    print("good job u didnt fail")
elif scor <89 and scor >80:
    print("Grade: B") 
elif scor <79 and scor >50:
    print("Grade: C") 
elif scor <69 and scor >60:
    print("Grade: D") 
elif scor <59 and scor >0:
    print("Grade: F") 