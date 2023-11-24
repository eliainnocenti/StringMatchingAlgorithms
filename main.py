# main.py

import test
from input import testset_1, testset_2, testset_3, testset_4
from out.times import test_times

if __name__ == "__main__":

    # Test 1 - random tests
    testset_1_1 = testset_1.testset_1_1
    testset_1_2 = testset_1.testset_1_2

    # Test 2 - tests with the same text of different sizes but same pattern in every test case
    testset_2_1 = testset_2.testset_2_1
    testset_2_2 = testset_2.testset_2_2
    testset_2_3 = testset_2.testset_2_3

    # Test 3 - tests with the same text but different patterns
    testset_3_1 = testset_3.testset_3_1

    # Test 4 - first chapter of "The Hobbit" by J.R.R. Tolkien
    testset_4_1 = testset_4.testset_4_1

    # Test the algorithms and store the execution times
    '''
    naive_times_test_1_1, kmp_times_test_1_1 = test.test_algorithms(testset_1_1, '1_1')
    naive_times_test_1_2, kmp_times_test_1_2 = test.test_algorithms(testset_1_2, '1_2')
    naive_times_test_2_1, kmp_times_test_2_1 = test.test_algorithms(testset_2_1, '2_1')
    naive_times_test_2_2, kmp_times_test_2_2 = test.test_algorithms(testset_2_2, '2_2')
    naive_times_test_2_3, kmp_times_test_2_3 = test.test_algorithms(testset_2_3, '2_3')
    naive_times_test_3_1, kmp_times_test_3_1 = test.test_algorithms(testset_3_1, '3_1')
    naive_times_test_4_1, kmp_times_test_4_1 = test.test_algorithms(testset_4_1, '4_1')
    '''

    # Plot the execution times on a chart
    '''
    test.plot_execution_time_chart(naive_times_test_1_1, kmp_times_test_1_1, '1_1')
    test.plot_execution_time_chart(naive_times_test_1_2, kmp_times_test_1_2, '1_2')
    test.plot_execution_time_chart(naive_times_test_2_1, kmp_times_test_2_1, '2_1')
    test.plot_execution_time_chart(naive_times_test_2_2, kmp_times_test_2_2, '2_2')
    test.plot_execution_time_chart(naive_times_test_2_3, kmp_times_test_2_3, '2_3')
    test.plot_execution_time_chart(naive_times_test_3_1, kmp_times_test_3_1, '3_1')
    test.plot_execution_time_chart(naive_times_test_4_1, kmp_times_test_4_1, '4_1')
    '''

    # Plot the execution times on a table
    '''
    test.plot_execution_times_table(naive_times_test_1_1, kmp_times_test_1_1, '1_1')
    test.plot_execution_times_table(naive_times_test_1_2, kmp_times_test_1_2, '1_2')
    test.plot_execution_times_table(naive_times_test_2_1, kmp_times_test_2_1, '2_1')
    test.plot_execution_times_table(naive_times_test_2_2, kmp_times_test_2_2, '2_2')
    test.plot_execution_times_table(naive_times_test_2_3, kmp_times_test_2_3, '2_3')
    test.plot_execution_times_table(naive_times_test_3_1, kmp_times_test_3_1, '3_1')
    test.plot_execution_times_table(naive_times_test_4_1, kmp_times_test_4_1, '4_1')
    '''

    test.plot_execution_times_table(test_times.naive_execution_times_3_1, test_times.kmp_execution_times_3_1, '3_1')
    test.plot_execution_times_table(test_times.naive_execution_times_4_1, test_times.kmp_execution_times_4_1, '4_1')