#Write a recursion function to calculate the sum of first natural number.

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(n) = 1 + 2 + 3 + ..... + n 
'''



def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)


n = int(input("Enter the number: "))
print(f"the sum of numbers: {sum(n)}")


