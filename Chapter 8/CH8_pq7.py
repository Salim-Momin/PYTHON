# Write a python function to remove a given word from a list and strip it at the same time.

def remove(List):
    s = []
    word = input("Enter the word: ")
    for item in List:
        if not(item == word):
            s.append(item.strip(word)) 
    return s 

List = ["salim","aftab","vasim","rizwan","sikander"]

print(f"{remove(List)}")
