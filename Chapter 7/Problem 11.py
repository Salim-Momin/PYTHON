#Write a program to print the multiplecation table reverse.

n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} X {(11-i)} = {n*(11-i)}")