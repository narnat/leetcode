#!/usr/bin/env python3

class Solution:
    def maximalSquare_bf(self, matrix):
        size = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                while self.check_square(matrix, i, j, size):
                    size += 1
        return size ** 2

    def check_square(self, matrix, i, j, size):
        end_i = i + size
        end_j = j + size

        if (end_i >= len(matrix) or end_j >= len(matrix[0])):
            return False

        for x in range(i, end_i + 1):
            for y in range(j, end_j + 1):
                if matrix[x][y] != '1':
                    return False

        return True

    def maximalSquare(self, matrix):
        if not matrix or len(matrix) <= 0:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]

        maxlen = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    maxlen = max(maxlen, dp[i][j])
        return maxlen ** 2

    def maximalSquare_dp_1(self, matrix):
        if not matrix or len(matrix) <= 0:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        dp = [0] * (col + 1)
        prev = 0
        maxlen = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                val = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(dp[j - 1], dp[j], prev) + 1
                    maxlen = max(maxlen, dp[j])
                else:
                    dp[j] = 0
                prev = val
        return maxlen ** 2

    
if __name__ == '__main__':
    maximalSquare = Solution().maximalSquare
    assert maximalSquare([["1","0","1","0","0"],
                          ["1","0","1","1","1"],
                          ["1","1","1","1","1"],
                          ["1","0","0","1","0"]]) == 4

    print("All good!!!")
