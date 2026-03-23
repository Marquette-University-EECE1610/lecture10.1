"""
Reverse a String
This code reverses a string using a for loop. Three different approaches are shown. The first two use direct iteration
and index-based iteration to build the reversed string by adding characters to the front of result. The third approach
uses index-based iteration with a negative step to iterate through text in reverse order, adding characters to the back
of result.
"""

text = "code"
result = ""

for char in text:
    result = char + result
print(result)

result = ""
for index in range(len(text)):
    result = text[index] + result
print(result)

result = ""
print(list(range(len(text) - 1, -1, -1)))  # for debugging
for index in range(len(text) - 1, -1, -1):  # start, stop, step
    result += text[index]
print(result)
