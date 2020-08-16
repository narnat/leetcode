#!/usr/bin/env python3
from typing import List


class Solution:
    ''' Interval scheduling problem'''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 1: return 0
        points.sort(key=lambda a: a[1])
        count = 1
        end = points[0][1]
        for i in points:
            if i[0] > end:
                count += 1
                end = i[1]
        return count
