# Summary Table: type() in Python

data_examples = [
    ("Integer", 5),
    ("Float", 3.14),
    ("String", "hello"),
    ("List", [1, 2, 3]),
    ("Tuple", (1, 2)),
    ("Dictionary", {'a': 1, 'b': 2}),
    ("Set", {1, 2, 3}),
    ("Boolean", True),
    ("None", None),
    ("Function", lambda x: x + 1),
]

print(f"{'Data Type':<15} {'Example':<20} {'type() Result'}")
print("-" * 55)

for name, value in data_examples:
    print(f"{name:<15} {str(value):<20} {type(value)}")
