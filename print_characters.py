"""
Print Characters in a String
This code demonstrates two ways to print each character in a string on a separate line. The first loop uses direct
iteration, while the second loop uses index-based iteration. Note that in the second loop, we use text[index] to access
the character at the current index.
"""

text = "engineer"

# Write your loop below this line.
for char in text:
    print(char)

for index in range(len(text)):
    print(text[index])
