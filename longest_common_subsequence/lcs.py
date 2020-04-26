#!/usr/bin/env python3

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Dynamic programming, O(nm) runtime and optimized O(m) space complexity
        we don't need the full table, two rows are sufficient
        where:
        @n: len(text1)
        @m: len(text2)
        """
        t1_l = len(text1)
        t2_l = len(text2)
        dp1 = [0] * (t2_l + 1)
        dp2 = [0] * (t2_l + 1)

        for row in range(1, t1_l + 1):
            i = row - 1
            for col in range(1, t2_l + 1):
                j = col - 1
                if text1[i] == text2[j]:
                    dp1[col] = dp2[col - 1] + 1
                else:
                    dp1[col] = max(dp1[col - 1], dp2[col])

            dp1, dp2 = dp2, dp1

        return dp2[t2_l]

    def longestCommonSubsequence_2(self, text1: str, text2: str) -> int:
        """
        Dynamic programming, O(nm) runtime and optimized O(nm) space complexity
        where:
        @n: len(text1)
        @m: len(text2)
        """
        t1_l = len(text1)
        t2_l = len(text2)
        dp = [[0] * (t2_l + 1) for _ in range(t1_l + 1)]

        for row in range(1, t1_l + 1):
            i = row - 1
            for col in range(1, t2_l + 1):
                j = col - 1
                if text1[i] == text2[j]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return dp[t1_l][t2_l]


if __name__ == '__main__':
    lcs = Solution().longestCommonSubsequence
    assert lcs("ezupkr", "ubmrapg") == 2
    assert lcs("abcde", "ace") == 3
    print("Passed!!!")
