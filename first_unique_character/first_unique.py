#!/usr/bin/env python3


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26

        for c in s:
            idx = ord(c) - ord('a')
            count[idx] += 1

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if count[idx] == 1:
                return i

        return -1
