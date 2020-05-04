#!/usr/bin/env python3


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        idx = (m + n) - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1

        if j >= 0:
            while j >= 0:
                nums1[idx] = nums2[j]
                j -= 1
                idx -= 1


if __name__ == '__main__':
    merge = Solution().merge

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [4, 5, 6]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]
    print("All good")
