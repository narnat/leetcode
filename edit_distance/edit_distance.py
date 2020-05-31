#!/usr/bin/env python3


class Solution:
    ''' Levenshtein distance '''

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                no_match = 1
                if word2[j - 1] == word1[i - 1]:
                    no_match = 0

                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] +
                               1, dp[i - 1][j - 1] + no_match)

            print(dp, '\n\n')
        return dp[m][n]


class Solution_2:
    ''' Levenshtein distance, space optimized '''

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)

        for j in range(1, n + 1):
            dp[j] = j

        for i in range(1, m + 1):
            pre = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                no_match = 1
                if word2[j - 1] == word1[i - 1]:
                    no_match = 0
                cur = dp[j]
                dp[j] = min(dp[j - 1] + 1,
                              dp[j] + 1,
                              pre + no_match)
                pre = cur
        return dp[n]


if __name__ == '__main__':
    minDistance = Solution().minDistance
    minDistance("horse", "ros")
    # minDistance("intention", "execution")
