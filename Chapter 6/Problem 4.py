#write a program to find whether a given username contains less than 10

username= input("Enter the username: ")

if (len(username)<10):
    print("Username is correct.")
else:
    print("Username contained extra charecter.")    