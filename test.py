# test.py

import time
import algorithms

# Function to compare KMP and Naive algorithms
def compare_algorithms(text, pattern):

    # Measure execution time for Naive String Matcher
    start_time = time.time()
    naive_result = algorithms.naive_string_matcher(text, pattern)
    naive_time = time.time() - start_time

    # Measure execution time for KMP Matcher
    start_time = time.time()
    kmp_result = algorithms.kmp_matcher(text, pattern)
    kmp_time = time.time() - start_time

    return naive_time, kmp_time, naive_result, kmp_result

# Function to test the algorithms
def test_algorithms():

    test_cases = [
        # TODO - check tests' comments

        # Test case 1: Basic test with a simple pattern.
        ("abcdefg", "cd"),

        # Test case 2: Multiple non-overlapping occurrences.
        ("xyxyxy", "xy"),

        # Test case 3: Overlapping pattern.
        ("bababababa", "aba"),

        # Test case 4: Pattern at the beginning of the text.
        ("racecar", "race"),

        # Test case 5: Pattern at the end of the text.
        ("moonlight", "light"),

        # Test case 6: Pattern repeated in the text.
        ("patternpattern", "pattern"),

        # Test case 7: Numeric text with pattern.
        ("0123456789012345", "2345"),

        # Test case 8: Pattern of words.
        ("treefrogstreefrogs", "treefrogs"),

        # Test case 9: Palindromic pattern.
        ("abcdeedcba", "deed"),

        # Test case 10: Pattern not in text.
        ("thisisaverylongtextwithnopattern", "pattern"),

        # Test case 11: Short pattern repeated.
        ("abcdefabcdef", "abcdef"),

        # Test case 12: Repeating pattern.
        ("ababababababababababab", "abab"),

        # Test case 13: Pattern not in the text.
        ("abcdefghi", "ijk"),

        # Test case 14: Pattern at the middle of the text.
        ("pythonisfun", "is"),

        # Test case 15: Empty text.
        ("", "pattern"),

        # Test case 16: Long pattern.
        ("z" * 100, "z" * 10),

        # Test case 17: Pattern of vowels.
        ("abcdefghijklmnopqrstuwxyz", "aeiou"),

        # Test case 18: Digits pattern.
        ("124578915", "69"),

        # Test case 19: No match.
        ("one", "two"),

        # Test case 20: Lorem Ipsum text.
        ("loremipsumdolorsitamet", "ipsumdolor"),
    ]

    test_cases_2 = [
        # FIXME - tests' comments are not correct

        # Test case 1: Pattern occurs at the beginning, Naive is faster.
        ("patternabacabac", "pattern"),  # Pattern at the beginning of the text.

        # Test case 2: Pattern occurs at the end, Naive is faster.
        ("abacabacpattern", "pattern"),  # Pattern at the end of the text.

        # Test case 3: Both algorithms perform similarly, alternating pattern and text.
        ("abacababacabacababacab", "abacab"),  # Alternating pattern and text.

        # Test case 4: Naive performs better, unbalanced text.
        ("abababababababababababababababab", "abababababab"),  # Unbalanced text.

        # Test case 5: KMP is faster, large text.
        ("a" * 1000000 + "b" * 5000, "b" * 5000),  # Large text with pattern at the end.

        # Test case 6: Both algorithms perform similarly, complex pattern.
        ("a" * 1000000 + "ab" * 25000 + "a" * 1000000, "ab" * 25000),  # Large text with complex pattern.

        # Test case 7: Naive performs better, a simpler pattern.
        ("ab" * 1000000, "abab"),  # Large text with a simpler pattern.

        # Test case 8: Both algorithms perform similarly, no pattern.
        ("abcdefghijklmnopqrstuvwxyz", "12345"),  # No pattern in the text.

        # Test case 9: KMP is faster, pattern occurs multiple times.
        ("abcabcabcabcabc", "abc")   # Pattern occurs multiple times.
    ]

    for i, (text, pattern) in enumerate(test_cases):
        # Compare the performance of Naive and KMP algorithms for a specific test case
        naive_time, kmp_time, naive_result, kmp_result = compare_algorithms(text, pattern)

        # Print the results
        print("--------------------------------------------------")
        print()
        print(f"Test Case {i + 1}")
        print(f"Text: {text}")
        print(f"Pattern: {pattern}")
        print("Naive String Matcher:")
        print(f"\tTime: {naive_time} seconds")
        print(f"\tOccurrences: {naive_result}")
        print("KMP Matcher:")
        print(f"\tTime: {kmp_time} seconds")
        print(f"\tOccurrences: {kmp_result}")
        print()

    for i, (text, pattern) in enumerate(test_cases_2):
        # Compare the performance of Naive and KMP algorithms for a specific test case
        naive_time, kmp_time, naive_result, kmp_result = compare_algorithms(text, pattern)

        # Print the results
        print("--------------------------------------------------")
        print()
        print(f"Test Case {i + 1}")
        #print(f"Text: {text}")
        #print(f"Pattern: {pattern}")
        print("Naive String Matcher:")
        print(f"\tTime: {naive_time} seconds")
        #print(f"\tOccurrences: {naive_result}")
        print("KMP Matcher:")
        print(f"\tTime: {kmp_time} seconds")
        #print(f"\tOccurrences: {kmp_result}")
        print()