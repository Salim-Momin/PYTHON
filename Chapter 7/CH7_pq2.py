#write a program to greet all the person names stored in a list "l" and which starts with "S".  l = ["salim","Larry","Sam","Carry"]

l = ["salim","Larry","sam","Carry"]

for name in l:
    if(name.startswith("s")):
        print(f"Hello {name}")