#!/usr/bin/env python3
"""
CSC410 Assignment 1 - SAT and SMT.
Problem 1: Encodings of At-Most-k
by Victor Nicolet, Logan Murphy
"""
# You cannot import any other modules. Put all your helper functions in this file
import time
from z3 import *
import itertools
import sys
from typing import *

# ================================================================================
# ⚠️ Do not modify above!
# Your task is to write the functions 'naive' and 'sequential_counter' below.
# If you want to write your own automated tests, you can import this file into
# another file.
# Good luck!
# ================================================================================

def naive(literals: List[BoolRef], k: int, c: int = 0) -> List[BoolRef]:
    """
    Design your naive encoding of the at-most-k constraint.
    You are not allowed to create new variables for this encoding.
    The function returns the list of clauses that encode the at-most-k contraint.
    NOTE:
    The parameter c can be used to store temporary information that needs to be
    passed onto the next call of sequential_counter (see the test function.)
    """
    clauses = []

    # TODO: Replace this with your implementation
    raise Exception("naive encoder not implemented.")

    return clauses, c + 1

def sequential_counter(literals: List[BoolRef], k: int, c: int = 0) -> List[BoolRef]:
    """
    Implement the sequential counter encoding of the at-most-k constraint.
    You have to create new variables for this encoding.
    The function returns the list of clauses that encode the at-most-k constraint.
    NOTE:
    The parameter c can be used to store temporary information that needs to be
    passed onto the next call of sequential_counter (see the test function).
    """
    clauses = []
    
    # TODO: Replace this with your implementation
    raise Exception("naive encoder not implemented.")

    return clauses, c + 1

# ================================================================================
#  ⚠️ Do not modify below!
# ================================================================================

def test(encoding_function, n: int, k: int) -> None:
    """
    The following test encodes the constraint of having exactly k variables true by
    encoding at-most-k over (X_1, .., X_n) and at-least-k:
    - at-most-k is encoded by the encoding function given as argument.
    - at-least-k is encoded by encoding at-most-(n-k) on the negation of the variables.
    """
    X = []
    for i in range(n):
        X += [Bool("x_%d" % (i+1))]
    s = Solver()
    at_most_k, c = encoding_function(X, k)
    # Parameter c returned in previous call is passed as argument in next call.
    # Use it if you need it - but you cannot modify this code.
    at_least_k, c = encoding_function([Not(x) for x in X], n - k, c)
    # Add all the clauses to the solver
    for clause in at_most_k + at_least_k:
        s.add(clause)
    # Should print sat
    start = time.time()
    resp = s.check()
    end = time.time()

    if str(resp) == "sat":
        m = s.model()
        count_true = 0
        for x in X:
            try:
                if m.evaluate(x):
                    count_true += 1
            except Z3Exception:
                pass
        if count_true == k:
            print("PASSED in %fs" % (end - start))
        else:
            print("FAILED")
    else:
        print("FAILED")


def usage():
    print("Usage: python3 q1.py E N K")
    print("      - E is 0 to use naive encoding or 1 to use sequential counter encoding.")
    print("      - K and N two integers such that N >= K > 2.")


def main(argv):
    if len(argv) < 4:
        usage()
        exit(1)
    e, n, k = int(argv[1]) == 0, int(argv[2]), int(argv[3])
    if not (n >= k > 2):
        usage()
        exit(1)
    if e:
        test(naive, n, k)
    else:
        test(sequential_counter, n, k)


if __name__ == '__main__':
    main(sys.argv)
