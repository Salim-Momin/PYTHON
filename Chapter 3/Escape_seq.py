sen = "Rizwan is not\na gay person"     #The escape seq is \n this function add new line in your program
print(sen)

sentence = "Aftab is not good at \"Among us\"."   #You can add qoutation in string using \" 
print(sentence)

#HERE THE MORE ESCAPE SEQ IN PYTHON

# Tab
print("Tab: \\t ->", "Column1\tColumn2")

# Carriage Return
print("Carriage Return: \\r ->", "12345\rABC")  # 'ABC45'

# Backspace
print("Backspace: \\b ->", "123\b45")  # Output may look like '1245'

# Form Feed (rarely used)
print("Form Feed: \\f ->", "Hello\fWorld")  # May behave differently on different consoles

# Vertical Tab (rarely used)
print("Vertical Tab: \\v ->", "Hello\vWorld")  # Same as above

# Bell (might beep in some terminals)
print("Bell: \\a ->", "Beep\a")  # Won't show visible output, might produce sound

# Octal Value (\ooo)
print("Octal: \\101 ->", "\101")  # ASCII code 101 octal = 'A'

# Hexadecimal Value (\xhh)
print("Hex: \\x41 ->", "\x41")  # ASCII hex 41 = 'A'

# Unicode 16-bit
print("Unicode 16-bit: \\u03B1 ->", "\u03B1")  # Greek letter alpha: α

# Unicode 32-bit
print("Unicode 32-bit: \\U0001F600 ->", "\U0001F600")  # 😀 emoji
print("Unicode 32-bit: \\U0001F601 ->", "\U0001F601")  # 😁 emoji


# Unicode by name
print("Unicode name: \\N{GREEK CAPITAL LETTER DELTA} ->", "\N{GREEK CAPITAL LETTER DELTA}")  # Δ

# Null character
print("Null character: \\0 ->", "Null\0Char")  # \0 won't be visible
