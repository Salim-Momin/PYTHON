#Write a program to calculate the grade of a student from his marks 

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Grede 'F' \nBetter luck next time :( ")