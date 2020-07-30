#!/usr/bin/env python3
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) < 2:
            return 0
        n = len(prices)

        rest, buy, sell = 0, -prices[0], -1
        for i in range(1, n):
            prev_rest = rest
            rest = max(rest, sell)
            sell = buy + prices[i]
            buy = max(buy, prev_rest - prices[i])
        return max(sell, rest)


class Solution_2:
    ''' DP, O(n) space '''

    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) < 2:
            return 0
        n = len(prices)
        rest = [0] * n
        buy = [0] * n
        sell = [0] * n
        rest[0], buy[0], sell[0] = 0, -prices[0], float('-inf')

        for i in range(1, n):
            rest[i] = max(rest[i - 1], sell[i - 1])
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            sell[i] = buy[i - 1] + prices[i]

        return max(sell[-1], rest[-1])
