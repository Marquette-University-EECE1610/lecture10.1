"""
Goal: Write a program that detects whether a string is a palindrome.

TODO:
- Choose an input string and store it in a variable.
- Set a flag variable that assumes the string is a palindrome.
- Use loop logic that compares characters from opposite ends of the string.
- On each step, compare the left-side character to the matching right-side character.
- If any pair does not match, update the flag and stop checking further.
- After the loop, use the flag to decide which message to print.
- Print whether the string is a palindrome or not.
- Test with multiple examples, including both palindrome and non-palindrome cases.
- Add a trace plan to show index pairs checked each iteration.
"""

test_cases = ["racecar", "python", "level", "coding"]

for text in test_cases:
    is_palindrome = True

    # Trace index pairs checked in each iteration.
    for left_index in range(len(text) // 2):
        right_index = len(text) - 1 - left_index
        print(
            f"Checking {text}: index {left_index} ('{text[left_index]}') vs index {right_index} ('{text[right_index]}')"
        )

        if text[left_index] != text[right_index]:
            is_palindrome = False
            break

    if is_palindrome:
        print(f"{text} is a palindrome.\n")
    else:
        print(f"{text} is not a palindrome.\n")
