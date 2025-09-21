#Write a program to find out whether the student has pass or not if in requires a total of 40% and at least 33% in each subject to pass.
#assume 3 subject and take marks as an input from the user.

sub1 = int(input("Enter the mark: "))
sub2 = int(input("Enter the mark: "))
sub3 = int(input("Enter the mark: "))

total = sub1+sub2+sub3

avg = total/3

print(avg)

if (avg >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33) :
    print("YOUR PASS :)")
else : 
    print("YOUR FAIL :(")
