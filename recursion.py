#!/usr/bin/python2.7


# Computes the two given sequences lexographically.
def compareTo(a, b):
    # The case where one input is a prefix of the other.
    if not a or not b:
        return (not b) - (not a)
    # Continue onwards if the first characters are equal.
    elif a[:1] == b[:1]:
        return compareTo(a[1:], b[1:])
    # Exit upon seeing a difference in leading characters.
    else:
        return -1 if a[:1] < b[:1] else 1


# Computes the nth term in the Fibonacci sequence
def fib(n):
    # The base case that handles the zeroth and first terms.
    if n <= 1:
        return n
    # The recursive case implemented the standard formula.
    else:
        return fib(n - 1) + fib(n - 2)


# Computes the greatest common denominator of its inputs.
def gcd(a, b):
    # Ensure that a < b.
    if b > a:
        return gcd(b, a)
    # Continue if b does not divide a evenly.
    elif a % b:
        return gcd(b, a % b)
    # The base case where b divides a evenly.
    else:
        return b