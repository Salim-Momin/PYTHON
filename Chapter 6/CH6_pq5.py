#write a program to finds out whether a given name is present in a list or not

list = ["Aftab","Vasim","Nishant","Nakul","Salim","Pranav","Parth","Sunny","Raj","Rihan"]

name = input("Enter the name: ")

if name in list:
    print("The name is present in list.")
else:
    print("The name is not present in list.")