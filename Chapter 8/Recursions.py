'''
factorial (5) X factorial(4)
factorial (5) X (4) X factorial(3)
factorial (5) X (4) X (3) X factorial(2)
factorial (5) X (4) X (3) X (2) X factorial(1)
facrorial (5) X (4) X (3) X (2) X (1) = 120
'''


def factorial(n):
    if (n==1 or n==0):
        return 1
    return n*factorial(n-1)


n = int(input("Enter the number: "))
print(f"The factorial is : {factorial(n)}")


