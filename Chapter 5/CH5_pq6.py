# Create an empty dict. Allows 4 friends to enter their language as value and use key as thier names. Assume that the names are unique.

friends = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")

friends.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")

friends.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")

friends.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")

friends.update({name : lang})

print(friends)