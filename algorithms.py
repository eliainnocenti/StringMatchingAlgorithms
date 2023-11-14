# algorithms.py

# T: Text, P: Pattern

def naive_string_matcher(T, P):

    n = len(T)
    m = len(P)
    occurrences = []  # Create a list to store occurrences

    for s in range(n - m + 1):
        if P == T[s:s + m]:
            # print("Pattern occurs with shift", s)
            occurrences.append(s)  # Add the index of the occurrence

    return occurrences


def kmp_matcher(T, P):

    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)
    q = 0                                                       # number of characters matched
    occurrences = []  # Create a list to store occurrences

    for i in range(n):                                          # scan the text from left to right
        while q > 0 and P[q] != T[i]:
            q = pi[q]                                           # next character does not match
        if P[q] == T[i]:
            q = q + 1                                           # next character matches
        if q == m:                                              # is all of P matched?
            # print("Pattern occurs with shift", i - m + 1)
            occurrences.append(i - m + 1)  # Add the index of the occurrence
            q = pi[q - 1]                                       # look for the next match

    return occurrences


def compute_prefix_function(P):

    m = len(P)
    pi = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k]
        if P[k] == P[q]:
            k = k + 1
        pi[q] = k

    return pi