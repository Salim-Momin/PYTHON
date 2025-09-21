# Write a python function to convert inch in centimeter.
# Formula : 1 inch = 2.54cm

def in_to_cm():
    inch = int(input("Enter the value: "))
    print(f"{inch} inch into {round(inch*(2.54))}cm")

in_to_cm()    