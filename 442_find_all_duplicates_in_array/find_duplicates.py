#!/usr/bin/env python3
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []

        for i, e in enumerate(nums):
            idx = abs(e) - 1
            if nums[idx] < 0:
                output.append(idx + 1)
            nums[idx] = -nums[idx]
        return output
