# test.py

import os
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
def test_algorithms(testset, n_test):

    naive_test_times = []
    kmp_test_times = []

    for i, (text, pattern) in enumerate(testset):
        # Compare the performance of Naive and KMP algorithms for a specific test case
        naive_time, kmp_time, naive_result, kmp_result = compare_algorithms(text, pattern)

        # Store the execution times
        naive_test_times.append(naive_time)
        kmp_test_times.append(kmp_time)

        # Print the results
        print("--------------------------------------------------\n")

        if n_test == '1_1':

            print(f"Test Case {n_test}: {i + 1}")
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

        else:

            print(f"Test Case {n_test}: {i + 1}")

            # Naive String Matcher:
            print("Naive String Matcher:")
            print(f"\tTime: {naive_time} seconds")
            print(f"\tNum of occurrences: {len(naive_result)}")

            # KMP Matcher:
            print("KMP Matcher:")
            print(f"\tTime: {kmp_time} seconds")
            print(f"\tNum of occurrences: {len(kmp_result)}\n")

    return naive_test_times, kmp_test_times


# Function to plot the execution time of the algorithms
def plot_execution_time(naive_time, kmp_time, n_test):

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

    # Display the plot
    plt.show()

    # Save the plot as an image with the specified test case count
    folder_name = 'out/images'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = 'execution_times_' + n_test + '.png'
    file_path = os.path.join(os.getcwd(), folder_name, file_name)

    if os.path.exists(file_path):
        user_response = input("The file already exists. Do you want to replace it? (y/n): ").lower()
        if user_response == 'y':
            plt.savefig(file_path)
            print(f"File overwritten: {file_path}")
        else:
            print("File not overwritten.")
    else:
        plt.savefig(file_path)
        print(f"New file saved: {file_path}")