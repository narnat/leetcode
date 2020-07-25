#!/usr/bin/env python3
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if not nums:
            return -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        left = 0
        right = len(nums) - 1

        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot

        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
