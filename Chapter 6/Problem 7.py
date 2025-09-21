#Write a program to find the whether a given post is taking about "PYTHON" or not.

post = input("Enter the post: ")

if ("python".lower() in post.lower()):
    print("this post is taking about PYTHON.")
else:
    print("This post is trash.")    