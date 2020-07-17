#!/usr/bin/env python
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        '''
        Peak valley approach
        Time: O(n)
        Memory: O(1)
        '''
        i = 0
        n = len(prices) - 1
        profit = 0
        while i < n:
            while i < n and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < n and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            profit += peak - valley
        return profit

    def maxProfit_2(self, prices: List[int]) -> int:
        '''
        Greedy Approach, but when the next day stock prices will go up
        Time: O(n)
        Memory: O(1)
        '''
        i = 0
        n = len(prices) - 1
        profit = 0
        for i in range(n):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit
