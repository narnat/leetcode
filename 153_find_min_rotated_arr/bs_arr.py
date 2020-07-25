#!/usr/bin/env python3
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        # This solution won't work when array is already sorted, so we need that condition
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid
        return nums[right]


class Solution_2:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


class Solution_3:
    ''' Regular Binary search '''

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]
