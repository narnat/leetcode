#!/usr/bin/env python3


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        pattern = [0] * 26
        s = [0] * 26

        for i in range(len(s1)):
            pattern[ord(s1[i]) - ord('a')] += 1
            s[ord(s2[i]) - ord('a')] += 1

        window = len(s1) - 1
        if s == pattern:
            return True

        i = 1

        while i + window < len(s2):
            s[ord(s2[i - 1]) - ord('a')] -= 1
            s[ord(s2[i + window]) - ord('a')] += 1
            if s == pattern:
                return True
            i += 1

        return False
