#!/usr/bin/env python3


class Solution:
    ''' Starting from end, two pointers technique  '''

    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1

        def backspace(idx, string):
            skip = 0
            while idx >= 0:
                if string[idx] != '#' and skip == 0:
                    break
                if string[idx] == '#':
                    skip += 1
                else:
                    skip -= 1
                idx -= 1
            return idx

        while i >= 0 or j >= 0:
            i = backspace(i, S)
            j = backspace(j, T)
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
            if (j >= 0) != (i >= 0):
                return False
            i -= 1
            j -= 1
        return True
