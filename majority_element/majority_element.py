#!/usr/bin/env python3


class Solution:
    def majorityElement(self, nums):
        """Boyer-Moore voting algorithm"""
        idx = 0
        count = 1

        for i in range(1, (len(nums))):
            count += 1 if nums[idx] == nums[i] else -1
            if count == 0:
                count = 1
                idx = i

        return nums[idx]
