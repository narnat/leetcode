#!/usr/bin/env python


class Solution_1:
    ''' DP approach '''

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        prev = 1
        cur = 2
        for i in range(2, n):
            tmp = cur
            cur += prev
            prev = tmp
        return cur


class Solution_2:
    ''' Using formula to get nth term '''

    def climbStairs(self, n: int) -> int:
        sqrt5 = pow(5, 0.5)
        phi = (1 + sqrt5) / 2
        return round(pow(phi, n + 1) / sqrt5)
