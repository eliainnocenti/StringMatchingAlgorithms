# test.py

import time
import algorithms
import matplotlib.pyplot as plt


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

    test_cases_1 = [
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
        # TODO - check tests' comments

        # Test case 1: Pattern at the beginning of the text.
        ("patternabacabac", "pattern"),

        # Test case 2: Pattern at the end of the text.
        ("abacabacpattern", "pattern"),

        # Test case 3: Alternating pattern and text.
        ("abacababacabacababacab", "abacab"),

        # Test case 4: Unbalanced text.
        ("abababababababababababababababab", "abababababab"),

        # Test case 5: Large text with pattern at the end.
        ("a" * 1000000 + "b" * 5000, "b" * 5000),

        # Test case 6: Large text with complex pattern.
        ("a" * 1000000 + "ab" * 25000 + "a" * 1000000, "ab" * 25000),

        # Test case 7: Large text with a simpler pattern.
        ("ab" * 1000000, "abab"),

        # Test case 8: No pattern in the text.
        ("abcdefghijklmnopqrstuvwxyz", "12345"),

        # Test case 9: Pattern occurs multiple times.
        ("abcabcabcabcabc", "abc"),

        # Test case 10: Long text with a randomized complex pattern.
        ("abcdefghijklmnopqrstuwxyz" * 20000, "pqrs" * 5000 + "uvwxyz" * 5000),

        # Test case 11: Long text with an alternating pattern.
        ("0101010101" * 100000, "01" * 50000),

        # Test case 12: Long text with an overlapping pattern.
        ("abcdefgh" * 50000, "abcd" * 25000),

        # Test case 13: Long text with a complex pattern.
        ("a1b2c3d4e5f6g7h8i9j0" * 5000, "12345" * 1000 + "j0" * 1000),

        # Test case 14: Long text with a complex pattern.
        ("!@#$%^&*()_+=" * 25000, "!@#$" * 5000),

        # Test case 15: Long text with a repeating pattern.
        ("abcdefgh" * 100000, "abcdefgh" * 50000),

        # Test case 16: Large text with a randomized complex pattern.
        ("0123456789" * 200000, "56789" * 40000 + "23456" * 40000),

        # Test case 17: Large text with pattern at the end.
        ("a" * 1000000 + "b" * 5000, "b" * 5000),

        # Test case 18: Large text with complex pattern.
        ("a" * 1000000 + "ab" * 25000 + "a" * 1000000, "ab" * 25000),

        # Test case 19: Large text with a simpler pattern.
        ("ab" * 1000000, "abab"),

        # Test case 20: Large text with a complex pattern at the end.
        ("a" * 1000000 + "ab" * 25000 + "a" * 1000000, "ab" * 25000),

        # Test case 21: Large text with a simple pattern.
        ("ab" * 1000000, "abab"),

        # Test case 22: Long text with a randomized complex pattern at the beginning.
        ("0123456789" * 200000, "01234" * 40000),

        # Test case 23: Large text with a complex pattern at the end.
        ("abcdefghijklmnopqrstuvwxyz" * 50000, "uvwxyz" * 10000),

        # Test case 24: Long text with a randomized complex pattern in the middle.
        ("abcdefghijklmnopqrstuwxyz" * 100000, "pqrs" * 25000 + "uvwxyz" * 25000),

        # Test case 25: Long text with an alternating pattern.
        ("0101010101" * 50000, "01" * 25000)

    ]

    # Times for the first part of the assignment (test cases 1)
    naive_times_test_cases_1 = []
    kmp_times_test_cases_1 = []

    for i, (text, pattern) in enumerate(test_cases_1):
        # Compare the performance of Naive and KMP algorithms for a specific test case
        naive_time, kmp_time, naive_result, kmp_result = compare_algorithms(text, pattern)

        # Store the execution times
        naive_times_test_cases_1.append(naive_time)
        kmp_times_test_cases_1.append(kmp_time)

        # Print the results
        print("--------------------------------------------------\n")

        print(f"Test Case {i + 1}")
        print(f"Text: {text}")
        print(f"Pattern: {pattern}")

        # Naive String Matcher:
        print("Naive String Matcher:")
        print(f"\tTime: {naive_time} seconds")
        print(f"\tOccurrences: {naive_result}")

        # KMP Matcher:
        print("KMP Matcher:")
        print(f"\tTime: {kmp_time} seconds")
        print(f"\tOccurrences: {kmp_result}\n")

    # Times for the second part of the assignment (test cases 2)
    naive_times_test_cases_2 = []
    kmp_times_test_cases_2 = []

    for i, (text, pattern) in enumerate(test_cases_2):
        # Compare the performance of Naive and KMP algorithms for a specific test case
        naive_time, kmp_time, naive_result, kmp_result = compare_algorithms(text, pattern)

        # Store the execution times
        naive_times_test_cases_2.append(naive_time)
        kmp_times_test_cases_2.append(kmp_time)

        # Print the results
        print("--------------------------------------------------\n")

        print(f"Test Case {i + 1}")
        # print(f"Text: {text}")
        # print(f"Pattern: {pattern}")

        # Naive String Matcher:
        print("Naive String Matcher:")
        print(f"\tTime: {naive_time} seconds")
        print(f"\tNum of occurrences: {len(naive_result)}")

        # KMP Matcher:
        print("KMP Matcher:")
        print(f"\tTime: {kmp_time} seconds")
        print(f"\tNum of occurrences: {len(kmp_result)}\n")

    return naive_times_test_cases_1, kmp_times_test_cases_1, naive_times_test_cases_2, kmp_times_test_cases_2


# Function to plot the execution time of the algorithms
def plot_execution_time(naive_time, kmp_time, n_test_cases):

    # Create a list of test cases based on the length of execution times
    test_cases = list(range(1, len(naive_time) + 1))

    # Create a figure to plot the execution times of both algorithms
    plt.figure(figsize=(10, 6))
    plt.plot(test_cases, naive_time, marker='o', label='Naive Matcher')
    plt.plot(test_cases, kmp_time, marker='o', label='KMP Matcher')
    plt.xlabel('Test Cases')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Comparison of Naive and KMP Matcher Execution Times')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Set x-axis ticks to display all test case numbers
    plt.xticks(test_cases)

    # Save the plot as an image with the specified test case count
    file_name = 'execution_times_' + str(n_test_cases) + '.png'
    plt.savefig(file_name)

    # Display the plot
    plt.show()