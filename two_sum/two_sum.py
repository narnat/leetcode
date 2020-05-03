#!/usr/bin/env python3


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = [-1, -1]
        for i, e in enumerate(nums):
            compl = target - e
            if e in d:
                res = [d[e], i]
                break
            d[compl] = i
        return res
