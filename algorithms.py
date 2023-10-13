"""
NAIVE-STRING-MATCHER(T,P)
    n = T.length
    m = P.length
    for s = 0 to n - m
        if P[1..m] == T[s + 1..s + m]
            print "Pattern occurs with shift" s
"""

"""
KMP-MATCHER(T,P)
    n = T.length
    m = P.length
    pi = COMPUTE-PREFIX-FUNCTION(P)
    q = 0                                           # number of characters matched                 
    for i = 1 to n                                  # scan the text from left to right
        while q > 0 and P[q + 1] != T[i]            
            q = pi[q]                               # next character does not match
        if P[q + 1] == T[i]
            q = q + 1                               # next character matches
        if q == m                                   # is all of P matched?
            print "Pattern occurs with shift" i - m
            q = pi[q]                               # look for the next match

COMPUTE-PREFIX-FUNCTION(P)
    m = P.length
    let pi[1..m] be a new array
    pi[1] = 0
    k = 0
    for q = 2 to m
        while k > 0 and P[k + 1] != P[q]
            k = pi[k]
        if P[k + 1] == P[q]
            k = k + 1
        pi[q] = k
    return pi
"""


def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)
    q = 0
    occurrences = []  # Create a list to store occurrences
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q]
        if P[q] == T[i]:
            q = q + 1
        if q == m:
            #print("Pattern occurs with shift", i - m + 1)
            occurrences.append(i - m + 1)  # Add the index of the occurrence
            q = pi[q - 1]
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


def naive_string_matcher(T, P):
    n = len(T)
    m = len(P)
    occurrences = []  # Create a list to store occurrences
    for s in range(n - m + 1):
        if P == T[s:s + m]:
            #print("Pattern occurs with shift", s)
            occurrences.append(s)  # Add the index of the occurrence
    return occurrences