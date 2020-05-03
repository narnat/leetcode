#!/usr/bin/env python3


class Solution:
    def canConstruct_2(self, ransomNote, magazine):
        count = [0] * 26

        for c in magazine:
            idx = ord(c) - 97
            count[idx] += 1

        for c in ransomNote:
            idx = ord(c) - 97
            if count[idx]:
                count[idx] -= 1
            else:
                return False

        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        res = Counter(ransomNote) - Counter(magazine)
        return not res

if __name__ == '__main__':
    canConstruct = Solution().canConstruct
    assert canConstruct("a", "b") == False
    assert canConstruct("aa", "ab") == False
    assert canConstruct("aa", "aab") == True
