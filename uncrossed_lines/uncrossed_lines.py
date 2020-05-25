#!/usr/bin/env python3
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        ''' Space optimized DP'''
        m = len(A)
        n = len(B)
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(1, m + 1):
            idx = i % 2
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[idx][j] = dp[idx ^ 1][j - 1] + 1
                else:
                    dp[idx][j] = max(dp[idx ^ 1][j], dp[idx][j - 1])
        return dp[idx][n]

    def maxUncrossedLines_2(self, A: List[int], B: List[int]) -> int:
        ''' Longest common subsequence '''
        m = len(A)
        n = len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]
