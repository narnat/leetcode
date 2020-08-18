#!/usr/bin/env python
from typing import List


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = list(range(10))
        for _ in range(N-1):
            out = []
            for i in res:
                j = i % 10
                if i > 0 and j + K < 10:
                    out.append(10 * i + j + K)
                if i > 0 and K > 0 and j - K >= 0:
                    out.append(10 * i + j - K)
            res = out
        return res
                
