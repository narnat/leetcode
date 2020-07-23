#!/usr/bin/env python
from typing import List


class Solution:
    '''
    Using XOR to get two numbers which occur twice
    Time: O(n)
    Memory: O(1)
    '''

    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for n in nums:
            x ^= n
        mask = x & ~(x - 1)
        n1 = 0
        for n in nums:
            if n & mask:
                n1 ^= n
        return n1, n1 ^ x
