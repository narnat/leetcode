#!/usr/bin/env python3


def isPerfectSquare_1(num):
    """
    Sequence of odd numbers, can be proved by getting the sum
    of n odd numbers, which equals to n^2
    """
    i = 1
    while num > 0:
        num -= i
        i -= 2
    return num == 0


def isPerfectSquare_2(num):
    """Newton's method"""
    if num == 0:
        return True

    x = num
    while x * x > num:
        x = (x + num // x) // 2
    return x ** 2 == num


def isPerfectSquare_3(num):
    """ Bitwise trick"""

    x = 0
    bit = 1 << 15
    while bit > 0:
        x |= bit
        if num < x * x:
            x ^= bit
        bit >>= 1
    return x * x == num


def isPerfectSquare(num):
    """ Binary Search solution O(logn)"""
    lo = 0
    hi = num

    while lo <= hi:
        mid = (hi + lo) // 2
        sq = mid ** 2
        if sq == num:
            return True
        if sq < num:
            lo = mid + 1
        else:
            hi = mid - 1

    return False


if __name__ == '__main__':
    print(isPerfectSquare_3(49))
