#!/usr/bin/env python3


class Solution:
    def findKthLargest(self, nums, k):
        return self.findKth(nums, len(nums) - k, 0, len(nums) - 1)

    def findKth_rec(self, nums, k, l, r):
        pivot = self.partition(nums, l, r)

        if pivot == k:
            return nums[k]
        if pivot < k:
            return self.findKth(nums, k, pivot + 1, r)
        return self.findKth(nums, k, l, pivot - 1)

    def findKth(self, nums, k, l, r):

        while l < r:
            pivot = self.partition(nums, l, r)
            if pivot == k:
                break
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1

        return nums[k]

    def partition(self, arr, start, end):
        pivot = arr[end]
        lo, i = start, start

        while i < end:
            if arr[i] <= pivot:
                arr[lo], arr[i] = arr[i], arr[lo]
                lo += 1
            i += 1
        arr[lo], arr[end] = arr[end], arr[lo]

        return lo


if __name__ == '__main__':
    find = Solution().findKthLargest

    print(find([3, 2, 1, 5, 6, 4], 2))
