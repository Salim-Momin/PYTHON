#Write a program to multiplication table from given number

t = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{t} X {i} = {t*i}")