# All Python Set Methods Example

# 1. add()
print("1. add()")
s1 = {1, 2}
s1.add(3)
print(s1)  # {1, 2, 3}

# 2. clear()
print("\n2. clear()")
s2 = {1, 2, 3}
s2.clear()
print(s2)  # set()

# 3. copy()
print("\n3. copy()")
s3 = {4, 5}
s3_copy = s3.copy()
print(s3_copy)  # {4, 5}

# 4. difference()
print("\n4. difference()")
a = {1, 2, 3}
b = {3, 4}
print(a.difference(b))  # {1, 2}

# 5. difference_update()
print("\n5. difference_update()")
a = {1, 2, 3}
b = {2, 3}
a.difference_update(b)
print(a)  # {1}

# 6. discard()
print("\n6. discard()")
s4 = {1, 2, 3}
s4.discard(2)
s4.discard(10)  # does not raise error
print(s4)  # {1, 3}

# 7. intersection()
print("\n7. intersection()")
s5 = {1, 2, 3}
s6 = {2, 3, 4}
print(s5.intersection(s6))  # {2, 3}

# 8. intersection_update()
print("\n8. intersection_update()")
s7 = {1, 2, 3}
s8 = {2, 3, 4}
s7.intersection_update(s8)
print(s7)  # {2, 3}

# 9. isdisjoint()
print("\n9. isdisjoint()")
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True

# 10. issubset()
print("\n10. issubset()")
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True

# 11. issuperset()
print("\n11. issuperset()")
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))  # True

# 12. pop()
print("\n12. pop()")
s9 = {1, 2, 3}
print(s9.pop())  # Random element (depends)

# 13. remove()
print("\n13. remove()")
s10 = {1, 2, 3}
s10.remove(2)
print(s10)  # {1, 3}
# s10.remove(5)  # This would raise KeyError

# 14. symmetric_difference()
print("\n14. symmetric_difference()")
a = {1, 2, 3}
b = {3, 4}
print(a.symmetric_difference(b))  # {1, 2, 4}

# 15. symmetric_difference_update()
print("\n15. symmetric_difference_update()")
a = {1, 2, 3}
b = {3, 4}
a.symmetric_difference_update(b)
print(a)  # {1, 2, 4}

# 16. union()
print("\n16. union()")
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}

# 17. update()
print("\n17. update()")
a = {1, 2}
a.update({3, 4})
print(a)  # {1, 2, 3, 4}
