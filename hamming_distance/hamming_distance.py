#!/usr/bin/env python3


def hammingDistance(x, y):
    n = x ^ y
    count = 0
    while n:
        count += 1
        n &= n - 1

    return count
