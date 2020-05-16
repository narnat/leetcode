#!/usr/bin/env python3


class Solution:
    def removeDuplicates(self, nums):
        left_idx = i = 0
        while i < len(nums):
            nums[left_idx] = nums[i]
            while i < len(nums) and nums[i] == nums[left_idx]:
                i += 1
            left_idx += 1
        return left_idx
