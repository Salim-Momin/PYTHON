'''#here the syntax

if condition1:
    # code block if condition1 is True
elif condition2:
    # code block if condition2 is True
else:
    # code block if all above conditions are False
'''

age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Output is your eligiable to vote.

#example with elif conditions.

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
    print("Grede 'F' \nBetter luck next time")        
    

#like we use like a ladder of if-elif-else.
