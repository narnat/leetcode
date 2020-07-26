#!/usr/bin/env python3


class Solution:
    ''' Finding digital root, note that root cannot be equal to 0 '''

    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1
