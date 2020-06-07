#!/usr/bin/env python3
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for i in people:
            queue.insert(i[1], i)
        return queue
