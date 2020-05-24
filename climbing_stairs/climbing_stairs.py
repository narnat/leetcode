#!/usr/bin/env python3


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        prev = 1
        cur = 2

        for i in range(3, n + 1):
            last = prev + cur
            prev = cur
            cur = last
        return last
