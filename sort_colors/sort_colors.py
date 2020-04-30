#!/usr/bin/env python3


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        hi = len(nums) - 1
        k = 0
        while k <= hi:
            print(k, lo, hi)
            if nums[k] == 0:
                nums[lo], nums[k] = nums[k], nums[lo]
                k += 1
                lo += 1
            elif nums[k] == 2:
                nums[hi], nums[k] = nums[k], nums[hi]
                hi -= 1
            else:
                k += 1

if __name__ == '__main__':
    sortColors = Solution().sortColors
    arr = [2, 0, 1]
    sortColors(arr)
    assert arr == [0, 1, 2]
    print("All good!!!")
