# main.py

import algorithms
import test

def main():
    text = "acaabcabacabacacdc"
    pattern = "abacab"
    print("Naive String Matcher:")
    algorithms.naive_string_matcher(text, pattern)
    print("KMP Matcher:")
    algorithms.kmp_matcher(text, pattern)

if __name__ == "__main__":
    #main()
    test.test_algorithms()