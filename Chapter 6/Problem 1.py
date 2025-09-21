#Write a to find the greatest of four numbers entered by user.

n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))
n3 = int(input("Enter the number3: "))
n4 = int(input("Enter the number4: "))

if (n1>n2 and n1>n3 and n1>n4):
    print("NO:1 is greater")
elif (n2>n1 and n2>n3 and n2>n4):
    print("NO:2 is greater")    
elif (n3>n1 and n3>n2 and n3>n4):
    print("NO:3 is greater")
elif (n4>n1 and n4>n2 and n4>n3):
    print("NO:4 is greater")    
else:
    print("ERROR :)")