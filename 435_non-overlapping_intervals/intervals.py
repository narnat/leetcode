#!/usr/bin/env python3
from typing import List


class Solution:
    '''
    Interval Scheduling problem. Greedy algorithm
    Time: O(nlogn)
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        intervals.sort(key=lambda a: a[1])
        count = 1
        end = intervals[0][1]
        for i in intervals:
            if i[0] >= end:
                count += 1
                end = i[1]
        return len(intervals) - count
