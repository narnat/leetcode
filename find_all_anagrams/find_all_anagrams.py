#!/usr/bin/env python3


class Solution:
    def findAnagrams(self, s, p):
        res = []
        if len(p) > len(s):
            return res

        pattern = [0] * 26
        count = [0] * 26
        for i in range(len(p)):
            pattern[ord(p[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] += 1

        i = 1
        window = len(p) - 1
        if count == pattern:
            res.append(0)

        while i + window < len(s):
            count[ord(s[i - 1]) - ord('a')] -= 1
            count[ord(s[i + window]) - ord('a')] += 1
            if count == pattern:
                res.append(i)
            i += 1

        return res
