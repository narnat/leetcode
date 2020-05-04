#!/usr/bin/env python3


class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    plus_one = Solution().plusOne
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([9, 9, 9]) == [1, 0, 0, 0]
    print("All good!!!")
