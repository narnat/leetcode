#!/usr/bin/env python3


class Solution:
    def intersect(self, nums1, nums2):
        from collections import Counter
        if len(nums1) < len(nums2):
            nums2, nums1 = nums1, nums2

        d = Counter(nums2)
        res = []
        for i in nums1:
            if d[i]:
                res.append(i)
                d[i] -= 1

        return res

    def intersect_2(self, nums1, nums2):
        from collections import Counter as C
        return list((C(nums1) & C(nums2)).elements())
