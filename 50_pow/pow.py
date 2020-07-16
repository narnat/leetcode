#!/usr/bin/env python


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ''' Iterative O(logn) Solution'''
        result = 1
        N = abs(n)
        while N > 0:
            if N & 1:
                result *= x
            x *= x
            N >>= 1
        return result if n >= 0 else 1 / result

    def myPow_2(self, x: float, n: int) -> float:
        ''' Recursive O(logn) Solution'''
        def power(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n & 1 == 0:  # Even
                ret = self.myPow(x, n // 2)
                return ret * ret
            ret = self.myPow(x, n // 2)
            return x * ret * ret
        ret = power(x, abs(n))
        return ret if n > -1 else 1 / ret
