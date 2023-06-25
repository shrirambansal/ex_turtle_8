"""
Write a program to accept percentage from the user and display
the grade according to the following criteria:
 Marks             Grade
 > 90               A
 > 80 and <= 90     B
 >= 60 and <= 80    C
 below 60           D 
"""
percent = float(input("Enter the Percentage : "))
if percent > 90 :
    print("A") 
elif (percent > 80 and percent <= 90) :
    print("B")
elif (percent >= 60 and percent <= 80) :
    print("C")
else:
    print("D")
