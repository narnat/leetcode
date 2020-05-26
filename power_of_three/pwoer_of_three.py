#!/usr/bin/env python3


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_int_val = 3 ** 19
        return n > 0 and max_int_val % n == 0
