from os import system
system("clear")
from module import vowel_count
import sys

def run_all_tests():
    tests = [
        ("Banana", 3),
        ("Dart", 1),
        ("Enter", 2),
        ("Zzz", 0),
        ("123", 0),
        ("", 0),
    ]

    for i, (input_string, expected) in enumerate(tests):
        if one_test_success(input_string, expected):
            print(f"Test {i}: Pass!")
        else:
            print(f"Test {i}: Fail")
            one_or_more_failures = True

def one_test_success(input, expected):
    try:
        actual = vowel_count(input)
        print(f"Expected: {expected}, Got: {actual}")
        assert(actual == expected)
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)