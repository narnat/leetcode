#!/usr/bin/env python
from typing import List


class Solution_1:
    '''
    DP solution, modified Kadane's Algorithm to handle all
    negative numbers array
    Time: (n)
    '''

    def maxSubArray(self, nums: List[int]) -> int:
        loc = 0
        gl_max = float('-inf')

        for i in range(len(nums)):
            loc = loc + nums[i]
            gl_max = max(gl_max, loc)

            if loc < 0:
                loc = 0

        return gl_max


class Solution_2:
    '''
    Divide and Conquer approach
    Time: O(nlog(n))
    '''

    def subarr(self, nums, l, r):
        if l > r:
            return float('-inf')
        mid = (l + r) // 2
        left_sum = self.subarr(nums, l, mid)
        right_sum = self.subarr(nums, mid + 1, r)
        center_l, center_r = 0, 0
        l_s, r_s = 0, 0
        for i in range(mid, l - 1, -1):
            l_s += nums[i]
            center_l = max(l_s, center_l)
        for i in range(mid + 1, r + 1):
            r_s += nums[i]
            center_r = max(r_s, center_r)
        return max(left_sum, right_sum, nums[0] + center_l + center_r)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.subarr(nums, 0, len(nums) - 1)
