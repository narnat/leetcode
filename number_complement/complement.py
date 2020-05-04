#!/usr/bin/env python3
from math import log


class Solution:
    def findComplement(self, num):
        return ~num & (1 << int(log(num, 2))) - 1

if __name__ == '__main__':
    findComplement = Solution().findComplement

    assert findComplement(5) == 2
    assert findComplement(1) == 0
    print("All good!")
