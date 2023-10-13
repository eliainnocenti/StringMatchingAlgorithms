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
    algorithms.kmp_matcher(text, pattern)
    kmp_time = time.time() - start_time

    return naive_time, kmp_time, naive_result

# Function to test the algorithms
def test_algorithms():
    test_cases = [
        ("abcdefg", "cd"),  # Test case 1: Basic test with a simple pattern.
        ("xyxyxy", "xy"),  # Test case 2: Multiple non-overlapping occurrences.
        ("bababababa", "aba"),  # Test case 3: Overlapping pattern.
        ("racecar", "race"),  # Test case 4: Pattern at the beginning of the text.
        ("moonlight", "light"),  # Test case 5: Pattern at the end of the text.
        ("patternpattern", "pattern"),  # Test case 6: Pattern repeated in the text.
        ("0123456789012345", "2345"),  # Test case 7: Numeric text with pattern.
        ("treefrogstreefrogs", "treefrogs"),  # Test case 8: Pattern of words.
        ("abcdeedcba", "deed"),  # Test case 9: Palindromic pattern.
        ("thisisaverylongtextwithnopattern", "pattern"),  # Test case 10: Pattern not in text.
        ("abcdefabcdef", "abcdef"),  # Test case 11: Short pattern repeated.
        ("ababababababababababab", "abab"),  # Test case 12: Repeating pattern.
        ("abcdefghi", "ijk"),  # Test case 13: Pattern not in the text.
        ("pythonisfun", "is"),  # Test case 14: Pattern at the middle of the text.
        ("", "pattern"),  # Test case 15: Empty text.
        ("z" * 100, "z" * 10),  # Test case 16: Long pattern.
        ("abcdefghijklmnopqrstuwxyz", "aeiou"),  # Test case 17: Pattern of vowels.
        ("124578915", "69"),  # Test case 18: Digits pattern.
        ("one", "two"),  # Test case 19: No match.
        ("loremipsumdolorsitamet", "ipsumdolor"),  # Test case 20: Lorem Ipsum text.
    ]

    for i, (text, pattern) in enumerate(test_cases):
        # Compare the performance of Naive and KMP algorithms for a specific test case
        naive_time, kmp_time, naive_result = compare_algorithms(text, pattern)

        # Print the results
        print("--------------------------------------------------")
        print()
        print(f"Test Case {i + 1}")
        print(f"Text: {text}")
        print(f"Pattern: {pattern}")
        print(f"Occurrences: {naive_result}")
        print("Naive String Matcher:")
        print(f"\tTime: {naive_time} seconds")
        print("KMP Matcher:")
        print(f"\tTime: {kmp_time} seconds")
        print()