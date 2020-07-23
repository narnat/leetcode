#!/usr/bin/env python
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - 97] += 1
            k = tuple(cnt)
            d.setdefault(k, [])
            d[k].append(s)

        return d.values()
