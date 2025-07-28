#A spam comment is defined as a text containing following keywords.
# "GODLIKE","YELLOW HEART","DIL SE GODLIKE","JONATHAN"
#Write a program to detect these spams.

c1 = "GODLIKE"
c2 = "YELLOW HEART"
c3 = "DIL SE GODLIKE"
c4 = "JONATHAN"

comment = input("Enter comment: ")

if ((c1 in comment) or (c2 in comment) or (c3 in comment) or (c4 in comment)):
    print("This comment is spam")
else:
    print("nothing")