# All Python Dictionary Methods Example

# 1. clear()
print("1. clear()")
d1 = {'a': 1, 'b': 2}
d1.clear()
print(d1)  # {}

# 2. copy()
print("\n2. copy()")
d2 = {'x': 10, 'y': 20}
d2_copy = d2.copy()
print(d2_copy)  # {'x': 10, 'y': 20}

# 3. fromkeys()
print("\n3. fromkeys()")
keys = ['id', 'name', 'age']
d3 = dict.fromkeys(keys, 'NULL')
print(d3)  # {'id': 'N/A', 'name': 'N/A', 'age': 'N/A'}

# 4. get()
print("\n4. get()")
d4 = {'a': 100}
print(d4.get('a'))      # 100
print(d4.get('b', 0))   # 0

# 5. items()
print("\n5. items()")
d5 = {'a': 1, 'b': 2}
print(list(d5.items()))  # [('a', 1), ('b', 2)]

# 6. keys()
print("\n6. keys()")
print(list(d5.keys()))  # ['a', 'b']

# 7. pop()
print("\n7. pop()")
d6 = {'a': 100, 'b': 2}
print(d6.pop('a'))       # 100
print(d6.pop('b'))       #2
print(d6.pop('c', 0))    # 0

# 8. popitem()
print("\n8. popitem()")
d7 = {'a': 1, 'b': 2}
print(d7.popitem())  # ('b', 2)

# 9. setdefault()
print("\n9. setdefault()")
d8 = {'lang': 'Python'}
print(d8.setdefault('lang', 'Java'))   # Python
print(d8.setdefault('level', 'Beginner'))  # Beginner
print(d8)  # {'lang': 'Python', 'level': 'Beginner'}

# 10. update()
print("\n10. update()")
d9 = {'a': 1}
d9.update({'b': 2, 'c': 3})
print(d9)  # {'a': 1, 'b': 2, 'c': 3}

# 11. values()
print("\n11. values()")
d10 = {'a':1000,'b':"b for bal",'c':"ben10"}
print(list(d10.values()))  # [1000,"b for bal","ben10"]

# 12. in operator
print("\n12. in operator")
print('a' in d9)  # True
print('z' in d9)  # False
