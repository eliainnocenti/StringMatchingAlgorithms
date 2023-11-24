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
def plot_execution_time_chart(naive_time, kmp_time, n_test):

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
    folder_name = 'out/images/charts'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = 'execution_times_' + n_test + '.png'
    file_path = os.path.join(os.getcwd(), folder_name, file_name)

    # FIXME - savefig does not work properly (blank image)

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


# Function to create the tables of the execution times
def plot_execution_times_table(naive_time, kmp_time, n_test):

    formatted_naive_time = [format_time(time) for time in naive_time]
    formatted_kmp_time = [format_time(time) for time in kmp_time]

    table_data = [ ['Test Case', 'Naive', 'KMP'] ]

    # Create a list of test cases based on the length of execution times
    for i, (naive, kmp) in enumerate(zip(formatted_naive_time, formatted_kmp_time), start=1):
        table_data.append([i, naive, kmp])

    # Create a figure to plot the execution times of both algorithms
    plt.figure(figsize=(6, 8))
    table = plt.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.2, 0.2, 0.2])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.axis('off')

    # Display the plot
    plt.show()

    # Save the plot as an image with the specified test case count
    folder_name = 'out/images/tables'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    table_file_name = 'table_execution_times_' + n_test + '.png'
    table_file_path = os.path.join(os.getcwd(), folder_name, table_file_name)

    # FIXME - savefig does not work properly (blank image)

    if os.path.exists(table_file_path):
        user_response = input("The file already exists. Do you want to replace it? (y/n): ").lower()
        if user_response == 'y':
            #plt.savefig(table_file_path)
            plt.savefig(table_file_path, bbox_inches='tight', pad_inches=0.05) # FIXME - reduce white space
            print(f"File overwritten: {table_file_path}")
        else:
            print("File not overwritten.")
    else:
        #plt.savefig(table_file_path)
        plt.savefig(table_file_path, bbox_inches='tight', pad_inches=0.05) # FIXME - reduce white space
        print(f"New file saved: {table_file_path}")


def format_time(time):
    if 'e' in str(time):
        formatted_time = f'{time:.4e}'
    else:
        formatted_time = f'{time:.4f}'

    return formatted_time