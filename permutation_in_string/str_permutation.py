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

    def checkInclusion_2(self, s1: str, s2: str) -> bool:
        ''' Optimized count checking'''
        if len(s1) > len(s2):
            return False

        pattern = [0] * 26
        s = [0] * 26

        for i in range(len(s1)):
            pattern[ord(s1[i]) - ord('a')] += 1
            s[ord(s2[i]) - ord('a')] += 1
        matches = 0
        window = len(s1)
        for i in range(len(pattern)):
            if pattern[i] == s[i]:
                matches += 1
        for i in range(len(s2) - len(s1)):
            if matches == 26:
                return True
            left = ord(s2[i]) - ord('a')
            right = ord(s2[i + window]) - ord('a')
            s[left] -= 1
            if s[left] == pattern[left]:
                matches += 1
            elif s[left] == pattern[left] - 1:
                matches -= 1
            s[right] += 1
            if s[right] == pattern[right]:
                matches += 1
            elif s[right] == pattern[right] + 1:
                matches -= 1

        return matches == 26
