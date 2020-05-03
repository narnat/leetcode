#!/usr/bin/env python3


class Solution_2:
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

class Solution:
    """
    Guaranteed O(n) solution
    Blum-Floyd-Pratt-Rivest-Tarjan
    """
    def findKthLargest(self, nums, k):
        return self.findKth(nums, len(nums) - k, 0, len(nums) - 1)

    def findKth(self, nums, k, l, r):
        length = r - l + 1
        median = [0] * ((length + 4) // 5)

        i = 0
        while i < length // 5:
            median[i] = self.get_median(nums, l + i * 5, l + i * 5 + 4)
            i += 1

        if i * 5 < length:
            median[i] = self.get_median(nums, l + i * 5, l + i * 5 + length % 5)
            i += 1

        med = median[0] if i == 1 else self.findKth(median, i // 2, 0, i - 1)


        pivot = self.partition(nums, l, r, med)
        if pivot == k:
            return nums[k]
        if pivot < k:
            return self.findKth(nums, k, pivot + 1, r)
        return self.findKth(nums, k, l, pivot - 1)

    def partition(self, arr, start, end, med):
        lo = i = start

        med_idx = arr.index(med)
        arr[med_idx], arr[end] = arr[end], arr[med_idx]
        pivot = arr[end]
        while i < end:
            if arr[i] <= pivot:
                arr[lo], arr[i] = arr[i], arr[lo]
                lo += 1
            i += 1
        arr[lo], arr[end] = arr[end], arr[lo]

        return lo

    def get_median(self, arr, start, end):
        arr[start:end + 1] = sorted(arr[start:end+1])
        return arr[(start + end) // 2]

    
if __name__ == '__main__':
    find = Solution().findKthLargest

    print(find([3, 2, 1, 5, 6, 4], 2))
