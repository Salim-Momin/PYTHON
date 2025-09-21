#use len function for check the lenght of string

name = "salim_momin"

print(len(name))

#the endswith functions use for check the string ends with correct character or not

print(name.endswith("im"))

#the similar function is startswith for check the string start with correct character or not

print(name.startswith("s"))

# 🔎 Search & Check
print("salim" in name)         # Check if 'salim' in string
print(name.find("salim"))      # Find 'salim' → index
print(name.index("salim"))     # Index of 'World
print("hello".isalpha())       # All letters?
print("12345".isdigit())       # All digits?
print("   ".isspace())         # Only spaces?

# 🔠 Case Conversion
print("salim".lower())      # To lowercase
print("salim".upper())      # To uppercase
print("salim".capitalize()) # Capitalize first letter
print("salim".title())      # Capitalize each word
print("salim".swapcase())   # Swap case

# 🧼 Trimming & Replacing
print(name.strip())                 # Remove surrounding spaces
print(name.lstrip())                # Remove left spaces
print(name.rstrip())                # Remove right spaces
print(name.replace("Hello", "Hi"))  # Replace substring

# 🧱 Splitting & Joining
print("a b c".split())      # Split by space
print("a,b,c".split(','))   # Split by comma
print('-'.join(['a', 'b'])) # Join with '-'

# 📏 Other Useful Methods
print("banana".count('a'))  # Count occurrences of 'a'
print("42".zfill(5))        # Pad with zeroes → '00042'
print("hi".center(5, '-'))  # Center → '--hi-'
print("hi".ljust(5, '_'))   # Left-align with padding
print("hi".rjust(5, '_'))   # Right-align with padding
