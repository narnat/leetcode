#!/usr/bin/env python3

class Solution:
    def search(self, nums, target):
        left = 0
        rigth = len(nums) - 1

        if not nums:
            return -1

        while left < rigth:
            mid = left + (rigth - left) // 2
            if nums[mid] > nums[rigth]:
                left = mid + 1
            else:
                rigth = mid

        pivot = left
        left = 0
        rigth = len(nums) - 1

        if nums[pivot] <= target <= nums[rigth]:
            left = pivot
        else:
            rigth = pivot

        print(left, rigth)
        while left <= rigth:
            mid = left + (rigth - left) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] > target:
                rigth = mid - 1
            else:
                left = mid + 1

        return -1

if __name__ == '__main__':
    search = Solution().search

    arr1 = [4,5,6,7,0,1,2]
    # print(search(arr1, 0))

    arr1 = [4,5,6,0,1,2]
    # print(search(arr1, 0))

    arr1 = [1]
    print(search(arr1, 1))

    arr1 = [4,5,6,7,0,1,2]
    print(search(arr1, 3))

    arr1 = [1]
    print(search(arr1, -1))

    arr1 = [1, 3]
    print(search(arr1, 3))
