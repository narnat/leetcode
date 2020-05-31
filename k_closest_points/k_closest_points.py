#!/usr/bin/env python3
from typing import List
from random import randint


class Solution:
    ''' Using quickselect algorithm '''

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        lo, hi = 0, len(points) - 1
        while lo < hi:
            i = self.partition(points, lo, hi)
            if i == K - 1:
                break
            if i > K - 1:
                hi = i - 1
            else:
                lo = i + 1
        return points[:K]

    def partition(self, arr, lo, hi):
        idx = randint(lo, hi)
        arr[idx], arr[hi] = arr[hi], arr[idx]
        pivot = arr[hi][0] ** 2 + arr[hi][1] ** 2
        for i in range(lo, hi):
            d = arr[i][0] ** 2 + arr[i][1] ** 2
            if d < pivot:
                arr[lo], arr[i] = arr[i], arr[lo]
                lo += 1
        arr[lo], arr[hi] = arr[hi], arr[lo]
        return lo
