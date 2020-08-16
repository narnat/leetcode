#!/usr/bin/env python3
from typing import List


class Solution:
    '''
    Using DP approach. We have 4 states.
    Time: O(n)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        first_buy, second_buy, first_sell, second_sell = float('-inf'), float('-inf'), 0, 0

        for price in prices:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)

        return second_sell
