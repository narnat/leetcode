#!/usr/bin/env python3


class StockSpanner:
    from collections import deque

    def __init__(self):
        self.stack = deque()

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            t = self.stack.pop()
            res += t[1]
        self.stack.append((price, res))
        print(self.stack)
        return res
