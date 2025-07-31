# write a program to print the following pattern
'''
*
**
*** for n = 3
'''

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print(" "*(i-n), end="")
    print("*"* (i), end="")
    print("")