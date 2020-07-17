#!/usr/bin/env python
from typing import List


class Solution_1:
    '''
    Heap based solution, also can use QuickSelect to make it faster
    Time: O(nlogk)
    Memory: O(n)
    '''

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        import heapq
        # Edge case, ro reduce heap solution frm getting O(nlog(n)) time
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count, key=count.get)


class Solution_2:
    '''
    Bucket Sort version
    Time: O(n)
    Memory: O(n)
    To use less memory, can make bucket as dict and iterate down from the
    length of nums array
    '''

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        bucket = [None] * (len(nums) + 1)

        for key, freq in count.items():
            if bucket[freq] is None:
                bucket[freq] = []
            bucket[freq].append(key)

        output = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] is not None:
                output.extend(bucket[i])
            if len(output) == k:
                break
        return output
