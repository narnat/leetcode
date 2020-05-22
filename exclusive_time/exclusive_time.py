#!/usr/bin/env python3
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        from collections import deque
        stack = deque()
        res = [0] * n
        prev = 0
        for i in range(len(logs)):
            func, state, time = logs[i].split(':')
            func = int(func)
            time = int(time)
            if state == 'start':
                if len(stack) > 0:
                    res[stack[-1]] += time - prev
                stack.append(func)
                prev = time
            else:
                res[func] += time - prev + 1
                stack.pop()
                prev = time + 1
            print(prev)
            print(stack)
        return res
