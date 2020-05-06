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

class Solution_2:
    """ O(n) time complexity, no need to go over the string the second time"""
    def firstUniqChar(self, s: str) -> int:
        count = [[0, -1] for _ in range(26)]

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            count[idx][0] += 1
            count[idx][1] = i

        idx = -1
        for i in count:
            if i[0] == 1 and i[1] >= 0 and (i[1] < idx or idx == -1):
                idx = i[1]

        return idx
