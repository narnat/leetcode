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

    def sortColors_2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for i in nums:
            count[i] += 1

        zero, one, two = count

        for i in range(zero):
            nums[i] = 0

        for i in range(zero, zero + one):
            nums[i] = 1

        for i in range(zero + one, zero + one + two):
            nums[i] = 2

if __name__ == '__main__':
    sortColors = Solution().sortColors
    arr = [2, 0, 1]
    sortColors(arr)
    assert arr == [0, 1, 2]
    print("All good!!!")
