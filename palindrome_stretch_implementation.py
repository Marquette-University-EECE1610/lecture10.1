"""
Goal: Write a program that detects whether a string is a palindrome.

TODO Phase 1:
- Choose an input string and store it in a variable.
- Set a flag variable that assumes the string is a palindrome.
- Use loop logic that compares characters from opposite ends of the string.
- On each step, compare the left-side character to the matching right-side character.
- If any pair does not match, update the flag and stop checking further.
- After the loop, use the flag to decide which message to print.
- Print whether the string is a palindrome or not.
- Test with multiple examples, including both palindrome and non-palindrome cases.
- Add a trace plan to show index pairs checked each iteration.

TODO Phase 2:
- Query a large dictionary of words from the internet that has definitions.
- Find the first up to 100 words that are palindromes and print them.
"""

import json
import textwrap
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def is_palindrome(text, show_trace=False):
    is_palindrome_flag = True

    for left_index in range(len(text) // 2):
        right_index = len(text) - 1 - left_index

        if show_trace:
            print(
                f"Checking {text}: index {left_index} ('{text[left_index]}') "
                f"vs index {right_index} ('{text[right_index]}')"
            )

        if text[left_index] != text[right_index]:
            is_palindrome_flag = False
            break

    return is_palindrome_flag


# Phase 1
phase_1_cases = ["racecar", "python", "level", "coding", "rotor", "openai"]

print("Phase 1 results")
for sample_text in phase_1_cases:
    result = is_palindrome(sample_text, show_trace=True)
    if result:
        print(f"{sample_text} is a palindrome.\n")
    else:
        print(f"{sample_text} is not a palindrome.\n")

phase_1_expected = {
    "racecar": True,
    "python": False,
    "level": True,
    "coding": False,
    "rotor": True,
    "openai": False,
}

for sample, expected in phase_1_expected.items():
    actual = is_palindrome(sample)
    assert actual == expected, f"Verification failed for {sample}: expected {expected}, got {actual}"

print("Phase 1 verification passed.\n")


# Phase 2
def fetch_dictionary_entries(url):
    with urlopen(url, timeout=20) as response:
        payload = response.read().decode("utf-8")
        return json.loads(payload)


def format_definition(definition_text, max_chars=200):
    single_line = " ".join(definition_text.split())
    if len(single_line) > max_chars:
        single_line = single_line[: max_chars - 3] + "..."
    return single_line or "Definition not found"


# Large dictionary dataset with definitions.
dictionary_url = (
    "https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json"
)

print("Phase 2 results")
try:
    entries = fetch_dictionary_entries(dictionary_url)
    palindrome_entries = []

    for candidate, raw_definitions in entries.items():
        clean_word = candidate.strip().lower()

        if not clean_word.isalpha() or len(clean_word) <= 1:
            continue

        if not is_palindrome(clean_word):
            continue

        extracted_definition = "Definition not found"
        if isinstance(raw_definitions, list) and raw_definitions:
            first_definition = str(raw_definitions[0]).strip()
            if first_definition:
                extracted_definition = first_definition
        elif isinstance(raw_definitions, dict):
            # Some dictionary sources use nested objects for definition text.
            nested_definition = raw_definitions.get("definition") or raw_definitions.get("meaning")
            if nested_definition:
                extracted_definition = str(nested_definition).strip()
        elif isinstance(raw_definitions, str) and raw_definitions.strip():
            extracted_definition = raw_definitions.strip()

        palindrome_entries.append((clean_word, extracted_definition))

        if len(palindrome_entries) >= 100:
            break

    palindrome_entries.sort(key=lambda item: item[0])

    print(f"Found {len(palindrome_entries)} palindrome words:")
    for index, (palindrome_word, definition) in enumerate(palindrome_entries, start=1):
        short_definition = format_definition(definition, max_chars=200)
        prefix = f"{index:3}. {palindrome_word} - "
        wrapper = textwrap.TextWrapper(width=88, initial_indent=prefix, subsequent_indent="        ")
        for line in wrapper.wrap(short_definition):
            print(line)

except (HTTPError, URLError, TimeoutError, UnicodeDecodeError, json.JSONDecodeError) as error:
    print(f"Could not retrieve words from the internet: {error}")
