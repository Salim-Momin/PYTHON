#Write a function to find the largest number between three numbers.

n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
n3 = int(input("Enter the number: "))             


def great():
    if n1 > n2 :
        print("NO:1 is greatest.")
    elif n1 > n3 :
        print("NO:1 is greatest.")
    elif n2 > n3 :
        print("NO:2 is greatest.")
    else :
        print("NO:3 is greatest.")

    
great()  