#!/usr/bin/env python3
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # Alternatively, loop invariant can be left <= right
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
                left += 1
            else:
                right -= 1

        return nums[left]


class Solution_2:
    '''
    This solution guarantees that left will be pivot index
    [1 1 1 1 1 1 1 1 2 1 1] here in v1 left will be 0, but in this version it is 9
    It is helpful to search in rotated sorted array with duplicates
    '''

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # Alternatively, loop invariant can be left < right
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
                left += 1
            else:
                if nums[right - 1] > nums[right]:
                    left = right
                right -= 1

        return nums[left]
