# main.py

import test

if __name__ == "__main__":

    # Test the algorithms and store the execution times
    naive_times_test_cases_1, kmp_times_test_cases_1, naive_times_test_cases_2, kmp_times_test_cases_2, naive_times_test_cases_3, kmp_times_test_cases_3, naive_times_test_cases_4, kmp_times_test_cases_4 = test.test_algorithms()

    # Plot the execution times
    test.plot_execution_time(naive_times_test_cases_1, kmp_times_test_cases_1, 1)
    test.plot_execution_time(naive_times_test_cases_2, kmp_times_test_cases_2, 2)
    test.plot_execution_time(naive_times_test_cases_3, kmp_times_test_cases_3, 3)
    test.plot_execution_time(naive_times_test_cases_4, kmp_times_test_cases_4, 4)