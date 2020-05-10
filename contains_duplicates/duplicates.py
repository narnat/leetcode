#!/usr/bin/env python3


class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)

    def containsDuplicate_2(self, nums):
        s = set()

        for i in nums:
            if i in s:
                return False
            s.add(i)

        return True
