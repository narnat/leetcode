#!/usr/bin/env python3


def hammingWeight(n):
    count = 0

    while n:
        count += 1
        n &= n - 1

    return count
