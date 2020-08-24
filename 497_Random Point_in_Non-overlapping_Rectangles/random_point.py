#!/usr/bin/env python3
import bisect
import random
from typing import List


class Solution:
    '''
    Picks points from rectangles uniformly
    '''
    def __init__(self, rects: List[List[int]]):
        weights = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        for i in range(1, len(weights)):
            weights[i] += weights[i - 1]
        self.weights = [i / weights[-1] for i in weights]
        self.rects = rects

    def pick(self) -> List[int]:
        n = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n]
        return [random.randint(x1, x2), random.randint(y1, y2)]
